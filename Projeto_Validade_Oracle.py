#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import pyautogui
import time
import tkinter as tk
from tkinter import simpledialog

# Inicializar o navegador Chrome
driver = webdriver.Chrome()# Abrir o URL
url = "url do oracle da sua empresa"
driver.get(url)



if __name__ == "__main__":
    # Criar a janela para entrada de informações
    root = tk.Tk()
    root.withdraw()  # Ocultar a janela principal

    # Solicitar nomes de fornecedores usando uma caixa de diálogo
    user_input = simpledialog.askstring("Entrada", "Digite os nomes dos fornecedores separados por vírgula:")
    
    janela_x = 100
    janela_y = 200
    
    time.sleep(12)


    if user_input:
        names = user_input.split(',')

    
    time.sleep(2)

    # Procura STONE ISupplier - Cadastro de Fornecedores
    element = driver.find_element(By.XPATH, '/html/body/div[3]/form/span[2]/div[3]/div/div[1]/div/div[3]/div[1]/div[2]/table[2]/tbody/tr/td/div/table/tbody/tr/td[1]/table/tbody/tr/td/div/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/ul/li[2]/a/div[2]')

    # Clicar em STONE ISupplier - Cadastro de Fornecedores
    element.click()

    time.sleep(2)

    # Procura Supply Base
    element = driver.find_element(By.XPATH, '/html/body/div[3]/form/span[2]/div[3]/div/div[1]/div/div[3]/div[1]/div[2]/table[2]/tbody/tr/td/div/table/tbody/tr/td[1]/table/tbody/tr/td/div/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/ul/li[2]/ul/li/a/div[2]')

    # Clicar em Supply Base
    element.click()

    time.sleep(6)

    # Iterar sobre cada nome digitado
    for name in names:
        # Procura Fornecedores
        element = driver.find_element(By.XPATH, '/html/body/div[3]/form/span[2]/div[3]/div/div[1]/div/div[3]/div[1]/div[2]/table[2]/tbody/tr/td/div/table/tbody/tr/td[1]/table/tbody/tr/td/div/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/ul/li[2]/ul/li/ul/li[1]/a/div[2]')

        # Clicar em Fornecedores
        element.click()

        time.sleep(10)
    
        # Procura Nome do Fornecedor
        element = driver.find_element(By.XPATH, '/html/body/div[3]/form/span[2]/div[3]/div/div[1]/div/div[3]/table[2]/tbody/tr/td[1]/div[1]/div[2]/table/tbody/tr[4]/td/table/tbody/tr/td/div/div[3]/table/tbody/tr/td[2]/table/tbody/tr[1]/td[3]/input')

        # Clicar em Nome do Fornecedor
        element.click()

        time.sleep(4)
    
        # Preencher o nome
        pyautogui.typewrite(name)

        time.sleep(2)

        # Simular pressionar "Enter"
        pyautogui.press('enter')

        time.sleep(8)

        # Procura Data de inativação
        element = driver.find_element(By.XPATH, '/html/body/div[3]/form/span[2]/div[3]/div/div[1]/table/tbody/tr[2]/td/div[1]/div[2]/table[2]/tbody/tr/td[2]/table/tbody/tr[5]/td[3]/div/input')

        # Clicar em Data de inativação
        element.click()
        
        time.sleep(2)
    
        # Limpar Data de inativação

        element.clear()
        
        time.sleep(2)

        # Procura Botão Salvar
        element = driver.find_element(By.XPATH, '/html/body/div[3]/form/span[2]/div[3]/div/div[1]/table/tbody/tr[2]/td/div[1]/div[1]/table/tbody/tr/td[2]/table/tbody/tr/td[3]/button/span')

        # Clicar em Salvar
        element.click()

        time.sleep(2)

        # Clicar em Home
        element = driver.find_element(By.XPATH, '/html/body/div[3]/form/span[2]/table[1]/tbody/tr[1]/td/table/tbody/tr[1]/td[3]/table/tbody/tr/td[2]/a/div/img')

        # Clicar no elemento
        element.click()
    
        time.sleep(4)

