# Generated by Django 4.1.7 on 2023-06-18 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_kids_women'),
    ]

    operations = [
        migrations.CreateModel(
            name='Men',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mname', models.CharField(max_length=225)),
                ('mprice', models.FloatField()),
                ('mimage', models.CharField(max_length=2500)),
            ],
        ),
        migrations.CreateModel(
            name='Unisex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=225)),
                ('uprice', models.FloatField()),
                ('uimage', models.CharField(max_length=2500)),
            ],
        ),
    ]
