from celery import Celery

celery_app = Celery(
    'tasks',
    broker='amqp://guest:guest@localhost:5672//',
    backend='rpc://'
)
celery_app.conf.update(
    result_expires=3600,
)

