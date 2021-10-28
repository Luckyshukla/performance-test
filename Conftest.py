import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def driver_init_1(request):
    web_driver = webdriver.Chrome()
    request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.fixture(scope="class")
def driver_init_2(request):
    web_driver = webdriver.Firefox()
    request.cls.driver = web_driver
    yield
    web_driver.close()