from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.headless = True
navegador = webdriver.Chrome(options=chrome_options)

for c in range(1):
    #navegador = webdriver.Chrome()
    #Abrindo o Drive
    navegador.get('https://drive.google.com/drive/folders/1G1L71C6MA7Lu92WFT4_bzS9Dj2UN8Lb_')
    time.sleep(5)
    #Selecionando e Baixando os arquivos
    n_name = navegador.find_elements_by_class_name('bSmy5')
    navegador.find_element_by_class_name('bSmy5').click()
    nomes = list()
    for nome_df in range(len(n_name)):
        nome = navegador.find_element_by_xpath('/html/body/div[8]/div[3]/div/div[1]/div[3]/div[1]').text
        print(nome)
        arq_tipe = (nome.split('.'))[-1]
        if arq_tipe == 'xlsx':
            nomes.append(nome)
            navegador.find_element_by_xpath('/html/body/div[8]/div[3]/div/div[3]/div[2]/div[2]/div[3]').click()
            time.sleep(4)

        navegador.find_element_by_xpath('/html/body/div[8]/div[2]/div[2]').click()
    time.sleep(2)
    navegador.quit()

    #Analisando informações dos Arquivos do Drive
    import pandas as pd
    mes = list()
    prod = list()
    val = list()

    for ane in nomes:
        tabela = pd.read_excel(fr'C:\Users\secre\Downloads\{ane}')
        mes.append(tabela.columns[0])
        prod.append(tabela['Produtos'].count())
        val.append(tabela['Vendas'].sum())

    #Enviando Email
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders

    #Anexador de Arquivos
    def anexo(a):
        attchment = open(a, 'rb')

        att = MIMEBase('application', 'octet-stream')
        att.set_payload(attchment.read())
        encoders.encode_base64((att))

        txt = a.split('\\')

        att.add_header('Content-Disposition', f'attachment;filename={txt[-1]}')
        attchment.close()

        email_msg.attach(att)

    #Escolhento Remetente
    host='smtp.gmail.com'
    port='587'
    login='espd.equipe@gmail.com'
    senha='odair0106'

    server=smtplib.SMTP(host,port)

    server.ehlo()
    server.starttls()
    server.login(login,senha)

    #Email
    email_msg = MIMEMultipart()
    email_msg['From']=login

    #Destinatário
    email_msg['To']='ricardojac9.15@gmail.com'

    #Assunto
    email_msg['Subject'] = 'Relatório de '+', '.join(mes)+'.'

    #Corpo
    corpo =['Prezados, a seguir estão as informações sobre as vendas dos últimos meses.']
    for c in range(len(mes)):
        inf = f"""
    
        {mes[c]}:
        Quantidade de produtos oferecidos: {prod[c]}
        Total de retorno: R${val[c]:,.2f}"""

        corpo.append(inf)

    email_msg.attach(MIMEText(' '.join(corpo)))

    #Anexar Arquivos
    cam_arquivo=list()
    for c in nomes:
        arquivo=fr'C:\\Users\\secre\\Downloads\\{c}'
        cam_arquivo.append(arquivo)

    for a in cam_arquivo:
        anexo(a)

    #Envio
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())


