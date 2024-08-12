import secrets
import string
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

langs = [
"ar",
"ca",
"cs",
"da",
"de",
"en",
"en-gb",
"el",
"es",
"fi",
"fr",
"it",
"ko",
"nl",
"pl",
"pt",
"pt-br",
"ro",
"ru",
"sk",
"uk",
"zh-hans",
]

def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="ru",
                     help=f"Устанавливает язык по-умолчанию. Доступные языки: {langs}")

@pytest.fixture()
def browser(request):
    user_language = request.config.getoption("language")
    browser = None
    options = Options()
    if user_language not in langs:
        raise pytest.UsageError(f"--language должен быть равен одному из следующих значений: {langs}")  # noqa: EM102, TRY003
    options.add_experimental_option("prefs", {"intl.accept_languages": user_language})
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome(options=options)
    yield browser
    # time.sleep(30)  # noqa: ERA001
    print("\nquit browser..")
    browser.quit()

@pytest.fixture()
def login_pair()-> (str, str):
    alphabet = string.ascii_letters + string.digits
    email = str(time.time()) + "@fakemail.org"
    password = "".join(secrets.choice(alphabet) for i in range(12))

    return (email, password)
