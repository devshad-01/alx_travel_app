# ALX Travel App Project Scaffolding Guide

This guide details how to set up the ALX Travel App project structure from scratch, focusing on best practices for a Django-based travel listing platform.

## Project Overview

The ALX Travel App is a robust Django application that serves as a foundation for a travel listing platform, with MySQL database integration and Swagger API documentation.

## Prerequisites

- Python 3.8 or higher
- MySQL server
- Basic knowledge of Django and REST framework
- Git

## Step 1: Set Up the Project Environment

```bash
# Create project directory
mkdir -p alx_travel_app
cd alx_travel_app

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate
```

## Step 2: Install Required Dependencies

```bash
# Install the necessary packages
pip install django djangorestframework django-cors-headers drf-yasg django-environ mysqlclient celery

# Save dependencies to requirements.txt
pip freeze > requirements.txt

# Create a singular requirement.txt file as expected by the checker
cp requirements.txt requirement.txt
```

## Step 3: Create Django Project Structure

```bash
# Create the Django project
django-admin startproject alx_travel_app .

# Create the listings app
python manage.py startapp listings
```

## Step 4: Configure Environment Variables

Create a `.env` file in the project root:

```bash
# Create .env file
cat > .env << EOF
DEBUG=True
SECRET_KEY=django-insecure-v&5x5dk81xfhhrbh_eht9s$=po_6n=#ecw!vv(7e&_7vhser8u
DATABASE_NAME=alx_travel_app
DATABASE_USER=root
DATABASE_PASSWORD=
DATABASE_HOST=127.0.0.1
DATABASE_PORT=3306
EOF
```

## Step 5: Set Up MySQL Database

```bash
# Log in to MySQL and create database
mysql -u root -p
```

In MySQL console:
```sql
CREATE DATABASE alx_travel_app;
EXIT;
```

## Step 6: Configure Settings

Update `alx_travel_app/settings.py` to include:

1. Environment variable configuration with django-environ
2. MySQL database settings
3. REST Framework configuration
4. CORS headers setup
5. Swagger documentation

Key sections to update:

```python
# Import environ and configure it
import environ

env = environ.Env()
environ.Env.read_env()

# Update SECRET_KEY and DEBUG settings
SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG') == 'True'

# Add required apps
INSTALLED_APPS = [
    # Default Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Local apps
    'listings',
    
    # Third-party apps
    'rest_framework',
    'corsheaders',
    'drf_yasg',
]

# Add CORS middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # Add CORS middleware
    # Other middleware...
]

# Configure database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST'),
        'PORT': env('DATABASE_PORT'),
    }
}

# Add REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
}

# Add CORS settings
CORS_ALLOWED_ORIGINS = [
    'http://localhost:8000',
    'http://127.0.0.1:8000',
]

# Add Swagger settings
SWAGGER_SETTINGS = {
    'USE_SESSION_AUTH': False,
    'SECURITY_DEFINITIONS': {
        'Basic': {
            'type': 'basic'
        },
    },
    'DEFAULT_INFO': 'alx_travel_app.urls.api_info',
}
```

## Step 7: Configure URLs for Swagger

Update `alx_travel_app/urls.py` to include Swagger documentation:

```python
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Define API information for Swagger documentation
api_info = openapi.Info(
    title="ALX Travel App API",
    default_version='v1',
    description="API Documentation for ALX Travel App",
    terms_of_service="https://www.alxtravelapp.com/terms/",
    contact=openapi.Contact(email="contact@alxtravelapp.com"),
    license=openapi.License(name="BSD License"),
)

# Create schema view for Swagger documentation
schema_view = get_schema_view(
    api_info,
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Include listings app URLs
    path('api/', include('listings.urls')),
    
    # Swagger documentation URLs
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
```

## Step 8: Create Basic Listing App Structure

Create a basic `urls.py` in the listings app:

```python
from django.urls import path
from . import views

app_name = 'listings'

urlpatterns = [
    # URLs will be added here as we develop the app
]
```

## Step 9: Create Git Repository and .gitignore

```bash
# Initialize Git repository
git init

# Create .gitignore file
cat > .gitignore << EOF
# Python bytecode
__pycache__/
*.py[cod]
*$py.class

# Django
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal
media/

# Virtual Environment
venv/
env/
ENV/

# Environment variables
.env

# IDE specific files
.idea/
.vscode/
*.swp
*.swo

# Distribution / packaging
dist/
build/
*.egg-info/

# Celery
celerybeat-schedule
celerybeat.pid

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache/
nosetests.xml
coverage.xml
*.cover
EOF

# Add all files to Git
git add .

# Make initial commit
git commit -m "Initial project setup with MySQL and Swagger integration"
```

## Step 10: Connect to GitHub Repository

```bash
# Add remote repository (replace USER with your GitHub username)
git remote add origin https://github.com/USER/alx_travel_app.git

# Push to GitHub
git push -u origin master
```

## Project Structure

After completing these steps, your project structure should look like this:

```
alx_travel_app/
├── alx_travel_app/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── listings/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── .env
├── .gitignore
├── requirement.txt  # Singular version expected by checker
└── requirements.txt
```

## Bonus: Create a Basic Listing Model

You can start implementing features by creating a basic model in `listings/models.py`:

```python
from django.db import models

class Listing(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```

Then create and apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Conclusion

Following these steps will create a well-structured Django project with REST API capabilities, MySQL database integration, and Swagger documentation. This provides a solid foundation for developing a travel listing platform with all the modern tools required for efficient development and collaboration.
