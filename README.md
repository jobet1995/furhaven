# 🐾 PawNest - Pet Adoption Platform

[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)

PawNest is a modern web application that connects pets in need of homes with loving families. Our platform makes the pet adoption process easier, safer, and more transparent for both shelters and adopters.

## ✨ Features

- 🐕 Browse available pets with detailed profiles
- 🏠 Connect with shelters and foster homes
- 🔍 Advanced search and filtering options
- 📱 Responsive design for all devices
- 🔒 Secure user authentication
- 📝 Application management system
- 📸 Image galleries for pets
- 📱 Mobile-friendly interface

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- PostgreSQL 13+
- Docker (optional)
- Poetry (for dependency management)

### Local Development

1. **Clone the repository**

```bash
git clone https://github.com/jobet1995/furhaven.git
cd furhaven
```
2. **Set up Python environment**

```bash
# Install Poetry if you haven't already
curl -sSL https://install.python-poetry.org | python3 -

# Install dependencies
poetry install --with=dev

# Activate the virtual environment
poetry shell
```

3. **Set up environment variables**
{{ ... }}
```bash
cp .env.example .env
# Edit .env with your configuration
```

4. **Set up the database**

```bash
python manage.py migrate
python manage.py createsuperuser
```

5. **Run the development server**

```bash
python manage.py runserver
```

### Docker Development

1. **Build and start the containers**

```bash
docker-compose up --build
```

2. **Run migrations**

```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

3. **Access the application**

   - Frontend: http://localhost:8000
   - Admin: http://localhost:8000/admin/

## 🛠️ Project Structure

```ini
paw_nest/
├── .github/              # GitHub Actions workflows
├── config/               # Project configuration
│   ├── settings/         # Django settings
│   ├── urls.py          # Main URL configuration
│   └── wsgi.py          # WSGI configuration
├── apps/                 # Django apps
│   ├── accounts/        # User accounts and authentication
│   ├── adoptions/       # Pet adoption logic
│   └── core/            # Core functionality
├── static/              # Static files (CSS, JavaScript, images)
├── templates/           # HTML templates
├── tests/               # Test files
├── .env.example         # Example environment variables
├── .gitignore           # Git ignore file
├── docker-compose.yml   # Docker Compose configuration
├── Dockerfile           # Docker configuration
├── manage.py            # Django management script
├── pyproject.toml       # Project dependencies and configuration
└── README.md            # This file
```

## 🧪 Testing

Run tests using pytest:

```bash
pytest
```

With coverage report:

```bash
pytest --cov=.
```

## 🔒 Environment Variables

Create a `.env` file in the project root with the following variables:

```env
# Django
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DB_NAME=paw_nest
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432

# Email (for production)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-email-password
DEFAULT_FROM_EMAIL=your-email@gmail.com
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Bootstrap 5](https://getbootstrap.com/)
- [Font Awesome](https://fontawesome.com/)
- [Poetry](https://python-poetry.org/)

---

Made with ❤️ by [Jobet P. Casquejo](mailto:jobetcasquejo221@gmail.com)
