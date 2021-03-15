from django.urls import path
from rest_framework import routers

from fpapp.views import FavoriteListViewSet, content, FavoriteListView

router = routers.DefaultRouter()
router.register('api/favorite_list', FavoriteListViewSet)

urlpatterns = [
                  path('', content, name="images"),
                  path('favorite/', FavoriteListView.as_view(), name="favorite"),
              ] + router.urls
