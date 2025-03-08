# Camera App Project

A full-stack web application featuring camera streaming with image processing capabilities, built with Django backend, React frontend, and Docker containerization.

## Created by: alexchen9419
## Date: 2025-02-18

## 📋 Features

- **Django Backend:**
  - REST API with GET, POST, PUT, DELETE endpoints
  - Internal and external request handling via port-forwarding
  - Camera streaming functionality
  - Real-time grayscale image processing
  - SQLite database integration

- **React Frontend:**
  - Form components (input fields, dropdowns, buttons)
  - Camera stream display
  - Data fetching and manipulation interface
  - Responsive design with Bootstrap

- **Docker Integration:**
  - Complete containerization of both frontend and backend
  - Volume mounting for data persistence
  - Container orchestration via Docker Compose

## 🔧 Requirements

- Docker and Docker Compose
- Web camera connected to your system
- For development: Python 3.9+, Node.js 16+

## 🚀 Quick Start

### Using Docker (Recommended)

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd camera_app_project
   ```

2. Build and start the containers:
   ```bash
   cd docker
   docker-compose up --build
   ```

3. Access the application:
   - Frontend: http://localhost
   - Backend API: http://localhost/api/
   - Camera Stream: http://localhost/camera/

### Manual Development Setup

#### Backend Setup:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Linux/Mac or venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

#### Frontend Setup:
```bash
cd frontend
npm install
npm start
```

## 📖 Usage Guide

### API Endpoints

- **GET /api/internal-get/**: Test internal GET request
- **GET /api/external-get/**: Test external GET request (via port-forwarding)
- **GET /api/items/**: List all items
- **POST /api/items/**: Create a new item
- **GET /api/items/{id}/**: Retrieve a specific item
- **PUT /api/items/{id}/**: Update a specific item
- **DELETE /api/items/{id}/**: Delete a specific item
- **GET /camera/**: View camera stream in browser
- **GET /camera/grayscale/**: View grayscale processed camera stream

### Frontend Pages

- **Home**: Dashboard with API test results
- **Items**: CRUD operations for database items
- **Camera View**: Live camera stream with grayscale processing option

## 🏗️ Project Structure

```
camera_app_project/
├── backend/                # Django backend
│   ├── api/                # API application
│   ├── camera_app/         # Main project config
│   ├── camera_stream/      # Camera streaming application
│   ├── db.sqlite3          # SQLite database
│   ├── manage.py
│   └── requirements.txt    # Backend dependencies
├── frontend/               # React frontend
│   ├── public/
│   ├── src/
│   ├── package.json
│   └── ...
└── docker/                 # Docker configuration
    ├── Dockerfile.backend
    ├── Dockerfile.frontend
    ├── docker-compose.yml
    └── nginx.conf
```

## 🔍 Key Implementation Details

### 1. Camera Streaming
The application captures video from the connected camera and streams it to the browser using multipart HTTP responses.

### 2. Image Processing
Simple image processing is implemented using OpenCV to convert the camera stream to grayscale.

### 3. Database Operations
Complete CRUD operations are available through both the API and frontend interface.

### 4. Data Persistence
Docker volumes are used to persist the SQLite database across container restarts.

## 🛠️ Technologies Used

- **Backend**: Django, Django REST framework, OpenCV
- **Frontend**: React, Axios, React Router, Bootstrap
- **Database**: SQLite
- **Containerization**: Docker, Docker Compose
- **Web Server**: Nginx (in production mode)

## ⚠️ Important Notes

1. **Camera Access**: Ensure your user or Docker has permission to access the camera device (/dev/video0).
2. **Security**: This is a demonstration setup. For production, implement proper security measures like HTTPS, restricted CORS, etc.
3. **Port Forwarding**: The setup demonstrates port-forwarding by exposing container services to external machines.

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
