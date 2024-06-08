import os

HOSTS = os.getenv('RENDER_EXTERNAL_HOSTNAME'), os.getenv('CLIENT_URL')
origins = ['http://localhost', 'http://localhost:8000']
[origins.append(host) for host in HOSTS if host is not None]
