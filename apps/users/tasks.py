from celery import shared_task
from django.core.mail import send_mail
from django.utils.html import strip_tags

from root.settings import EMAIL_HOST_USER


@shared_task
def send_verification_to_email(email: str, code):
    subject = 'Код подтверждения'
    html_message = f"""
    <html>
    <body>
        <div style="text-align: center;">   
            <img src="https://i.hh.uz/logos/svg/hh.ru__min_.svg?v=11032019" alt="logo" style="margin-top: 20px;">
            <p style="font-size: 18px;">{code} — ваш код для авторизации на <a href="https://hh.ru">hh.ru</a>.</p>
            <footer style="margin-top: 40px;">
                <a href="">Поиск вакансий | </a><a href="">Создать резюме</a>
                <p>© Группа компаний nimadir 2024</p>
            </footer>
        </div>
    </body>
    </html>
    """
    plain_message = strip_tags(html_message)
    send_mail(subject, plain_message, EMAIL_HOST_USER, [email], html_message=html_message)
    return {'Result': True, 'email': email}
