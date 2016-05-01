from fabric.api import local
from fabric.context_managers import prefix


def setup_env(name='local_env'):
    print '--- Creating virtual environment at ./{}'.format(name)
    local('virtualenv {}'.format(name))

    with prefix('. {}/bin/activate'.format(name)):
        print '--- Virtual environment created, installing dependencies from requirements.txt'
        local('pip install -r requirements.txt')

    print '-----------------------------------------\n\n' \
          'Virtual environment created at ./{0}\n' \
          'To activate use ". {0}/bin/activate"'.format(name)


def unit_test(args=''):
    local('python -m unittest discover {}'.format(args))
