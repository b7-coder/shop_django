# Generated by Django 4.2.3 on 2023-07-12 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_site', '0003_contacts'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrandsLogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstImage', models.ImageField(upload_to='')),
                ('secondImage', models.ImageField(upload_to='')),
                ('thirdImage', models.ImageField(upload_to='')),
                ('fourthImage', models.ImageField(upload_to='')),
            ],
        ),
    ]
