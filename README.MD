# Sustainability Project



## Overview
The **Sustainability Project** is a full-stack web application that allows users to track and manage sustainability actions. The backend is built using **Django** and **Django REST Framework (DRF)**, while the frontend is built using **React.js**.

## Features
- User-friendly interface for tracking sustainability actions
- API-based backend with Django REST Framework
- CRUD operations for sustainability actions
- Integrated React frontend
- SQLite/PostgreSQL database support

---

## File Structure
```
sustainability_project/  # Django Backend Project
│── sustainability_project/  # Django project folder
│   │── __init__.py
│   │── settings.py  # Main settings file
│   │── urls.py  # Root URL configuration
│   │── wsgi.py
│   │── asgi.py
│
│── sustainability_app/  # Django App for Sustainability Actions
│   │── migrations/  # Database migrations
│   │── __init__.py
│   │── admin.py  # Admin panel settings
│   │── apps.py
│   │── models.py  # Defines the SustainabilityAction model
│   │── serializers.py  # DRF serializers
│   │── views.py  # API views
│   │── urls.py  # API URLs
│
│── db.sqlite3  # SQLite database (if using PostgreSQL, replace with settings)
│── manage.py  # Django management script
│
│── frontend/  # React Frontend
│   │── node_modules/
│   │── public/
│   │── src/
│   │   │── components/  # React components
│   │   │── api.js  # Axios API requests
│   │   │── App.js  # Main React component
│   │   │── index.js  # React entry point
│   │── assets/
│   │   │── green-earth.png  # Project logo/image
│   │── package.json
│   │── .env  # Store API URL here
│   │── .gitignore
│
│── requirements.txt  # Dependencies (Django, DRF, Axios, etc.)
```

---

## Setup & Installation
### Backend (Django)
1. **Clone the repository**
   ```sh
   git clone https://github.com/stealth/sustainability_project.git
   cd sustainability_project
   ```
2. **Create a virtual environment**
   ```sh
   python -m venv venv
   source venv/bin/activate  
   ```
3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Run migrations and start the server**
   ```sh
   python manage.py migrate
   python manage.py runserver
   ```

### Frontend (React)
1. **Navigate to frontend folder**
   ```sh
   cd frontend
   ```
2. **Install dependencies**
   ```sh
   npm install
   ```
3. **Start the development server**
   ```sh
   npm start
   ```

---

## API Endpoints
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | `/api/actions/` | Get all sustainability actions |
| POST | `/api/actions/` | Add a new action |
| PUT | `/api/actions/:id/` | Update an action |
| DELETE | `/api/actions/:id/` | Delete an action |

---

## Environment Variables
Create a `.env` file in the frontend directory and add:
```
REACT_APP_API_URL=http://127.0.0.1:8000/api/
```

---

## License
This project is licensed under the MIT License.

---


