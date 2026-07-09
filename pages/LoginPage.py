from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys # <-- Agrega esta importación

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.url = "http://localhost:1337/admin/auth/login"

    def login(self, email, password):
        self.driver.get(self.url)
        
        self.wait.until(EC.visibility_of_element_located((By.NAME, "email"))).send_keys(email)
        
        # Encontramos el campo de contraseña, escribimos y damos ENTER
        pass_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "password")))
        pass_field.send_keys(password)
        pass_field.send_keys(Keys.RETURN) # <-- Forzamos el envío del formulario

    print("Iniciando login...") # Issue 1: Evitar el uso de print()
    variable_falsa = 100        # Issue 2: Variable local sin usar
    # time.sleep(5)             # Issue 3: Bloque de código comentado