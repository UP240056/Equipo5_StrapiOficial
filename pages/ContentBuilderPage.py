from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ContentBuilderPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def ir_a_content_builder(self):
        # Buscamos el enlace por su destino (href) en lugar del texto visible
        enlace_menu = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='content-type-builder']"))
        )
        self.driver.execute_script("arguments[0].click();", enlace_menu)

    def verificar_carga_exitosa(self):
        # Verificamos que navegó con éxito comprobando la URL, evitando problemas de idioma
        self.wait.until(EC.url_contains("content-type-builder"))
        return True