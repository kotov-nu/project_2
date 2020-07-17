from stepik_vacancies.vacancies.models import Company, Specialty, Vacancy
from stepik_vacancies.vacancies.data import jobs, companies, specialties
import datetime
from django.db import models
# В командной строке импорт без stepik_vacancies.


def create_companies():
    for c in companies:
        company = Company.objects.create(
            name=c['title'],
            location='Нет данных',
            logo='https://place-hold.it/100x60',
            description='Очень классная кампания',
            employee_count=50
        )
        company.save()


def create_specialties():
    for s in specialties:
        specialty = Specialty.objects.create(
            code=s['code'],
            title=s['title'],
            picture='https://place-hold.it/100x60'
        )
        specialty.save()


def import_vacancy_info():
    for job in jobs:
        vacancy = Vacancy.objects.create(
            title=job['title'],
            specialty=Specialty.objects.filter(code=job['cat']).first(),
            company=Company.objects.filter(name=job['company']).first(),
            skills=job['desc'],
            salary_min=int(job['salary_from']),
            salary_max=int(job['salary_to']),
            published_at=datetime.datetime.strptime(job['posted'], '%Y-%m-%d')
        )
        vacancy.save()
        print(job)
