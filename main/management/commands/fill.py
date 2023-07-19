from django.core.management import BaseCommand

from main.models import Student


class Command(BaseCommand):


    def handle(self, *args, **options):
        # print('Hi, Sky!')
        student_list = [
            {'last_name': 'Ivanov', 'first_name': 'Ivan'},
            {'last_name': 'Petrov', 'first_name': 'Petr'},
            {'last_name': 'Sidorov', 'first_name': 'Alex'},
            {'last_name': 'Kozlov', 'first_name': 'Nikolay'}
        ]

        # Вариант 1 - построчно. Для каждой строчки commit, для большого кол-ва студентов долго
        # for student_item in student_list:
        #     Student.objects.create(**student_item)

        # Вариант 2 - пакeтное добавление (для большого кол-ва студентов)
        students_for_create = []
        for student_item in student_list:
            students_for_create.append(Student(**student_item))

        Student.objects.bulk_create(students_for_create)
