import pytest
from selenium import webdriver

@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="failed_test",
                      attachment_type=AttachmentType.PNG)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching chrome browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching firerox browser")
    else:
        driver = webdriver.Chrome()
    return driver


def pytest_addoption(parser):  # this will get the value from the CLI
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # this will return the browser value to setup method
    return request.config.getoption("--browser")

#######Pytest HTML Reports############
# def pytest_configure(config):
#     config._metadata['Project Name']='nop commerce'
#     config._metadata['Module Name'] = 'Customers'
#     config._metadata['Tester Name'] = 'Fasiuddin'
# # it a hook for delete/modify environment info to html report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME",None)
#     metadata.pop("Plugins",None)
