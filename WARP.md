# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

This is a Django-based Online Information Portal designed for managing job postings, notifications, results, and contact information. The application is configured for local development with SQLite database and local media storage, with optional Cloudinary integration.

## Architecture Overview

### Core Structure
- **Django 4.2.7** web framework with modular app architecture
- **Four main Django apps**: `jobs`, `results`, `notifications`, `contact`
- **Local development setup**: Configured for local development with SQLite database
- **Media storage**: Local media storage with optional Cloudinary integration
- **Static files**: Served by Django development server
- **Database**: SQLite for local development

### Key Models Architecture
- **Job model**: Comprehensive job posting with Cloudinary image fields, organization details, application dates, qualification requirements, and social media links
- **Result model**: Exam results with Cloudinary file storage
- **Notification model**: System notifications with ordering and timestamps
- **Contact model**: Contact form submissions
- **QuickLink/CallLetter/AdmitCard models**: Administrative link management

### URL Structure
- Root URL (`/`) serves the jobs app home page
- Single URL configuration in `online_information/urls.py` includes jobs URLs
- Health check endpoint at `/health/` for monitoring

## Development Commands

### Environment Setup
```powershell
# Create and activate virtual environment (Windows)
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Environment configuration
copy .env.example .env
# Edit .env with your configuration
```

### Database Operations
```powershell
# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Make migrations after model changes
python manage.py makemigrations
python manage.py migrate
```

### Development Server
```powershell
# Start development server
python manage.py runserver

# Alternative: Use the provided batch file
start_server.bat
```

### Testing and Quality
```powershell
# Run Django tests
python manage.py test

# Run specific app tests
python manage.py test jobs
python manage.py test results

# Django system check
python manage.py check

# Test project configuration (media, static files, database)
python test_project.py
```

### Project Testing
```powershell
# Test project configuration
python test_project.py

# Generate secure secret key (if needed)
python generate_secret_key.py
```

## Configuration Management

### Settings Architecture
- **Local Development**: Uses `settings.py` with DEBUG=True, SQLite database, local media storage
- **Smart Cloudinary Integration**: Automatically detects Cloudinary credentials and enables cloud storage when configured

### Environment Variables (.env file)
- `SECRET_KEY`: Django secret key (already set)
- `DEBUG`: Set to True for development
- `ALLOWED_HOSTS`: localhost,127.0.0.1 for local development
- Email configuration variables for SMTP functionality (optional)

### File Storage
The application uses local file storage for simplicity:
- **Image files**: Stored in `media/job_images/` directory
- **Result files**: Stored in `media/results/` directory
- **Automatic upload**: Files uploaded through admin interface are saved locally
- **Development friendly**: No external services or API keys required

## Local Development Features

### File Storage Strategy
- **Local storage**: All files stored in `media/` directory with organized subdirectories
- **No external dependencies**: No cloud services or API keys required
- **Simple development**: Upload files through Django admin, view them locally

### Database
- **SQLite**: Perfect for local development, no setup required
- **Automatic creation**: Database file created on first migration
- **Easy reset**: Simply delete `db.sqlite3` file to start fresh

## Development Patterns

### Model Conventions
- All models include proper `__str__` methods and Meta classes
- Cloudinary fields are used consistently for file uploads with folder organization
- Models use appropriate field types (CharField with max_length, TextField for long content)
- Ordering is specified in Meta classes for consistent data presentation

### View Architecture
- Views follow Django function-based pattern
- Home view aggregates data from multiple models for dashboard display
- Consistent use of `get_object_or_404` for detail views
- Template context includes all necessary data for views

### URL Configuration
- Clean, SEO-friendly URL patterns
- Consistent naming conventions for URL names
- Single root URL configuration including health checks

## File Organization Patterns

### Static Files
- App-specific static files in `jobs/static/`
- Production collection to `staticfiles/` directory
- WhiteNoise handles serving with compression and caching

### Templates
- Global templates in `templates/` directory
- App-specific templates in app directories using `APP_DIRS = True`

### Media Files
- Cloudinary integration for production file storage
- Local `media/` directory for development
- Automatic fallback between storage backends

## Testing and Validation

The project includes a comprehensive testing script:
- **Configuration validator**: `test_project.py` checks all project settings
- **Database validation**: Verifies SQLite database configuration
- **Media storage test**: Verifies local file storage is working
- **Static files check**: Ensures static files are properly configured
- **Clear feedback**: Provides detailed status and next steps

## Environment-Specific Considerations

### Windows Development
- Use `start_server.bat` for easy development server startup
- PowerShell commands are optimized for Windows environment
- Virtual environment activation uses Windows-specific scripts
- Media files stored in `media/` directory with proper permissions

### Project Structure
Clean local development setup:
- No deployment files or production configurations
- Simplified requirements.txt with only essential packages (Django, Pillow, python-decouple)
- Local SQLite database for easy development
- Local file storage with organized directory structure
- No external service dependencies
