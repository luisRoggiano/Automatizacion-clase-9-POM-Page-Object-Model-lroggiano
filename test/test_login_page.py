from page.login_page import LoginPage


def test_login( driver ):
    #crear objeto (instanciarlo)
    loginPage = LoginPage(driver) 
    loginPage.open()
    loginPage.login()