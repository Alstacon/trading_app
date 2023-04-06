import smtplib
from email.message import EmailMessage

from celery import Celery

from config import SMTP_USER, SMTP_PASSWORD

SMTP_HOST = 'smtp.gmail.com'
SMTP_PORT = 465
celery = Celery('tasks', broker='redis://localhost:6379')


def get_email_template_fashboard(name: str):
    email = EmailMessage()
    email['Subjects'] = 'Отчет Дашборд'
    email['From'] = SMTP_USER
    email['To'] = SMTP_USER

    email.set_content(
        '<div>'
        f'''<h1 style='color: black;'>Здравствуйте, {name} 🙋🏼‍♀️! Это Ваш отчет.</h1>'''
        '<img src="https://brobank.ru/wp-content/uploads/2021/09/otchet-brokera—1.jpg" width="600">'
        '</div>',
        subtype='html'
    )
    return email


@celery.task
def send_email_report_dashboard(name: str):
    email = get_email_template_fashboard(name)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(email)
