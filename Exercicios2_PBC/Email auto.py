
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
def anexo(a):
    attchment = open(a, 'rb')

    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64((att))

    txt = a.split('\\')

    att.add_header('Content-Disposition', f'attachment;filename={txt[-1]}')
    attchment.close()

    email_msg.attach(att)

host='smtp.gmail.com'
port='587'
login='espd.equipe@gmail.com'
senha='odair0106'

server=smtplib.SMTP(host,port)

server.ehlo()
server.starttls()
server.login(login,senha)

corpo = '<p>Agora vai!!!</p>'

email_msg = MIMEMultipart()
email_msg['From']=login
email_msg['To']='ricardojac9.15@gmail.com'
email_msg['Subject'] = 'Email AUTO'
email_msg.attach(MIMEText(corpo,'html'))

cam_arquivo=[r'C:\\Users\\secre\\Downloads\\Nomes perifericos farda.xlsx',
             r'C:\\Users\\secre\\Downloads\\ITENS EMBLEMAS PARA COMPRA DESBRAVADOR TOTAL.xlsx']

for a in cam_arquivo:
    anexo(a)

server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())

server.quit()