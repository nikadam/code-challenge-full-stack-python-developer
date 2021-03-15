from django.contrib import messages
from django.shortcuts import render
from django.views import generic
from rest_framework import viewsets

from fpapp.models import FavoriteList, CurrentList
from fpapp.resources import get_result_for_search
from fpapp.serializers import FavoriteListSerializer, CurrentListSerializer


def content(request):
    page = request.GET.get('page', 1)

    places = [dict(x) for x in CurrentListSerializer(CurrentList.objects.all(), many=True).data]
    context = {"places": places}
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')
    error = False
    if not (lat and lon):
        messages.add_message(request, messages.INFO, "Need lat and lon or select a Location")
        return render(request, 'home.html', context)
    data = get_result_for_search(lat=lat, long=lon, page=page)
    if data['stat'] == 'fail':
        messages.add_message(request, messages.WARNING, data['message'])
        return render(request, 'home.html', context)
    if data['photos']['total'] == '0':
        messages.add_message(request, messages.WARNING, "No photos found for given Lat and Lon")
        return render(request, 'home.html', context)

    context.update({'photos': data['photos'],
                    "loop_range": range(1, data['photos']['pages'] + 1)})
    return render(request, 'home.html', context)


class FavoriteListViewSet(viewsets.ModelViewSet):
    queryset = FavoriteList.objects.all()
    serializer_class = FavoriteListSerializer


class FavoriteListView(generic.ListView):
    template_name = 'favorite.html'
    queryset = FavoriteList.objects.all()
    paginate_by = 10
    context_object_name = "favorite_list"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(FavoriteListView, self).get_context_data()
        context['photos'] = {"page": context['page_obj'].number,
                             "pages": context['paginator'].num_pages}
        context['loop_range'] = range(1, context['paginator'].num_pages + 1)
        return context
