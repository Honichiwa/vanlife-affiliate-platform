# Vanlife Affiliate Platform

## 🚐 About the Project

The **Vanlife Affiliate Platform** is a Django-based web application that helps users find and share van-related products through an affiliate system, allowing users to explore and recommend gear for the vanlife community.

## 🛠️ Tech Stack

- **Backend**: Django, Django
- **Database**: PostgreSQL / SQLite (depending on environment)
- **Frontend**: Django templates

## 🌟 Features

- User authentication (signup, login, logout)
- User CRUD operations for their van/rv setups
- Search and filter vanlife-related products
- Store and manage affiliate links
- Admin dashboard for product management

## 🚀 Getting Started

### Clone the repository

```sh
 git clone https://github.com/Honichiwa/vanlife-affiliate-platform.git
 cd vanlife-affiliate-platform
```

### Set up a virtual environment

```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### Install dependencies

```sh
pip install -r requirements.txt
```

### Create and update local_settings.py file
Create `local_settings.py` file in `weather_app/weather_app` next to django `settings.py`

Make django secret key:
```sh
django-admin shell
```
```sh
from django.core.management.utils import get_random_secret_key  
get_random_secret_key()
```
Copy generated secret key to `local_settings.py`:
```python
SECRET_KEY = "(your_generated_random_secret_key)"
```

### Apply database migrations

```sh
python manage.py migrate
```

### Creating an admin user

```sh
python manage.py createsuperuser
```
With this user you can login to the app with or even http://localhost:8000/admin

### Run the development server

```sh
python manage.py runserver
```

Visit [localhost:8000](http://localhost:8000) to see the app in action.


## 🤝 Contributing

Pull requests are welcome! Please open an issue first to discuss any major changes.

