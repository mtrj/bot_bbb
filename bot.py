# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()  
chrome_options.add_argument("--headless") 

class bbb:
    def __init__(self, path, un, pw):
        """
        Path = path do webdriver
        un = Username
        pw = Password
        """
        self.path = path
        self.un = un
        self.pw = pw
        self.driver = webdriver.Chrome(self.path, options=chrome_options)
        
    def _login(self):
        """
        Os XPaths utilizados são específicos da votação da Manu 31/3/20
        """
        driver = self.driver
        driver.implicitly_wait(10)
        link_login = 'https://minhaconta.globo.com'
        driver.get(link_login)
        un, pw = self.un, self.pw
        x_un = '/html/body/div[1]/main/div[2]/div/div/div/div[2]/div[1]/form/div[1]/input'
        x_pw = '/html/body/div[1]/main/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/input'
        x_final = '/html/body/div[1]/main/div[2]/div/div/div/div[2]/div[1]/form/div[6]/button'
        un_input = driver.find_element_by_xpath(x_un).send_keys(un)
        pw_input = driver.find_element_by_xpath(x_pw).send_keys(pw)
        final_click = driver.find_element_by_xpath(x_final).click()
            
    def _vote(self, votos=10):
        self._login()
        driver = self.driver
        link_votacao = 'https://gshow.globo.com/realities/bbb/bbb20/votacao/paredao-bbb20-quem-voce-quer-eliminar-felipe-manu-ou-mari-a9f49f90-84e2-4c12-a9af-b262e2dd5be4.ghtml'
        driver.get(link_votacao)
        for i in range(1,votos):
            print('{0}/{1} voto em andamento'.format(i, votos))
            driver.find_element_by_xpath('/html/body/div[2]/div[4]/div/div[1]/div[4]/div[2]/div/div[1]').click()
            driver.implicitly_wait(15)
            try:
                driver.find_elements_by_xpath('//*[@id="roulette-root"]/div/div[1]/div[4]/div[2]/div[2]/div/div/div[2]/div/div[2]/img')[0].click()
            except IndexError:
                driver.get(link_votacao)
                driver.find_element_by_xpath('/html/body/div[2]/div[4]/div/div[1]/div[4]/div[2]/div/div[1]').click()
            driver.implicitly_wait(15)
            x_loop = '/html/body/div[2]/div[4]/div/div[3]/div/div/div[1]/div[2]/button'
            votou=False
            while votou==False:
                time.sleep(5)
                try:
                    driver.find_elements_by_xpath(x_loop).click()
                    votou = True
                    break                  
                except:
                    try:
                        driver.find_elements_by_xpath('//*[@id="roulette-root"]/div/div[1]/div[4]/div[2]/div[2]/div/div/div[2]/div/div[2]/img')[0].click()
                    except IndexError: 
                        driver.get(link_votacao)
                        votou=True
                        break 
                    time.sleep(10)
                    driver.implicitly_wait(15)
                    continue
            print('{0}/{1} voto concluído'.format(i, votos))
