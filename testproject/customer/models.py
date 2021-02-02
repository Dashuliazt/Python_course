from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=25, verbose_name='Имя')
    second_name = models.CharField(max_length=30, verbose_name='Фамилия')
    birthdate = models.DateField(verbose_name='Дата рождения')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрация')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    salary = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Размер зарплаты')
    profession = models.ForeignKey('Professions', on_delete=models.PROTECT, verbose_name='Профессия')


    def __str__(self):
        return f'{self.first_name} {self.second_name}'
# Переименование имени в админке и в шапке таблицы в админке
    class Meta:
        verbose_name_plural = 'Клиенты'
        verbose_name = 'Клиент'
# сортировка по дате обновления
        ordering = ('updated_at',)

class Professions(models.Model):
    profession_name = models.CharField(max_length=30, verbose_name='Наименование профессии')


    def __str__(self):
        return f'{self.profession_name}'


    class Meta:
        verbose_name_plural = 'Профессии'
        verbose_name = 'Профессия'