# Generated by Django 4.2.3 on 2023-07-10 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
