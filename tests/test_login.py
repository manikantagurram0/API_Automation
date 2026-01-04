



def test_login_services(log_ser):
    session, response=log_ser.login()
    assert response.status_code ==200
    