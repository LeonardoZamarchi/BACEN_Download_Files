from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def busca_cooperados_coop(chrome):
    time.sleep(3)
    chrome.get('https://www.bcb.gov.br/estabilidadefinanceira/cooperados_cooperativa')
    html = chrome.find_element('xpath','html')    
    for n in range(1,7):
        for i in range(1,12):
            time.sleep(1)
            arquivo = chrome.find_element('xpath','/html/body/app-root/app-root/main/dynamic-comp/div/div/div[2]/div[2]/bcb-download-filter/div/div[2]/table/tbody/tr['+str(i)+']/td[2]/div/a')
            while True:
                try:
                    arquivo.click()
                    break
                except:
                    html.send_keys(Keys.DOWN)
        while True:
            try:
                prox = chrome.find_element('xpath','/html/body/app-root/app-root/main/dynamic-comp/div/div/div[2]/div[2]/bcb-download-filter/div/div[2]/div/pagination/ul/li[10]/a')
                prox.click()  
                html.send_keys(Keys.PAGE_UP)
                break
            except:
                html.send_keys(Keys.DOWN)


def busca_cooperados_municipio(chrome):
    time.sleep(3)
    chrome.get('https://www.bcb.gov.br/estabilidadefinanceira/cooperados_municipio')
    html = chrome.find_element('xpath','html')
    
    for n in range(1,7):
        for i in range(1,12):
            time.sleep(1)
            arquivo = chrome.find_element('xpath','/html/body/app-root/app-root/main/dynamic-comp/div/div/div[2]/div[2]/bcb-download-filter/div/div[2]/table/tbody/tr['+str(i)+']/td[2]/div/a')
            while True:
                try:
                    arquivo.click()
                    break
                except:
                    html.send_keys(Keys.DOWN)
        while True:
            try:
                prox = chrome.find_element('xpath','/html/body/app-root/app-root/main/dynamic-comp/div/div/div[2]/div[2]/bcb-download-filter/div/div[2]/div/pagination/ul/li[10]/a')
                prox.click()  
                html.send_keys(Keys.PAGE_UP)
                break
            except:
                html.send_keys(Keys.DOWN)


def balancetes_bcb(chrome):
    time.sleep(3)
    chrome.get('https://www4.bcb.gov.br/fis/cosif/balancetes.asp?frame=1')
    html = chrome.find_element('xpath','html')
    for i in range(1,184):
        time.sleep(1)
        select = chrome.find_element('xpath','/html/body/div/table[1]/tbody/tr[3]/td[2]/form/select')
        select.click()
        item = chrome.find_element('xpath','/html/body/div/table[1]/tbody/tr[3]/td[2]/form/select/option['+str(i)+']')
        item.click()
        download = chrome.find_element('xpath','/html/body/div/table[1]/tbody/tr[3]/td[3]/input')
        download.click()
        time.sleep(1)


def estatistica_munic(chrome):
    chrome.maximize_window()
    chrome.get('https://www.bcb.gov.br/estatisticas/estatisticabancariamunicipios/fis/cosif/cont/estban/municipio')
    html = chrome.find_element('xpath','html')
    time.sleep(1)
    cookie = chrome.find_element('xpath','/html/body/app-root/bcb-cookies/div/div/div/div/button[2]')
    cookie.click()
    for i in range(1,184):
        select = chrome.find_element('xpath','/html/body/div/table/tbody/tr/td[1]/div/form/select')
        select.click()
        while True:
            try:    
                item = chrome.find_element('xpath','/html/body/div/table/tbody/tr/td[1]/div/form/select/option['+str(i)+']')
                item.click()
                break
            except:
                time.sleep(1)

        while True:
            try:
                download = chrome.find_element('xpath','/html/body/div/table/tbody/tr/td[1]/div/form/input')
                download.click()
                break
            except:
                time.sleep(1)
        

def if_data(chrome):
    chrome.maximize_window()
    chrome.get('https://www3.bcb.gov.br/ifdata/')
    html = chrome.find_element('xpath','html')
    ''
    for i in range(1,35):
        btn_data  = chrome.find_element('xpath','/html/body/form/div[2]/div[2]/div/div[1]/button[2]')
        btn_data.click()
        while True:
            try:
                btn_data_op = chrome.find_element('xpath','/html/body/form/div[2]/div[2]/div/div[1]/ul/li['+str(i)+']/a')
                btn_data_op.click()
                break
            except:
                time.sleep(1)
        bnt_inst = chrome.find_element('xpath','/html/body/form/div[2]/div[2]/div/div[2]/button[1]')
        bnt_inst.click()
        cong_fin = chrome.find_element('xpath','/html/body/form/div[2]/div[2]/div/div[2]/ul/li[2]/a')
        cong_fin.click()
        btn_relat = chrome.find_element('xpath','/html/body/form/div[2]/div[2]/div/div[3]/button[1]')
        btn_relat.click()
        resumo = chrome.find_element('xpath','/html/body/form/div[2]/div[2]/div/div[3]/ul/li[1]/a')
        resumo.click()
        
        while True:
            try:
                download = chrome.find_element('xpath','/html/body/form/div[6]/a[2]')
                download.click()
                break
            except:
                time.sleep(1)
