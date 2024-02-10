from django.urls import path

from webapp.views.advert_views import IndexView, AdvertView, AdvertCreateView, AdvertUpdateView, AdvertDeleteView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('advert/<int:pk>/', AdvertView.as_view(), name='advert_view'),
    path('advert/add/', AdvertCreateView.as_view(), name='advert_create'),
    path('advert/<int:pk>/update/', AdvertUpdateView.as_view(), name='advert_update'),
    path('advert/<int:pk>/delete/', AdvertDeleteView.as_view(), name='advert_delete'),
    # path('article/<int:pk>/comment/add/', CommentCreateView.as_view(), name='comment_add'),
    # path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update_view'),
    # path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete_view'),
]