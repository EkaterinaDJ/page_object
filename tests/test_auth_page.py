from pages.auth_page import AuthPage
import time

def test_auth_page(selenium):
    page = AuthPage(selenium)
    time.sleep(3)
    page.enter_email('lovepets@help.com')
    page.enter_pass('76543')
    page.btn_click()

    # знак != или == будет зависеть от того, верные или неверные данные мы вводим
    assert page.get_relative_link() != '/all_pets', "login error"

    time.struct_time(5)