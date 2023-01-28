import pytest


@pytest.fixture()  # Действия до запуска
def set_up():
    print(" Enter to the system successful")
    yield
    print(" Exit from system")


@pytest.fixture(scope="function")  # Действия до запуска
def some():
    print(" Start")
    yield
    print(" End")