# Video Chat Application - Deployment Guide

## Quick Start

### Local Development

1. **Clone and Setup**
```bash
git clone https://github.com/Suryansh913/videochat
cd videochat
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. **Configure Environment**
```bash
cp .env.example .env
# Edit .env with your local settings
```

3. **Database Setup**
```bash
python manage.py migrate
python manage.py createsuperuser  # Optional
```

4. **Run Development Server**
```bash
# Using Daphne (WebSocket support)
daphne -b 127.0.0.1 -p 8000 videochat.asgi:application

# Or using Django's development server
python manage.py runserver
```

### Render.com Deployment

1. **Prerequisites**
   - Render account (render.com)
   - GitHub repository connected to Render

2. **Automatic Deployment**
   - Push this code to your GitHub repository
   - Connect your repo to Render
   - Render will automatically use `render.yaml` configuration
   - Static files are automatically collected during build

3. **Manual Configuration (if not using render.yaml)**
   - Create PostgreSQL database
   - Create Redis instance
   - Set environment variables in Render dashboard
   - Deploy using the Procfile

4. **Environment Variables to Set in Render Dashboard**
   - `SECRET_KEY`: Generate a new Django secret key
   - `DEBUG`: Set to `false` for production
   - `ALLOWED_HOSTS`: Your Render domain (e.g., `yourdomain.onrender.com`)
   - `DATABASE_URL`: PostgreSQL connection string
   - `REDIS_URL`: Redis connection string
   - `CSRF_TRUSTED_ORIGINS`: Your domain with https

### Project Structure

```
videochat/
├── videochat/              # Project settings
│   ├── settings.py         # Django settings (STATIC_ROOT configured)
│   ├── asgi.py            # WebSocket & HTTP handling
│   ├── wsgi.py            # WSGI configuration
│   └── urls.py
├── video/                  # Video chat app
│   ├── consumers.py        # WebSocket consumers
│   ├── views.py
│   └── urls.py
├── manage.py
├── requirements.txt        # Python dependencies
├── Procfile               # Render/Heroku process file
├── render.yaml            # Render infrastructure config
├── .env.example           # Example environment variables
└── static/               # Static files (collected to staticfiles/)
```

### Key Components

- **Django 6.0.5**: Web framework
- **Django Channels 4.3.2**: WebSocket support
- **Daphne 4.2.1**: ASGI server
- **PostgreSQL**: Database
- **Redis**: Channel layer & caching
- **WhiteNoise**: Static file serving
- **Gunicorn**: WSGI server (optional)

### Important Configuration Notes

1. **Static Files**: 
   - `STATIC_ROOT` is set to `staticfiles/` directory
   - `collectstatic` runs during deployment
   - WhiteNoise handles serving in production

2. **WebSocket**:
   - Uses Redis for channel layer communication
   - Consumer class: `VideoChat` in `video/consumers.py`
   - WebSocket endpoint: `/ws/`

3. **Database**:
   - PostgreSQL required for production
   - Use PostgreSQL locally for development (recommended)
   - Run `python manage.py migrate` to create tables

4. **Security**:
   - Change `SECRET_KEY` in production
   - Set `DEBUG=False` in production
   - Update `ALLOWED_HOSTS` with your domain
   - Configure `CSRF_TRUSTED_ORIGINS`

### Troubleshooting

**Build Fails on collectstatic**
- Ensure `STATIC_ROOT` is configured ✓
- Ensure `STATICFILES_STORAGE` is set ✓
- Check static files don't have permission issues

**WebSocket Connection Issues**
- Verify Redis is running
- Check `REDIS_URL` configuration
- Ensure `CHANNEL_LAYERS` is properly configured

**Database Errors**
- Ensure PostgreSQL is running
- Check `DATABASE_URL` or individual DB settings
- Run `python manage.py migrate`

### Monitoring

Check deployment logs:
```bash
# For Render: View logs in dashboard
# For local: Monitor console output
```

## Support

- Django Docs: https://docs.djangoproject.com/
- Channels Docs: https://channels.readthedocs.io/
- Render Docs: https://render.com/docs/
