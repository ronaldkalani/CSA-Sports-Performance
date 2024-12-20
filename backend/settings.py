import environ

# Initialize environment variables
env = environ.Env()

# Optional: Read from a .env file for local development
environ.Env.read_env()

# Database configuration
DATABASES = {
    'default': env.db(default='postgres://postgres:postgres@localhost:5432/sports_performance')
}

# Example: Debug and other settings using environ
DEBUG = env.bool('DEBUG', default=True)
SECRET_KEY = env('SECRET_KEY', default='your-default-secret-key')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['localhost'])
