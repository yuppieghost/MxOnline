from users.models import EmailVerifyRecord
from random import Random
from django.core.mail import send_mail
from MxOnline.settings import EMAIL_HOST_USER


def random_str(randomlength=8):
    str = ''
    chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    if send_type == 'update_email':
        code = random_str(4)
    else:
        code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ''
    email_body = ''

    if send_type == 'register':
        email_title = '在线注册激活链接'
        email_body = '请点击链接激活账号:http://www.wjj0315.top/active/{}'.format(code)

        send_status = send_mail(email_title, email_body, EMAIL_HOST_USER, [email])
        if send_status:
            pass

    elif send_type == 'forget':
        email_title = '密码重置链接'
        email_body = '请点击链接重置密码:http://www.wjj0315.top/reset/{}'.format(code)
        send_status = send_mail(email_title, email_body, EMAIL_HOST_USER, [email])
        if send_status:
            pass
    elif send_type == 'update_email':
        email_title = '邮箱修改验证码'
        email_body = '您的邮箱验证码为{}'.format(code)
        send_status = send_mail(email_title, email_body, EMAIL_HOST_USER, [email])
        if send_status:
            pass