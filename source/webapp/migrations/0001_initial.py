# Generated by Django 4.2.7 on 2024-02-10 06:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='user_pics', verbose_name='Photo')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('description', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Description')),
                ('price', models.PositiveIntegerField(verbose_name='Price')),
                ('advert_status', models.CharField(choices=[('on moderation', 'на модерации'), ('published', 'опубликовано'), ('canceled', 'отклонено'), ('on delete', 'на удалении')], default='on_moderation', max_length=50, verbose_name='Category')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('published', models.DateTimeField(verbose_name='Published at')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Updated at')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('cars', 'авто'), ('business', 'бизнес'), ('apartment', 'недвижимость')], max_length=50, verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1000, verbose_name='Comment body')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Comment created at')),
                ('advert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='advert_comments', to='webapp.advert', verbose_name='Commented advert')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Comment author')),
            ],
        ),
        migrations.AddField(
            model_name='advert',
            name='advert_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='webapp.category', verbose_name='Chosen category'),
        ),
        migrations.AddField(
            model_name='advert',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adverts', to=settings.AUTH_USER_MODEL, verbose_name='Advert author'),
        ),
    ]
