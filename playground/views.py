from django.core.mail import EmailMessage, BadHeaderError
from django.shortcuts import render


def say_hello(request):
    try:
        message = EmailMessage('subject', 'message', 'andre@diaz.com', ['crhistian.diazb@alumno.buap.mx'])
        message.attach_file('playground/static/images/dog.jpg')
        message.send()
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Mosh'})
