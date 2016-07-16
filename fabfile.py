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
def test(only='unit integration functional', env='local_env'):
    if 'unit' in only:
        run_unit_tests(env=env)
    if 'integration' in only or 'functional' in only:
        # need to pass only down to sh -> docker as command -> fab into docker to decide whether to run ft or int
        local('./docker_tests/run_docker_tests.sh {}'.format(only))


@task
def docker_tests(only='integration functional', env='local_env'):
    if 'integration' in only:
        integration(env=env)
    if 'functional' in only:
        ft(env=env)


@task
def docker_ft(env='local_env'):
    ft(env=env)


@task
def docker_integration(env='local_env'):
    integration(env=env)


@activate_env
def ft(env='local_env'):
    print 'Running functional tests..'
    print local('python -m unittest discover -s ./docker_tests/functional')


@activate_env
def integration(env='local_env'):
    print 'Running integration tests..'
    print local('python -m unittest discover -s ./docker_tests/integration')


@activate_env
def run_unit_tests(env='local_env'):
    print 'Running unit tests..'
    print local('python -m unittest discover -s ./tests/unit')
