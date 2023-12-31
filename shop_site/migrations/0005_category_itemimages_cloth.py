# Generated by Django 4.2.3 on 2023-07-19 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop_site', '0004_brandslogo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='ItemImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('gender', models.CharField(choices=[('М', 'Мужской'), ('Ж', ':Женский')], default='М', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Cloth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('М', 'Мужской'), ('Ж', ':Женский')], default='М', max_length=1)),
                ('color', models.CharField(max_length=250)),
                ('size', models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')], default='S', max_length=2)),
                ('price_manufacturer', models.FloatField()),
                ('price', models.FloatField()),
                ('categoryObject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_site.category')),
                ('imageObject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_site.itemimages')),
            ],
        ),
    ]
