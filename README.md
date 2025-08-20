# Calculator Service 🧮

A modern, responsive calculator web application with REST API endpoints, built with Flask and designed for cloud-native deployments.

![Calculator Service](https://img.shields.io/badge/Python-3.11-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)
![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Compatible-326CE5.svg)

## ✨ Features

- **🎨 Modern UI**: Responsive calculator interface with keyboard support
- **🚀 REST API**: Full-featured API endpoints for all operations
- **⌨️ Keyboard Navigation**: Complete keyboard support for accessibility
- **🔒 Input Validation**: Comprehensive error handling and validation
- **🐳 Docker Ready**: Containerized for easy deployment
- **☸️ Kubernetes Compatible**: Production-ready for cloud deployments
- **📱 Mobile Responsive**: Works seamlessly on all device sizes

## 🎯 Use Cases

This calculator service was built as a **cloud-native demo application** for:

- **Testing Frameworks**: Perfect for API testing, integration testing, and end-to-end testing
- **Kubernetes Demos**: Ideal for demonstrating deployments, services, and scaling
- **CI/CD Pipelines**: Simple application for testing automation workflows
- **Monitoring & Observability**: Great for testing logging, metrics, and tracing
- **Load Testing**: Multiple endpoints for performance testing scenarios
- **Security Testing**: API endpoints for security scanning and validation

## 🛠️ Technology Stack

- **Backend**: Python 3.11 + Flask
- **Frontend**: Vanilla JavaScript + Modern CSS
- **Containerization**: Docker
- **Deployment**: Kubernetes-ready
- **Production Server**: Gunicorn

## 🚀 Quick Start

### Local Development

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/calculator-service.git
   cd calculator-service
   ```

2. **Set up virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**

   ```bash
   python app.py
   ```

5. **Access the application**
   - Web UI: [http://localhost:5000](http://localhost:5000)
   - API Health Check: [http://localhost:5000/health](http://localhost:5000/health)

### Docker Deployment

#### Build the image

```bash
docker build -t calculator-service .
```

#### Run the container

```bash
docker run -p 5000:5000 calculator-service
```

#### Using pre-built image

```bash
docker run -p 5000:5000 atulinfracloud/calculator-service:latest
```

### Kubernetes Deployment

```bash
kubectl apply -f k8s/
```

## 📚 API Documentation

### Health Check

```http
GET /health
```

**Response:**

```json
{
  "status": "healthy",
  "service": "calculator"
}
```

### Mathematical Operations

#### Addition

```http
GET /add?a=5&b=3
```

**Response:**

```json
{
  "operation": "addition",
  "a": 5,
  "b": 3,
  "result": 8
}
```

## Web Interface

The calculator includes a fully functional web interface with:

- Visual Calculator: Click or touch interface
- Keyboard Support: Full keyboard navigation
- Numbers: 0-9
- Operations: +, -, *, /
- Actions: Enter (calculate), Escape (clear), Backspace
- Error Handling: Visual feedback for invalid operations
- Responsive Design: Works on desktop, tablet, and mobile

## 🧪 Testing the API

Using curl

```bash
# Test addition
curl "http://localhost:5000/add?a=5&b=3"
```

## 🔧 Configuration

### Environment Variables

- **FLASK_ENV**: Set to production for production deployment
- **PORT**: Application port (default: 5000)
- **WORKERS**: Number of Gunicorn workers (default: 2)