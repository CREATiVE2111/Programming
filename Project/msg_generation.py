import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from platform import python_version
import random as rd

goods = ['Пылесос Samsung X2100W', 'Монитор MSI Display 27165IG', ' Ноутбук Huawei MateMook 17716', 'Наушники SONY ClearAudioX24']
price = [15500, 29999, 89000, 22000]

server = 'smtp.mail.ru'
user = 'udachainyou@mail.ru'
password = 'UHpsdBsQ1hN0mwiGQ9S0'
recipients = ['udachainyou@mail.ru']
sender = 'udachainyou@mail.ru'
subject = 'Магазинчик Электроники'
# html =  f"<html>" \
#             f"<head>" \
#             f"</head>" \
#             f"<body>" \
#                 f"<p>Здравствуйте, Алексей Василев</p>" \
#                 f"<p>Вы приобрели: {goods[ch]}</p>" \
#                 f"<p>Стоимость: {price[ch]} рублей</p>" \
#                 f"</body" \
#         f"</html>"
c = 0
count = int(input())
for i in range(count):
    c += 1
    ch = rd.randint(0, len(goods) - 1)
    rd.choice(["приобрели", "продали"])
    html2 = "<html> <head> <style> " \
            ".status {color: black}" \
            ".price {color: red;font-weight: bold;}" \
            ".product {color: black;border-bottom: 1px dashed red;} " \
            "</style> </head>" + f'<body>' \
                    f'<p>Здравствуйте, Алексей Василев</p>' \
                    f'<p>Вы <span class="status">{rd.choice(["приобрели", "продали"])}</span>: <span class="product">{goods[ch]}</span></p>' \
                    f'<p>Стоимость: <span class="price">{price[ch]}</span></p>' \
                    f'</body>' \
                    f'</html>'
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = 'Python script <' + sender + '>'
    msg['To'] = ', '.join(recipients)
    msg['Reply-To'] = sender
    msg['Return-Path'] = sender
    msg['X-Mailer'] = 'Python/' + (python_version())

    part_text = MIMEText(html2, 'plain')
    part_html = MIMEText(html2, 'html')

    msg.attach(part_text)
    msg.attach(part_html)

    mail = smtplib.SMTP_SSL(server)
    mail.login(user, password)
    mail.sendmail(sender, recipients, msg.as_string())
    mail.quit()
    print(f"Sent successfully. Count: {c}")