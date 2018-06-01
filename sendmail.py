import smtplib
import datetime

date = datetime.datetime.now().strftime("%d/%m/%y-%H:%M")
folder_date = datetime.datetime.now().strftime("%d%m%y-%H%M")
gmail_sender = 'mrrikp.pi@gmail.com'
gmail_password = 'MyRaspb3rry'

server = smtplib.SMTP_SSL('smtp.gmail.com',465)
##server.ehlo()
##server.startttls()
server.login(gmail_sender, gmail_password)

to_addr ='rik.pettman@gmail.com'
mail_subject = 'Birdbox News - '+ date
mail_text = 'Hi \nYou have '+ "2" + " pictures and "+"3" + " videos. \nHere is a link http://www.python.org"
mail_body = '\r\n'.join(['To: %s' % to_addr,
                         'From: %s' % gmail_sender,
                         'Subject: %s' % mail_subject,
                         '', mail_text])
try:
    server.sendmail(gmail_sender, [to_addr], mail_body)
    print ('email sent')
except:
    print ('error sending mail')

server.quit()                      