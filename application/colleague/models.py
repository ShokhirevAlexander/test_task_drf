from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Employee(models.Model):
    """ Модель сотрудников """
    surname = models.CharField(max_length=20, verbose_name='фамилия')
    name = models.CharField(max_length=20, verbose_name='имя')
    patronymic = models.CharField(max_length=20, verbose_name='отчество')
    photo = models.ImageField(upload_to='photo_employee', verbose_name='фото', blank=True)
    post = models.CharField(max_length=20, verbose_name='должность')
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='оклад')
    age = models.PositiveIntegerField(validators=[
        MaxValueValidator(60),
        MinValueValidator(20)
    ], verbose_name='возраст')
    departament = models.ForeignKey('division.Departament', on_delete=models.CASCADE, related_name='employees',
                                    verbose_name='департамент')

    class Meta:
        verbose_name = 'сотрудники'
        verbose_name_plural = 'сотрудник'
        ordering = ('surname', 'name', )

    def full_name(self) -> str:
        return f'{self.surname} {self.name} {self.patronymic}'

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'
