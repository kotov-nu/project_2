from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.views import View
from vacancies.models import Company, Specialty, Vacancy


class MainView(View):
    """ Главная. """

    def get(self, request):
        specialties = Specialty.objects.annotate(count=Count('vacancies'))
        companies = Company.objects.annotate(count=Count('vacancies'))
        return render(
            request, 'index.html', context={'specialties': specialties, 'companies': companies}
        )


class VacanciesView(View):
    """ Все вакансии. """

    def get(self, request):
        vacancies = Vacancy.objects.all()
        return render(
            request, 'vacancies.html', context={'vacancies': vacancies, 'category': 'Все вакансии'}
        )


class CategoriesView(View):
    """ Вакансии по категориям. """

    def get(self, request, category):
        vacancies = Vacancy.objects.filter(specialty__code=category)
        category = get_object_or_404(Specialty.objects.filter(code=category)).title
        return render(
            request, 'vacancies.html', context={'vacancies': vacancies, 'category': category}
        )


class CompaniesView(View):
    """ Вакансии по компаниям. """

    def get(self, request, company_pk):
        vacancies = Vacancy.objects.filter(company__pk=company_pk)
        company_name = get_object_or_404(Company.objects.filter(pk=company_pk)).name
        return render(
            request, 'company.html', context={'vacancies': vacancies, 'company_name': company_name, 'referer': request.META['HTTP_REFERER']}
        )


class VacancyView(View):
    """ Вакансия. """

    def get(self, request, vacancy_pk):
        vacancy = get_object_or_404(Vacancy.objects.filter(pk=vacancy_pk))
        return render(
            request, 'vacancy.html', context={'vacancy': vacancy, 'referer': request.META['HTTP_REFERER']}
        )
