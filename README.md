# cars-API

## Overview

The Cars API is a Django-based application designed to manage car listings. It provides functionalities for creating, reading, updating, and deleting car records. This API allows users to interact with car data through a RESTful interface and a web interface.

## Features

- **CRUD Operations**: Create, Read, Update, and Delete car records.
- **User Authentication**: Manage users and associate car records with users.
- **API Endpoints**: Access car data through RESTful API endpoints.
- **Web Interface**: View and manage cars through a web interface.

## Installation

### Prerequisites

- Python 3.8 or higher
- Django 5.0.7 or higher
- Django REST framework (for API functionality)
- PostgreSQL (or other supported databases)

### Setup

1. **Clone the Repository**

   ```bash
   git clone git@github.com:Raghadkatout08/cars-API.git


2. **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate   # On Windows use `.venv\Scripts\activate`

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt

4. **Apply migrations:**
    ```bash
    python manage.py migrate
    
5. **Create a superuser:**
    ```bash
    python manage.py createsuperuser

6. **Run the server:**
    ```bash
    python manage.py runserver

### Running Tests
To run the tests, execute:
    ```python manage.py test```