from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

def open_browser():
    # Inicialización del navegador
    browser = webdriver.Firefox(options=Options())

    # Abrir una página (opcional)
    browser.get("https://www.example.com")  # Puedes cambiar la URL si lo deseas

    # Mantener el navegador abierto
    input("Presiona Enter para cerrar el navegador...")

    # Cerrar el navegador
    browser.quit()

if __name__ == "__main__":
    open_browser()
