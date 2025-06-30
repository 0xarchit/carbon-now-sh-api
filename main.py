from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from playwright.async_api import async_playwright
import urllib.parse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def generate_code_image(code: str, output_file: str = "code.jpg"):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        await page.set_viewport_size({"width": 512, "height": 512})
        
        params = {
            "code": code,
            "theme": "seti",
            "fontFamily": "Hack",
            "fontSize": "12px",
            "lineNumbers": "false",
            "windowControls": "false",
            "widthAdjustment": "false",
            "paddingVertical": "32px",
            "paddingHorizontal": "32px",
            "shadow": "false",
            "exportSize": "1x",
            "watermark": "false",
            "backgroundColor": "rgba(171,184,195,1)",
            "width": "512",
            "height": "512"
        }
        carbon_url = f"https://carbon.now.sh/?{urllib.parse.urlencode(params)}"
        
        await page.goto(carbon_url, wait_until="networkidle")
        
        element = await page.query_selector("#export-container")
        if not element:
            await browser.close()
            raise Exception("Code container not found")
        
        await element.screenshot(path=output_file, type="jpeg", quality=90)
        await browser.close()
        return output_file

@app.get("/generate-image")
async def generate_image(code: str):
    try:
        output_file = "code.jpg"
        await generate_code_image(code, output_file)
        return FileResponse(output_file, media_type="image/jpeg")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))