import pytest
from SRC.Services.Login_services import Login_services
from SRC.Services.Dashboard_services import dashboard_service

@pytest.fixture
def log_ser():
    LOGSER=Login_services()
    return LOGSER

@pytest.fixture
def dashboard():
    log=Login_services()
    session,response= log.login()
    dash=dashboard_service()
    
    return dash,session
