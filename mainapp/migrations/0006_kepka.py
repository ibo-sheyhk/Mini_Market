# Generated by Django 4.1 on 2022-09-04 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_koylak'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kepka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('created_date', models.DateField()),
                ('description', models.TextField()),
                ('price', models.FloatField()),
            ],
        ),
    ]
