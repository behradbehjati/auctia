# Generated by Django 4.1.7 on 2023-03-27 16:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("market", "0012_alter_item_image1_alter_item_image2_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="image1",
            field=models.ImageField(height_field=500, upload_to="", width_field=500),
        ),
        migrations.AlterField(
            model_name="item",
            name="image2",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="item",
            name="image3",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
