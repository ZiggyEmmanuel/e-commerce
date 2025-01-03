# Generated by Django 5.0.7 on 2024-08-11 09:03

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
            name='AboutPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='About Us', max_length=100)),
                ('content', models.TextField()),
                ('background_image', models.ImageField(blank=True, null=True, upload_to='backgrounds/')),
            ],
            options={
                'verbose_name': 'About Page',
                'verbose_name_plural': 'About Pages',
            },
        ),
        migrations.CreateModel(
            name='ContactPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Contact Us', max_length=100)),
                ('content', models.TextField()),
                ('background_image', models.ImageField(blank=True, null=True, upload_to='backgrounds/')),
            ],
            options={
                'verbose_name': 'Contact Page',
                'verbose_name_plural': 'Contact Pages',
            },
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Home', max_length=100)),
                ('content', models.TextField()),
                ('background_image', models.ImageField(blank=True, null=True, upload_to='backgrounds/')),
            ],
            options={
                'verbose_name': 'Home Page',
                'verbose_name_plural': 'Home Pages',
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
