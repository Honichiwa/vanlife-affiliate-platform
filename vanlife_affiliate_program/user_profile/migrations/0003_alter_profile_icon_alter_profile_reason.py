# Generated by Django 4.2.2 on 2023-06-30 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_profilereason_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='icon',
            field=models.ForeignKey(blank=True, limit_choices_to={'name__isnull': False}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profiles', to='user_profile.profileicon', verbose_name='icon'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='reason',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to='user_profile.profilereason', verbose_name='reason'),
        ),
    ]
