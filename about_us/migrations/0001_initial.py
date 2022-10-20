# Generated by Django 3.2.15 on 2022-10-11 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComingMovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=525)),
                ('duration', models.CharField(max_length=108)),
                ('grade', models.CharField(max_length=255)),
                ('poster_url', models.CharField(max_length=2025)),
                ('book_url', models.CharField(max_length=2025)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=525)),
                ('duration', models.CharField(max_length=108)),
                ('grade', models.CharField(max_length=255)),
                ('poster_url', models.CharField(max_length=2025)),
                ('book_url', models.CharField(max_length=2025)),
            ],
        ),
    ]
