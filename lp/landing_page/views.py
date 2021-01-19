import re
import sys

import requests
import smtplib as smtp




from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseForbidden


def send_email(email, password, dest_email, subject, email_text):
    message = 'From: {}\r\nTo: {}\r\nSubject: {}\r\n\r\n{}'.format(email,
                                                           dest_email,
                                                           subject,
                                                           email_text)
    server = smtp.SMTP_SSL('smtp.yandex.com')
    server.set_debuglevel(1)
    server.ehlo(email)
    server.login(email, password)
    #server.login('batcharvrn@yandex.ru', 'Piramida2')
    server.auth_plain()
    server.sendmail(email, email, message)
    server.quit()


def is_valid_email(email):
    return re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email) is not None

def index_page(request):
    return render(request, "landing_page/index.html")

def telegram_bot_send_message(bot_message):
    #bot_token, bot_chatid  = '1133525584:AAHFkMFb3ohIaOvTdPanWlg5dd-LeQYJUIs', '242451984'
    user_ids = ['242451984', '300500129']


    for chat_id in user_ids:
        bot_token ='1133525584:AAHFkMFb3ohIaOvTdPanWlg5dd-LeQYJUIs'
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + bot_message
        response = requests.get(send_text)
        print('bot_response', response.json(), file=sys.stderr)

    return response.json()


def mail(request):
    name    = request.GET['name']
    plan    = request.GET['plan']
    email   = request.GET['email']
    message = request.GET['message']

    if len(name) and len(email) and len(message) and is_valid_email(email):
        m  = 'UserName: {}\r\n'.format(name)
        m += 'Plan: {}\r\n'.format(plan)
        m += 'Email: {}\r\n'.format(email)
        m += 'Text: \r\n{}\r\n'.format(message)
        #send_email('batcharvrn@yandex.ru', 'Piramida2', email, 'Dataset',  m)
        
        telegram_bot_send_message("New message!\nPlan: {} \nUser: {}\nFrom: {}\nText: {}".format(plan, name, email, message))
        
        send_email('info@alphamattingdata.com', 'Piramida2', email, 'Dataset: {} [{}]'.format(name, email),  m)
        return HttpResponse("ok")
    else:
        return HttpResponseForbidden()


# fromaddr = "otkogo@gmail.com"
# toaddr = "komu@mail.ru"
# mypass = "password"

# msg = MIMEMultipart()
# msg['From'] = fromaddr
# msg['To'] = toaddr
# msg['Subject'] = "Привет от питона"

# body = "Это пробное сообщение"
# msg.attach(MIMEText(body, 'plain'))

# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls()
# server.login(fromaddr, mypass)
# text = msg.as_string()
# server.sendmail(fromaddr, toaddr, text)
# server.quit()
