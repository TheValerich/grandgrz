from django.shortcuts import render, get_object_or_404
from .models import Estate, Category


def main_page_view(request):
    best_offer = Estate.objects.filter(best_offer=True)
    return render(request, 'index.html', {'best_offer': best_offer})


def workers_view(request):
    return render(request, 'workers.html')


def requisites_view(request):
    return render(request, 'requisites.html')


# def estate_list_view(request, category_slug=None):
#     category = None
#     categories = Category.objects.all()
#     estates = Estate.objects.filter(available=True)
#     if category_slug:
#         category = get_object_or_404(
#             Category,
#             slug=category_slug
#         )
#         estates = estates.filter(category=category)
#     return render(
#         request,
#         'catalog1.html',
#         {
#             'category': category,
#             'categories': categories,
#             'estates': estates,
#         }
#     )


def estate_list_by_category_view(request):  # TODO добавить блок try-except
    houses=Category.objects.get(name='Дома').estates.all().filter(available=True)
    flates=Category.objects.get(name='Квартиры').estates.all().filter(available=True)
    sectors=Category.objects.get(name='Участки').estates.all().filter(available=True)
    garages=Category.objects.get(name='Гаражи').estates.all().filter(available=True)
    commercials=Category.objects.get(name='Коммерческие').estates.all().filter(available=True)
    rent=Category.objects.get(name='Аренда').estates.all().filter(available=True)
    rooms=Category.objects.get(name='Комнаты').estates.all().filter(available=True)
    # others=Category.objects.get(name='Прочие').estates.all().filter(available=True)
    return render(
        request,
        'catalog.html',
        {
            'houses': houses,
            'flates': flates,
            'sectors': sectors,
            'garages': garages,
            'commercial': commercials,
            'rent': rent,
            'rooms': rooms,
            # 'others': others
        }
    )
