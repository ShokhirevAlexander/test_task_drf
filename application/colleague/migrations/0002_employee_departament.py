# Generated by Django 3.2.12 on 2023-10-23 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('colleague', '0001_initial'),
        ('division', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='departament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='division.departament', verbose_name='департамент'),
        ),
    ]
