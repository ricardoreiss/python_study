from selenium import webdriver
import time
options = webdriver.ChromeOptions()
options.add_argument("--headless")
navegador = webdriver.Chrome(options=options)

for c in range(1):
    navegador = webdriver.Chrome()
    #Abrindo o Drive
    navegador.get('https://drive.google.com/drive/folders/1G1L71C6MA7Lu92WFT4_bzS9Dj2UN8Lb_')
    time.sleep(7)
    #Selecionando e Baixando os arquivos
    navegador.find_element_by_xpath('//*[@id="drive_main_page"]/div/div[2]/div/div/div[2]/div/div[2]/div/div[3]').click()
    arq = navegador.find_elements_by_class_name('uXB7xe')
    print(arq)
    arq = arq[int(len(arq)/2):]
    nomes = list()
    for n in range(len(arq)):
        n_pri = (arq[n].text)
        print(n_pri)

        arq_tipe = (n_pri.split('.'))[-1]
        if arq_tipe == 'xlsx':
            nomes.append(n_pri)
            arq[n].click()
            navegador.find_element_by_xpath('/html/body/div[8]/div[3]/div/div[3]/div[2]/div[2]/div[3]').click()

            time.sleep(4)














    """
    navegador.find_element_by_xpath('//*[@id=":2c"]/div/c-wiz/div[2]/c-wiz/div[1]/c-wiz/div/c-wiz/div[1]/c-wiz/c-wiz/div/c-wiz[1]/div/div/div/div[6]').click()

    arqui = navegador.find_elements_by_class_name('KL4NAf')
    n_arqui = int((len(arqui))/2)
    print(n_arqui)
    for c in range(n_arqui):
        print(arqui[c+n_arqui].text)
        att = navegador.find_element_by_xpath(f'//*[@id=":2c"]/div/c-wiz/div[2]/c-wiz/div[1]/c-wiz/div/c-wiz/div[1]/c-wiz/c-wiz/div/c-wiz[{c+1}]/div/div/div/div[6]').click()
        print(att)
"""


    """dowload_but = navegador.find_elements_by_class_name('akerZd')
    print(dowload_but)
    nomes = list()
    for c in range(len(arqui)):
        nome = arqui[c].text
        print(nome)
        arq_tipe = (nome.split('.'))[-1]
        if arq_tipe == 'xlsx':
            nomes.append(nome)
            dowload_but[c].click()
            time.sleep(4)

    print(nomes)
"""










    """navegador.find_element_by_xpath('//*[@id="drive_main_page"]/div/div[2]/div/div/div[2]/div/div[2]/div/div[3]').click()
    time.sleep(5)

    nomes_arq = navegador.find_elements_by_class_name('KL4NAf ')
    dowload = navegador.find_element_by_class_name('YM8blb M3pype')
    time.sleep(1)
    nomes = list()
    for df in range(len(nomes_arq)):
        nome = nomes_arq[df].text
        print(nome)
        arq_tipe = (nome.split('.'))[-1]
        if arq_tipe == 'xlsx':
            nomes.append(nome)
            print(dowload)
            dowload.click()
            time.sleep(8)"""

    """for nome_df in nomes_arq:
        nome = nome_df.text
        print(nome)
        arq_tipe = (nome.split('.'))[-1]
        if arq_tipe == 'xlsx':
            nomes.append(nome)
            time.sleep(2)
            nome_df.click()
            time.sleep(5)
            navegador.find_element_by_xpath('/html/body/div[8]/div[3]/div/div[3]/div[2]/div[2]/div[3]/div').click()
            time.sleep(5)
            navegador.find_element_by_xpath('/html/body/div[8]/div[3]/div/div[1]/div[1]').click()
            time.sleep(2)"""
    navegador.quit()
"""//*[@id=":2c"]/div/c-wiz/div[2]/c-wiz/div[1]/c-wiz/div/c-wiz/div[1]/c-wiz/c-wiz/div/c-wiz[1]/div/div/div/div[6]
//*[@id=":2c"]/div/c-wiz/div[2]/c-wiz/div[1]/c-wiz/div/c-wiz/div[1]/c-wiz/c-wiz/div/c-wiz[2]/div/div/div/div[6]
//*[@id=":2c"]/div/c-wiz/div[2]/c-wiz/div[1]/c-wiz/div/c-wiz/div[1]/c-wiz/c-wiz/div/c-wiz[3]/div/div/div/div[6]
//*[@id=":2c"]/div/c-wiz/div[2]/c-wiz/div[1]/c-wiz/div/c-wiz/div[1]/c-wiz/c-wiz/div/c-wiz[4]/div/div/div/div[6]
//*[@id=":2c"]/div/c-wiz/div[2]/c-wiz/div[1]/c-wiz/div/c-wiz/div[1]/c-wiz/c-wiz/div/c-wiz[5]/div/div/div/div[6]"""