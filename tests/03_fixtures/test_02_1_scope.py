import pytest


@pytest.fixture(scope='function') # default scope
def func_scope():
    print("function scope setup")
    yield
    print("function scope teardown")


@pytest.fixture(scope='module')
def mod_scope():
    print("Module scope")
    yield
    print("Module teardown")


