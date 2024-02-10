from django.urls import path

from webapp.views.advert_views import IndexView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]