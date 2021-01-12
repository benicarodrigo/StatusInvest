from bs4 import BeautifulSoup as bs
from selenium import webdriver



base_url = 'https://google.com.br'
url_site = f'{base_url}/indices/lista_reclamacoes/?id=902$status=ALL'
path = 'C:/Users/RodrigoCoelhoBenicá/PycharmProjects/selenium_beautfulsoup/chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get(base_url)
bs_obj = bs(driver.page_source, 'html.parser')

bar = driver.find_element_by_name('q')
btn_pesq = driver.find_element_by_name('btnK')
bar.send_keys('Live de python')
btn_pesq.click()
print('processo terminado')