# -*- coding: utf-8 -*-
# @Date    : 2020/4/23 16:07
# Software : PyCharm
import smtplib
import requests
import email
import sys
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

USER = sys.argv[1]
PWD = sys.argv[2]
YOU = sys.argv[3]

def get_mes():
    url = 'http://open.iciba.com/dsapi/'
    r = requests.get(url)
    data = r.json()
    en_content = data.get('content')
    zh_content = data.get('note')
    message = zh_content + '\n' + en_content
    return message

msg = get_mes()
print(msg)

HOST = 'smtp.qq.com'
SUBJECT = '嘿！今天也是幸运的一天~'
FROM = USER
TO = YOU
message = MIMEMultipart('related')
message_html = MIMEText(f"{msg}", 'plain', 'utf-8')
message.attach(message_html)
message['From'] = FROM
message['To'] = TO
message['Subject'] = SUBJECT
email_client = smtplib.SMTP_SSL(HOST)
email_client.connect(HOST, '465')
result = email_client.login(FROM, PWD)
email_client.sendmail(from_addr=FROM, to_addrs=TO.split(','), msg=message.as_string())
email_client.close()
print("Done.")
