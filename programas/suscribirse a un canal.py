from selenium import webdriver

# Crea una instancia del navegador Chrome
driver = webdriver.Chrome()

# Navega a la página deseada
driver.get('https://www.youtube.com/channel/UCfdBtc12Lz7p68a_nHUgBIQ')

# Busca el botón por su etiqueta y hace clic en él
button = driver.find_element_by_tag_name("yt-spec-touch-feedback-shape__fill")
button.click()

# Cierra el navegador
driver.quit()
