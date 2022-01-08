import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose lang")
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")



@pytest.fixture(scope="function")
def browser(request):
    lang = request.config.getoption("--language")
    browser_name = request.config.getoption("--browser_name")
    browser = None
    if browser_name == "firefox":
        print("\nstart firefox browser for test..")
        profile = webdriver.FirefoxProfile()
        profile.set_preference('intl.accept_languages', lang)
        browser = webdriver.Firefox(executable_path=r'C:\\geckodriver\\geckodriver.exe',firefox_profile=profile)
    else:
        print("\nstart chrome browser for test..")
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': lang})
        browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
