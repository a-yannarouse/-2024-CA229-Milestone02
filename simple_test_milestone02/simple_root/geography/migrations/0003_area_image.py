# Generated by Django 4.2.9 on 2024-04-10 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("geography", "0002_attraction_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="area",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="area_images/"),
        ),
    ]
