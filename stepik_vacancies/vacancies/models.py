from django.db import models


class Company(models.Model):
    """ Компания. """

    name = models.TextField('Название', max_length=30, unique=True, blank=True)
    location = models.TextField('Расположение', max_length=50, blank=True)
    logo = models.TextField('Логотип', blank=True)
    description = models.TextField('Описание компании', blank=True)
    employee_count = models.PositiveIntegerField('Количество сотрудников', default=0)


class Specialty(models.Model):
    """ Специализация. """

    code = models.TextField('Код специализации', max_length=50, unique=True)
    title = models.TextField('Название специализации', max_length=50, unique=True)
    picture = models.TextField('Логотип', blank=True)


class Vacancy(models.Model):
    """ Вакансия. """

    title = models.TextField('Название', max_length=100)
    specialty = models.ForeignKey(Specialty, verbose_name='Специализация', on_delete=models.CASCADE, related_name="vacancies")
    company = models.ForeignKey(Company, verbose_name='Компания', on_delete=models.CASCADE, related_name="vacancies")
    skills = models.TextField('Навыки', max_length=1000, blank=True)
    description = models.TextField('Требования', max_length=10000, blank=True)
    salary_min = models.PositiveIntegerField('Зарплата от', null=True)
    salary_max = models.PositiveIntegerField('Зарплата до', null=True)
    published_at = models.DateField()
