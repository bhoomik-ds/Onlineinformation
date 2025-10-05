# 📢 Online Information Portal

A comprehensive Django web application for managing job postings, notifications, results, and contact information. Built with modern web technologies and deployed on Vercel with production-ready security features.

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/yourusername/online-information-portal)

## 🌟 Features

### 📋 Job Management System
- **Job Listings**: Create, edit, and manage job postings
- **Job Details**: Comprehensive job information with age limits, qualifications
- **Application Forms**: Direct application submission
- **Salary Information**: Transparent salary details

### 📢 Notification System
- **Important Announcements**: System-wide notifications
- **Job Alerts**: Automated notifications for new job postings
- **Status Updates**: Real-time updates on application status

### 📊 Results Management
- **Result Publication**: Publish and manage examination results
- **File Uploads**: Support for PDF result files
- **Result Search**: Easy result lookup functionality

### 📞 Contact System
- **Contact Forms**: User inquiry management
- **Admin Interface**: Streamlined contact management
- **Response Tracking**: Track and manage user communications

## 🛠️ Technology Stack

- **Backend**: Django 4.2.7
- **Database**: PostgreSQL (Production) / SQLite (Development)
- **Media Storage**: Cloudinary
- **Static Files**: WhiteNoise
- **Deployment**: Vercel
- **Version Control**: Git & GitHub

## Installation

### Development Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd online-information-portal
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create superuser:
```bash
python manage.py createsuperuser
```

6. Run development server:
```bash
python manage.py runserver
```

### 🚀 Production Deployment

Follow our comprehensive deployment guides:
- 📚 [GitHub Upload Guide](GITHUB_UPLOAD_GUIDE.md) - Step-by-step guide to upload your code to GitHub
- 🌟 [Vercel Deployment Guide](VERCEL_DEPLOYMENT_GUIDE.md) - Complete Vercel deployment walkthrough
- 🚀 [General Deployment Guide](DEPLOYMENT_GUIDE.md) - Security fixes and deployment overview

#### Quick Deployment Steps:

1. **Upload to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Production-ready Django app"
   git remote add origin https://github.com/yourusername/online-information-portal.git
   git push -u origin main
   ```

2. **Deploy to Vercel**:
   - Connect GitHub repository to Vercel
   - Set environment variables in Vercel dashboard
   - Deploy with one click

3. **Set up Database**:
   - Create PostgreSQL database (Neon/Railway/Supabase)
   - Add DATABASE_URL to Vercel environment variables

#### 🔒 Security Features (Already Configured):
- ✅ Strong SECRET_KEY generated
- ✅ DEBUG=False for production
- ✅ HTTPS/SSL security headers enabled
- ✅ ALLOWED_HOSTS properly configured
- ✅ CSRF and XSS protection enabled
- ✅ Secure cookie settings
- ✅ WhiteNoise for static files
- ✅ Cloudinary for media storage

## Configuration

### Environment Variables

- `SECRET_KEY`: Django secret key (required)
- `DEBUG`: Debug mode (False for production)
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- `DB_ENGINE`: Database engine (postgresql for production)
- `DB_NAME`: Database name
- `DB_USER`: Database user
- `DB_PASSWORD`: Database password
- `DB_HOST`: Database host
- `DB_PORT`: Database port

### Static & Media Files

- Static files are automatically collected to `staticfiles/` directory in production.
- Media files (images, PDFs) are stored on Cloudinary.

#### Cloudinary Setup

Option A: Single URL
```bash
export CLOUDINARY_URL=cloudinary://<api_key>:<api_secret>@<cloud_name>
```

Option B: Individual keys
```bash
export CLOUDINARY_CLOUD_NAME=your_cloud_name
export CLOUDINARY_API_KEY=your_api_key
export CLOUDINARY_API_SECRET=your_api_secret
```

No code changes required in models; existing `ImageField/FileField` will upload to Cloudinary after env is set.

## Project Structure

```
online-information-portal/
├── jobs/                 # Job-related functionality
├── results/              # Results functionality
├── notifications/        # Notifications functionality
├── contact/              # Contact form functionality
├── templates/            # Global templates
├── media/                # User uploaded files
├── staticfiles/          # Collected static files
├── online_information/   # Project settings
├── requirements.txt      # Python dependencies
├── Dockerfile           # Docker configuration
├── docker-compose.yml   # Docker Compose configuration
└── nginx.conf           # Nginx configuration
```

## Security Features

- CSRF protection enabled
- XSS protection enabled
- Content type sniffing protection
- Clickjacking protection
- HSTS headers (when using HTTPS)
- Secure cookie settings (when using HTTPS)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For support, please contact us through the contact form on the website.
