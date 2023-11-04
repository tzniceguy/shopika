# Generated by Django 4.2.5 on 2023-11-02 08:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        (
            "shoppers",
            "0002_alter_products_category_alter_products_description_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="products",
            name="image",
            field=models.ImageField(
                default=django.utils.timezone.now, upload_to="products/"
            ),
            preserve_default=False,
        ),
    ]