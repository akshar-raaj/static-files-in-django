import multiprocessing

bind = '127.0.0.1:8001'
workers = multiprocessing.cpu_count() * 2 + 1
daemon = True
pidfile = 'gunicorn_process_id.txt'
django_settings = 'test_project.settings'
pythonpath = '.'
accesslog = 'gunicorn_access_log.txt'
errorlog = 'gunicorn_error_log.txt'
