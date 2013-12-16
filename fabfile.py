import time

from fabric.api import run, env, cd
from fabric.colors import green
from fabric.context_managers import prefix


env.hosts = ['pythoninternals.com']
env.user = 'ubuntu'
env.activate = 'source ../bin/activate'


def pull():
    print(green("Pulling code"))
    run('git pull')
    print(green("Pulled"))


def install_requirements():
    print(green("Installing requirements"))
    run('pip install -r requirements.txt')
    print(green("Installed requirements"))


def collect_static_files():
    print(green("Collecting static files"))
    run('python manage.py collectstatic')
    print(green("Collected static files"))


def kill_running_gunicorn_process():
    print(green("Killing gunicorn process"))
    run('kill -9 `cat gunicorn_process_id.txt`', pty=False)
    print(green("Killed gunicorn process"))


def start_gunicorn_process():
    print(green("Starting gunicorn process"))
    result = run('gunicorn test_project.wsgi:application -c gunicorn_cfg.py', pty=False)
    print(green(str(result.return_code)))
    print(green("Started gunicorn process"))


def deploy():
    code_dir = '~/staticvirt/test_project'
    with cd(code_dir):
        with prefix(env.activate):
            pull()
            install_requirements()
            collect_static_files()
            kill_running_gunicorn_process()
            time.sleep(10)
            start_gunicorn_process()
