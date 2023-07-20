from django.urls import path

from main.apps import MainConfig
# from main.views import index, contact, view_student, StudentListView
from main.views import contact, StudentListView, StudentDetailView

app_name = MainConfig.name

urlpatterns = [
    path('', StudentListView.as_view(), name='index'),
    path('contact/', contact, name='contact'),
    path('view/<int:pk>', StudentDetailView.as_view(), name='view_student'),
]

# urlpatterns = [
#     path('', StudentListView.as_view(), name='index'),
#     path('contact/', contact, name='contact'),
#     path('view/<int:pk>', view_student, name='view_student'),
# ]

# urlpatterns = [
#     path('', index, name='index'),
#     path('contact/', contact, name='contact'),
#     path('view/<int:pk>', view_student, name='view_student'),
# ]