# Generated by Django 5.1.4 on 2024-12-22 21:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Назва свята')),
                ('description', models.TextField(blank=True, verbose_name='Про свято')),
                ('date', models.DateField(verbose_name='дата святкування')),
                ('is_fixed', models.BooleanField(default=True, verbose_name='Фіксована дата')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата останнього оновлення')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Свято',
                'verbose_name_plural': 'Свята',
                'ordering': ['date'],
            },
        ),
    ]
