from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import time, requests
from modules.utils import get_site, get_token
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get(get_site())
etapa = driver.find_element(By.ID, 'EtapaEnsinoPesquisa')
etapa.click()
for i in range(7):
	etapa.send_keys(Keys.ARROW_DOWN)
etapa.send_keys(Keys.ENTER)
buttonok = driver.find_element(By.ID, 'btnModalOk')
buttonok.click()
municipio = driver.find_element(By.ID, 'MunicipioPesquisa')
for i in range(6):
	municipio.send_keys('r')
municipio.send_keys(Keys.ENTER)
bairro = driver.find_element(By.ID, 'BairroPesquisa')
for i in range(4):
	bairro.send_keys('l')
bairro.send_keys(Keys.ENTER)
bairro.send_keys(Keys.ENTER)
#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "TurnoManha"))).click()
#driver.find_element(By.XPATH("//label[contains(text(),'Manhã')]")).click()
bairro.send_keys(Keys.TAB, Keys.TAB, Keys.TAB, Keys.SPACE)

time.sleep(2)
pesquisar = driver.find_element(By.ID, 'ListaEscola')
pesquisar.click()
time.sleep(1)
#nome_escola = ', '.join([my_elem.tag_name for my_elem in driver.find_elements(By.CLASS_NAME, "lstGrid_dados")])
#turno = driver.find_element(By.XPATH, "//*[contains(text(), 'REGULAR - ENSINO MÉDIO - MANHÃ')]")

token = get_token()
def sendMessage(token, channel_id, message):
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
    data ={"content": message}
    header = {"authorization": token}    
    r = requests.post(url, data=data, headers=header)


def funcToName():
	#nome_escola = driver.find_element(By.XPATH, "//*[contains(text(), 'CE ANDRE MAUROIS')]")
	try:
		escola_nome = driver.find_element(By.XPATH, "//*[contains(text(), 'CE ANDRE MAUROIS')]").is_displayed()		
		print('Tem escola')
		sendMessage(f"{token}", 857302713233833987, "Tem escola porra! @Andrew.#4525")
		return 0
	except:
		print('Não tem escola')
		sendMessage(f"{token}", 857302713233833987, "Não tem escola porra! @Andrew.#4525")
		pesquisar.click()
		time.sleep(1440)
	return 1


while funcToName != 1:
	funcToName()
	if funcToName == 0:
		pass
