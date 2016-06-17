from functools import wraps

from fabric.api import local
from fabric.api import task
from fabric.context_managers import prefix
from os.path import exists


@task
def setup_env(env='local_env'):
    create_virtual_environment(env)
    install_dependencies(env=env)

    print '-----------------------------------------\n\n' \
          'Virtual environment created at ./{0}\n' \
          'To activate use ". {0}/bin/activate"'.format(env)


def create_virtual_environment(env):
    print '--- Creating virtual environment at ./{}'.format(env)
    local('virtualenv {}'.format(env))


def activate_env(fn):
    @wraps(fn)
    def with_env_activated(*args, **kwargs):
        # print(args, kwargs)
        env = kwargs['env']
        if not exists(env):
            setup_env(env)
        with prefix('. {}/bin/activate'.format(env)):
            return fn(env)

    return with_env_activated


@activate_env
def install_dependencies(env):
    print('--- Installing dependencies from requirements.txt in {}'.format(env))
    local('pip install -r requirements.txt')


@task
def test(only='unit,functional', env='local_env'):
    if 'unit' in only:
        run_unit_tests(env=env)
    if 'functional' in only:
        local('./ft/run_fts.sh')


@task
def docker_ft(env='local_env'):
    ft(env=env)


@activate_env
def ft(env='local_env'):
    print local('python -m unittest discover -s ./ft/add_account')


@activate_env
def run_unit_tests(env='local_env'):
    print 'Running unit tests..'
    print local('python -m unittest discover -s ./tests/unit')
