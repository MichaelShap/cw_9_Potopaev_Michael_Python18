from datetime import datetime, timezone

from django.db import models
from django.contrib.auth import get_user_model

STATUS = [('moderation', 'модерация'), ('published', 'опубликовано'), ('canceled', 'отклонено'),
          ('deleted', 'удалено')]


class Category(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Category')

    def __str__(self):
        return f'{self.name}'


class Advert(models.Model):
    photo = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Photo')
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name='Title')
    description = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Description')
    author = models.ForeignKey(get_user_model(), related_name='adverts', null=False, blank=False,
                               on_delete=models.CASCADE, verbose_name="Advert author")
    advert_category = models.ForeignKey(Category, related_name='categories', null=False, blank=False,
                                        on_delete=models.CASCADE, verbose_name="Chosen category")
    price = models.PositiveIntegerField(blank=False, null=False, verbose_name="Price")
    advert_status = models.CharField(max_length=50, choices=STATUS, default='moderation', null=False, blank=False,
                                     verbose_name='Status')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    published = models.DateTimeField(auto_now=False, null=True, blank=True, verbose_name='Published at')
    updated = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Updated at')

    def __str__(self):
        return f'{self.pk}. {self.title}'


class Comment(models.Model):
    text = models.TextField(max_length=1000, null=False, blank=False, verbose_name='Comment body')
    author = models.ForeignKey(get_user_model(), related_name='comments', null=False, blank=False,
                               on_delete=models.CASCADE, verbose_name="Comment author")
    advert = models.ForeignKey(Advert, related_name='advert_comments', null=False, blank=False,
                               on_delete=models.CASCADE, verbose_name="Commented advert")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Comment created at')

    def __str__(self):
        return f'{self.id}. {self.author}'
