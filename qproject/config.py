import os
import requests

MAILGUN_API_BASE_URL = os.getenv('MAILGUN_API_BASE_URL', '')
MAILGUN_API_KEY = os.getenv('MAILGUN_API_KEY', '')
MAILGUN_DOMAIN = os.getenv('MAILGUN_DOMAIN', '')

AMQP_USERNAME = os.getenv('AMQP_USERNAME', 'guest')
AMQP_PASSWORD = os.getenv('AMQP_PASSWORD', 'guest')
AMQP_HOST = os.getenv('AMQP_HOST', 'localhost')
AMQP_PORT = int(os.getenv('AMQP_PORT', '5672'))
AMQP_VHOST = os.getenv('AMQP_VHOST', '/')

CELERY_BROKER_URL = 'amqp://{}:{}@{}:{}/{}'.format(AMQP_USERNAME, AMQP_PASSWORD, AMQP_HOST, AMQP_PORT, AMQP_VHOST)

CELERY_RESULT_BACKEND = 'rpc://'
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_ENABLE_UTC = True

ip = requests.get('https://api.ipify.org/?format=json').json()['ip']
ALLOWED_HOSTS = [ip]
