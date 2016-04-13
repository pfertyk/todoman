import pytest
from click.testing import CliRunner


@pytest.fixture
def config(tmpdir):
    path = tmpdir.join('config')
    tmpdir.mkdir('default')  # default calendar
    path.write('[main]\n'
               'path = {}/*\n'
               'date_format = %Y-%m-%d\n'
               .format(str(tmpdir)))
    return path


@pytest.fixture
def runner(config):
    return CliRunner(env={
        'TODOMAN_CONFIG': str(config)
    })


@pytest.fixture
def generate():
    def inner(content):
        return (
            'BEGIN:VCALENDAR\n'
            'BEGIN:VTODO\n' +
            content +
            'END:VTODO\n'
            'END:VCALENDAR'
        )
    return inner


@pytest.fixture
def create(tmpdir, generate):
    def inner(name, content):
        tmpdir.join('default').join(name).write(generate(content))

    return inner


@pytest.fixture
def compare(tmpdir, generate):
    """
    Checks that file `name` contains the expected content, `content`.
    """
    def inner(name, content):
        actual = tmpdir.join('default').join(name).read()
        return actual == generate(content) + "\n"
    return inner
