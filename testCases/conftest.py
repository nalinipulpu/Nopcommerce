from datetime import datetime
from pathlib import Path
from Utilities.ReadProperties import ReadConf

import pytest
from selenium import webdriver
import pytest


# import pytest_xdist

def pytest_addoption(parser):
    parser.addoption('--browser')



@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')




@pytest.fixture()
def set_up(browser):
    brow = str(browser)

    if brow.lower() == 'google':
        driver = webdriver.Chrome()
        driver.get(ReadConf.get_BaseUrl())
        driver.maximize_window()
        return driver
    elif brow.lower() == 'firefox':
        driver = webdriver.Firefox()
        driver.get(ReadConf.get_BaseUrl())
        driver.maximize_window()
        return driver

    elif brow == 'ie':
        driver = webdriver.Ie
        driver.get(ReadConf.get_BaseUrl())
        driver.maximize_window()
        return driver

    else:
        driver = webdriver.Chrome()
        driver.get(ReadConf.get_BaseUrl())
        driver.maximize_window()

        return driver


# this is a hook for adding envirnment info to html reports
def pytest_configure(config):
    config._metadata['projectname'] = 'nop commerce'
    config._metadata['module name'] = 'Customers'
    config._metadata['Tester'] = 'Nalini'


# it is hook for delting/modifing enviornment info to html reports
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
    metadata.pop("Packages", None)
    metadata.pop("Python", None)
    metadata.pop("Platform", None)

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # set custom options only if none are provided from command line
    if not config.option.htmlpath:
        now = datetime.now()
        # create report target dir
        reports_dir = Path('Reports', now.strftime('%Y-%m-%d'))
        reports_dir.mkdir(parents=True, exist_ok=True)
        # custom report file
        report = reports_dir / f"report_{now.strftime('%H-%M')}.html"
        # adjust plugin options
        config.option.htmlpath = report
        config.option.self_contained_html = True

        # config._metadata['projectname'] = 'nop commerce'
        # config._metadata['module name'] = 'Customers'
        # config._metadata['Tester'] = 'Nalini'
