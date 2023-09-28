from multiprocessing import cpu_count


# Socket Path
bind = 'unix:/tmp/gunicorn_APP_NAME.sock'


# Worker Options
workers = cpu_count() * 5
worker_class = 'uvicorn_worker.UvicornWorker'


# Logging Options
loglevel = 'debug'
accesslog = 'APP_PWD/logs/gunicorn/access_log'
errorlog =  'APP_PWD/logs/gunicorn/error_log'


raw_env = [
    "DJANGO_DEBUG=False",
    "DJANGO_SECRET_KEY=TOKEN"
]
