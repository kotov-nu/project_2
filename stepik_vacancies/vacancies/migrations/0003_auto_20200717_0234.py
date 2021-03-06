# Generated by Django 3.0.4 on 2020-07-16 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0002_vacancy_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание компании'),
        ),
        migrations.AlterField(
            model_name='company',
            name='employee_count',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество сотрудников'),
        ),
        migrations.AlterField(
            model_name='company',
            name='location',
            field=models.TextField(blank=True, max_length=50, verbose_name='Расположение'),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.TextField(blank=True, verbose_name='Логотип'),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.TextField(blank=True, max_length=30, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='code',
            field=models.TextField(max_length=50, unique=True, verbose_name='Код специализации'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='picture',
            field=models.TextField(blank=True, verbose_name='Логотип'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='title',
            field=models.TextField(max_length=50, unique=True, verbose_name='Название специализации'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='vacancies.Company', verbose_name='Компания'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='description',
            field=models.TextField(blank=True, max_length=10000, verbose_name='Требования'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='salary_max',
            field=models.PositiveIntegerField(null=True, verbose_name='Зарплата до'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='salary_min',
            field=models.PositiveIntegerField(null=True, verbose_name='Зарплата от'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='skills',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Навыки'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='specialty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='vacancies.Specialty', verbose_name='Специализация'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='title',
            field=models.TextField(max_length=100, verbose_name='Название'),
        ),
    ]
