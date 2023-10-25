from django.db import models
from colleague.models import Employee


class Departament(models.Model):
    """ Модель депортаментов """
    title = models.CharField(max_length=50, verbose_name='наименование', unique=True)
    director = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        related_name='departaments',
        verbose_name='директор',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'департамент'
        verbose_name_plural = 'департаменты'
        ordering = ('title',)

    def __str__(self):
        return self.title
