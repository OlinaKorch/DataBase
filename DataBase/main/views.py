from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная страница', #передаем в шаблон какую-то надпись
        'values': ['Some', 'Hello', '123'], #передаем в шаблон список
        'obj': { #передаем в шаблон целый словарь
            'car': 'BMW',
            'age': 18,
            'hobby': 'FootBall'
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contact.html')
