# Generated by Django 4.1.7 on 2023-05-18 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kids',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kname', models.CharField(max_length=255)),
                ('kprice', models.FloatField()),
                ('kimage', models.CharField(max_length=2500)),
            ],
        ),
        migrations.CreateModel(
            name='Women',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wname', models.CharField(max_length=225)),
                ('wprice', models.FloatField()),
                ('wimage', models.CharField(max_length=2500)),
            ],
        ),
    ]
