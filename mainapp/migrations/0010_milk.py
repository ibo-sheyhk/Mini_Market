# Generated by Django 4.1 on 2022-09-08 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_shokolod'),
    ]

    operations = [
        migrations.CreateModel(
            name='Milk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('created_date', models.DateField()),
                ('end_date', models.DateField()),
                ('description', models.TextField()),
                ('price', models.FloatField()),
            ],
        ),
    ]
