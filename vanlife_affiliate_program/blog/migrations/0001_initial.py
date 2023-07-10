# Generated by Django 4.2.3 on 2023-07-10 17:10

from django.db import migrations, models
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(blank=True, default='', max_length=200)),
                ('blog_slug', models.SlugField(unique=True, verbose_name='Blog slug')),
                ('content', tinymce.models.HTMLField(blank=True, default='')),
                ('notes', tinymce.models.HTMLField(blank=True, default='')),
                ('published', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date published')),
            ],
            options={
                'verbose_name_plural': 'Blogs',
                'ordering': ['-published'],
            },
        ),
    ]
