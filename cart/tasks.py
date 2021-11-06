from celery import task
from django.core.mail import EmailMessage, send_mail
from order.models import Order

from django.template.loader import render_to_string
from django.conf import settings
from io import BytesIO
import weasyprint


@task
def order_created(order_id):
    print('fdjuvnbfjvnfvjfnjnjvnjn PIIIIIIIIIIIIIIIIIIIIIIIII', order_id)
    try:
        order = Order.objects.get(id=order_id)
        subject = f'Order N°. {order.id}'
        message = f'Chére {order.first_name}, \n\n' f'Votre Commande a été creer avec succées. \n' f'Votre Commande ID est: {order.id}.'
        mail_sent = EmailMessage(
            subject,
            message,
            'octopus.emailing@gmail.com' ,
            [order.email, 'dzoctopus@gmail.com']
        )
        print('email,', order.email)
        html = render_to_string('order_pdf.html' , {'order' : order})
        out = BytesIO()
        # stylesheets = [weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css' )]
        weasyprint.HTML(string=html).write_pdf(out)
        # attach PDF file
        mail_sent.attach(f'order_{order.id}.pdf' ,
        out.getvalue(),
        'application/pdf'
        )
        mail_sent.send()
    except:
        print('donenenneneeneenene')


# @task
# def order_created(order_id):
#     print('fdjuvnbfjvnfvjfnjnjvnjn PIIIIIIIIIIIIIIIIIIIIIIIII', order_id)
#     try:
#         send_mail(
#             'Example subject here',
#             'Here is the message body.',
#             'octopus.emailing@gmail.com',
#             ['inter.taki@gmail.com']
#         )
#         print('DOONE')
#     except:
#         print('lemail na pas ete envyer')