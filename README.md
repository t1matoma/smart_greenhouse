# Smart Greenhouse Prototype  
*A Django-based web application for managing greenhouse parameters*  

[![Django](https://img.shields.io/badge/Django-3.2-green)](https://www.djangoproject.com/) 

A prototype system for personalized smart greenhouse control, where each user manages their virtual greenhouse environment.  

---

##  Key Features  
- **User-specific greenhouses** with isolated settings.  
- **Modular control** for:  
  - Heating (`heating`)  
  - Lighting (`lighting`)  
  - Humidity (`steam_generator`)  
  - Sensors (`temp_n_humidity`)  
  - Ventilation (`ventilation`)  
  - Watering (`watering`)  
- **Persistent settings** saved to database.  
- **Auth system** (registration/login).  

---

##  Tech Stack
| Category       | Technologies                         |
|----------------|--------------------------------------|
| Backend        | Django 4.2+, Python 3.10+            |
| Frontend       | HTML5, CSS3                          |

## Quick Start with Docker


### Prerequisites
- Python 3.10+
- pip

### Installation
```bash
# 1. Clone repository
git clone https://github.com/t1matoma/smart_greenhouse.git
cd smart_greenhouse
```
###  Environment Configuration

The project uses environment variables for sensitive settings. 
**Never commit your `.env` file to version control!**

### Required `.env` variables:
```ini
# Django
SECRET_KEY=your-secret-key-here
```

To start the application with Docker, you can use the provided script `run.sh`, which will:

- Build the Docker image.
- Apply migrations.
- Collect static files.
- Start the server.

### Steps to run the server:

1. Ensure Docker and Docker Compose are installed on your machine.
2. Run the following command to start the application:

```bash
   ./run.sh
```

Now you can open the site in your browser at `http://127.0.0.1:8000/`.


### Creating a Superuser

```bash
docker-compose up -d
```

```bash
docker-compose exec django python portfolio/manage.py createsuperuser
```
### Access the Admin Panel

Once the server is running, you can access the Django admin panel at:

http://127.0.0.1:8000/admin/




##  Quick Setup without Docker

### Prerequisites
- Python 3.10+
- pip

### Installation
```bash
# 1. Clone repository
git clone https://github.com/t1matoma/smart_greenhouse
cd smart_greenhouse

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.\.venv\Scripts\activate   # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 5. Run migrations
python manage.py migrate

# 6. Create admin user
python manage.py createsuperuser

# 7. Run development server
python manage.py runserver
```
##  Environment Configuration

The project uses environment variables for sensitive settings. 
**Never commit your `.env` file to version control!**

### Required `.env` variables:
```ini
# Django
SECRET_KEY=your-secret-key-here
```
Now you can open the site in your browser at `http://127.0.0.1:8000/`.
