from django.urls import path
from .views import estate_list_by_category_view, main_page_view, workers_view, requisites_view, estate_detail_view

app_name = 'agency'
urlpatterns = [
    path('', main_page_view, name='index_url'),
    path('workers/', workers_view, name='workers_url'),
    path('requisites/', requisites_view, name='requisites_url'),
    path('catalog/', estate_list_by_category_view, name='catalog_url'),
    path('catalog/<int:pk>/', estate_detail_view, name='estate_detail_url'),
]
