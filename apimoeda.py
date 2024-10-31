from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

moeda = input('Deseja solicitar a cotação de qual moeda ?')

edge_driver_path = r"C:\path\to\msedgedriver.exe"  # Altere para o caminho correto

# Inicializa o WebDriver
navegador = webdriver.Edge()

navegador.get("https://www.google.com")
time.sleep(3)

criou = False;
try:
    # Aguarda até que o campo de pesquisa esteja presente
    pesquisa = WebDriverWait(navegador, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="APjFqb"]'))  # Substitua conforme necessário
    )
    
    # Preenche o campo de pesquisa
    pesquisa.send_keys('valor do '+ moeda)
    pesquisa.send_keys(Keys.RETURN)  # Envia a pesquisa
    time.sleep(5)

    resultado = 0
    pegaElementoValor = WebDriverWait(navegador, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]'))        
    )
    resultado = pegaElementoValor.get_attribute("data-value")

    time.sleep(4)
        
    pasta = r"C:\Users\faava\OneDrive\Área de Trabalho\Devv's" 
    arquivo = "CotaMoedas.txt"    

    os.makedirs(pasta, exist_ok=True)
    caminho_arquivo = os.path.join(pasta, arquivo)

    criou = True;
except Exception as e:
    criou = False;
    print(f"Ocorreu um erro: {e}")
finally:
    navegador.close()

if criou == True :
    data_hoje = datetime.now()
    data_string = data_hoje.strftime("%Y-%m-%d %H:%M:%S")
    with open(caminho_arquivo, 'w') as file:
            file.write('A moeda :'+ moeda +' fechou o dia na data de '+data_string+' valendo: '+ resultado +'\n')
            file.write('______________________________________________________________________')