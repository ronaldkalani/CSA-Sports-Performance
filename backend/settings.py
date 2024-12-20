import environ

# Initialize environment variables
env = environ.Env()

# Read from a .env file (optional for local development)
environ.Env.read_env(BASE_DIR / '.env')

# Security settings
DEBUG = env.bool('DEBUG', default=False)
SECRET_KEY = env('SECRET_KEY', default='your-default-secret-key')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['localhost'])
# Static files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
DATABASES = {
    'default': env.db(
        default='postgres://postgres:postgres@localhost:5432/sports_performance'
    )
}

