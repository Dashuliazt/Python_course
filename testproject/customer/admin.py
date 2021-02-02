from django.contrib import admin
from .models import *

# отображение в админке всех столбцов в админке
class CustomersAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'second_name',
        'birthdate',
        'created_at',
        'updated_at',
        'salary',
        'profession'
    )
# поисковик
    search_fields = ('second_name',)
# добавление ссылок на имени
    list_display_links = ('id', 'first_name')
# редактирование полей
    list_editable = ('profession','salary',)
# фильтр по колонкам
    list_filter = ('profession','salary',)
    list_per_page = 2

class ProfessionsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'profession_name'
    )
    search_fields = ('profession_name',)
    list_display_links = ('id', 'profession_name')

# Register your models here.
admin.site.register(Customer, CustomersAdmin)
admin.site.register(Professions, ProfessionsAdmin)