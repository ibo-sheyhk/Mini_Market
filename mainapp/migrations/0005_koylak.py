# Generated by Django 4.1 on 2022-09-04 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_futbolka'),
    ]

    operations = [
        migrations.CreateModel(
            name='Koylak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('created_date', models.DateField()),
                ('description', models.TextField()),
                ('price', models.FloatField()),
            ],
        ),
    ]
