from django.contrib import admin
from webapp.models import Comment, Advert, Category

admin.site.register(Advert)
admin.site.register(Comment)
admin.site.register(Category)
