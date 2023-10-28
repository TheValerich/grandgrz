from django.shortcuts import render
from django.views.generic import DetailView
from .models import Estate, Category


def main_page_view(request):
    best_offer = Estate.objects.filter(best_offer=True)
    return render(request, 'index.html', {'best_offer': best_offer})


def workers_view(request):
    return render(request, 'workers.html')


def requisites_view(request):
    return render(request, 'requisites.html')


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
        elif estate.category.name == 'Коммерческие':
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


class EstateDetailView(DetailView):
    model = Estate
    template_name = 'estate_detail.html'
    context_object_name = 'estate'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = Estate.objects.get(id=self.object.pk).images.all()
        return context
