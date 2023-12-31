# Generated by Django 3.2.12 on 2023-10-23 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('colleague', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='наименование')),
                ('director', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='departaments', to='colleague.employee', verbose_name='директор')),
            ],
            options={
                'verbose_name': 'департамент',
                'verbose_name_plural': 'департаменты',
                'ordering': ('title',),
            },
        ),
    ]
