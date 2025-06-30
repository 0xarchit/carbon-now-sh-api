# Carbon Code Image Generator

A FastAPI service that generates beautiful code images using Carbon.now.sh. Convert your code into shareable JPG images with customizable styling.

## Features

- 🖼️ Generate high-quality code images in JPG format
- 🎨 Pre-configured with Seti theme and Hack font
- 📐 Optimized for jpg output
- 🚀 Fast API with CORS support
- 🎯 Clean, minimal design without watermarks

## Installation & Usage

1. Build the Docker image:
```bash
docker build -t carbon-api .
```

2. Run the container:
```bash
docker run -p 8000:8000 carbon-api
```

3. Generate code image:
```
GET /generate-image?code=YOUR_CODE_HERE
```

### Example
```bash
curl "http://localhost:8000/generate-image?code=console.log('Hello World');"
```

Returns a JPG image of your formatted code.

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/generate-image` | GET | Generate code image from query parameter |

## Configuration

The service uses these Carbon.now.sh settings:
- **Theme**: Seti
- **Font**: Hack (12px)
- **Format**: JPG (90% quality)
- **No line numbers, window controls, or watermarks**

## Live Demo

🚀 **Try it now**: [https://zeroxcarbon.onrender.com/docs](https://zeroxcarbon.onrender.com/docs)

Interactive API documentation with live testing capabilities.

## Deployment

Ready for deployment on any Docker-compatible platform including AWS, Google Cloud, Azure, or Render.