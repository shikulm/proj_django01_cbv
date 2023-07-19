from django.shortcuts import render

from main.models import Student


# Create your views here.


def index(request):
    student_list = Student.objects.all()
    # student_list = Student.objects.filter(is_active=True)
    context = {
        'object_list': student_list,
        'title': "Главная"
    }
    return render(request, 'main/index.html', context)


def contact(request):
    print(request.method)
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email} - {message}')

    context = {
        'title': 'Контакты'
    }

    return render(request, 'main/contact.html', context)

# def index(request):
#     print(request.method)
#     if request.method == "POST":
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         print(f'{name} ({email} - {message}')
#     return render(request, 'main/index.html')
