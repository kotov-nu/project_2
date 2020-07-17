from django.contrib import admin
from django.urls import path
from vacancies.views import MainView, VacanciesView, CategoriesView, CompaniesView, VacancyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='index'),
    path('vacancies', VacanciesView.as_view(), name='vacancies'),
    path('vacancies/cat/<str:category>/', CategoriesView.as_view(), name='categories'),
    path('companies/<int:company_pk>/', CompaniesView.as_view(), name='companies'),
    path('vacancies/<int:vacancy_pk>/', VacancyView.as_view(), name='vacancy'),
]
