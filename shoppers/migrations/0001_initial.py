# Generated by Django 4.2.5 on 2023-10-24 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=50, verbose_name='')),
                ('category', models.CharField(max_length=50, verbose_name='')),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
