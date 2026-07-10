import pytest
from pages.LoginPage import LoginPage
from pages.ContentBuilderPage import ContentBuilderPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestStrapi:

    # ========================================================
    # PRUEBAS 1, 2 y 3: Data-driven para casos de error
    # ========================================================

    @pytest.mark.parametrize("email, password", [
        ("admin@falso.com", "mal123"),   # Credenciales incorrectas
        ("", "vacio"),                   # Email vacío
        ("sin_arroba", "123456")         # Formato inválido
    ])
    def test_login_invalido(self, driver, email, password):
        login_page = LoginPage(driver)
        login_page.login(email, password)
        
        # Como los datos están mal, validamos que el sistema no nos deje avanzar
        # y la URL siga conteniendo "login"
        assert "login" in driver.current_url

    # ========================================================
    # PRUEBA 4: Caso válido - Login exitoso
    # ========================================================

    def test_login_exitoso(self, driver):
        login_page = LoginPage(driver)
        
        login_page.login("joseluis.rangelz06@gmail.com", "JLRz131106") 
        
        # Validamos que entramos al dashboard (la URL ya no es de login)
        wait = WebDriverWait(driver, 10)
        wait.until_not(EC.url_contains("login"))
        assert "login" not in driver.current_url

    # ========================================================
    # PRUEBA 5: Navegación y uso del 2do Page Object
    # ========================================================

    def test_navegacion_content_builder(self, driver):
        login_page = LoginPage(driver)
        
        login_page.login("joseluis.rangelz06@gmail.com", "JLRz131106")
        
        # EL FIX: Esperamos a que el sistema salga de la pantalla de login ANTES de buscar el menú
        wait = WebDriverWait(driver, 10)
        wait.until_not(EC.url_contains("login"))
        
        # Una vez en el dashboard, instanciamos el POM y damos clic
        content_page = ContentBuilderPage(driver)
        content_page.ir_a_content_builder()
        
        # Verificamos que cargó bien
        assert content_page.verificar_carga_exitosa() is True