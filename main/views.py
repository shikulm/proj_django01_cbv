from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from main.models import Student


# Create your views here.


class StudentListView(ListView):
    model = Student
    template_name = 'main/index.html'

# def index(request):
#     student_list = Student.objects.all()
#     # student_list = Student.objects.filter(is_active=True)
#     context = {
#         'object_list': student_list,
#         'title': "Главная"
#     }
#     return render(request, 'main/index.html', context)


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


class StudentDetailView(DetailView):
    model = Student
    template_name = 'main/student_detail.html'

# def view_student(request, pk):
#     student_item = get_object_or_404(Student, pk=pk)
#     context = {
#         'object': student_item
#     }
#     return render(request, 'main/student_detail.html', context)

# def index(request):
#     print(request.method)
#     if request.method == "POST":
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         print(f'{name} ({email} - {message}')
#     return render(request, 'main/index.html')
