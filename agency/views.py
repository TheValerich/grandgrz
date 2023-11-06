from django.shortcuts import render
from .models import Estate, Workers, Requisites
from django.views.decorators.cache import cache_page


def main_page_view(request):
    best_offer = Estate.objects.filter(best_offer=True)
    return render(request, 'index.html', {'best_offer': best_offer})


def workers_view(request):
    workers = Workers.objects.all().order_by('id')
    return render(request, 'workers.html', {'workers': workers})


def requisites_view(request):
    requisites = Requisites.objects.all().order_by('id')
    return render(request, 'requisites.html', {'requisites': requisites})


@cache_page(600)
def estate_list_by_category_view(request):
    estates = Estate.objects.filter(available=True).select_related('category')
    context = {
        'houses': [],
        'flates': [],
        'sectors': [],
        'garages': [],
        'commercial': [],
        'rent': [],
        'rooms': [],
        'others': [],
    }
    for estate in estates:
        if estate.category.name == 'Дома':
            context['houses'].append(estate)
        elif estate.category.name == 'Квартиры':
            context['flates'].append(estate)
        elif estate.category.name == 'Участки':
            context['sectors'].append(estate)
        elif estate.category.name == 'Гаражи':
            context['garages'].append(estate)
        elif estate.category.name == 'Коммерческая недвижимость':
            context['commercial'].append(estate)
        elif estate.category.name == 'Аренда':
            context['rent'].append(estate)
        elif estate.category.name == 'Комнаты':
            context['rooms'].append(estate)
        elif estate.category.name == 'Прочие':
            context['others'].append(estate)
    return render(
        request,
        'catalog.html',
        context
    )


def estate_detail_view(request, pk):
    estate = Estate.objects.get(pk=pk)
    images = estate.images.all()
    estates = Estate.objects.filter(available=True).select_related('category')
    context = {
        'houses': [],
        'flates': [],
        'sectors': [],
        'garages': [],
        'commercial': [],
        'rent': [],
        'rooms': [],
        'others': [],
        'estate': estate,
        'images': images
    }
    for estate in estates:
        category_name = estate.category.name
        if category_name == 'Дома':
            context['houses'].append(estate)
        elif category_name == 'Квартиры':
            context['flates'].append(estate)
        elif category_name == 'Участки':
            context['sectors'].append(estate)
        elif category_name == 'Гаражи':
            context['garages'].append(estate)
        elif category_name == 'Коммерческие':
            context['commercial'].append(estate)
        elif category_name == 'Аренда':
            context['rent'].append(estate)
        elif category_name == 'Комнаты':
            context['rooms'].append(estate)
        elif category_name == 'Прочие':
            context['others'].append(estate)
    return render(
        request,
        'estate_detail.html',
        context
    )
