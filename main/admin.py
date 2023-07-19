from django.contrib import admin

from main.models import Student

# Register your models here.
# Вывод списка
# admin.site.register(Student)

# Вывод структурированного списка
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'is_active')
    # Вывод отфильтрованного списка
    list_filter = ('is_active', )
    # Поиск по списку
    search_fields = ('first_name', 'last_name')

