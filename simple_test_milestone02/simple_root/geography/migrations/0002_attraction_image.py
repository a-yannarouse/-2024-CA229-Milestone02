# Generated by Django 4.2.9 on 2024-04-04 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("geography", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="attraction",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="attraction_images/"
            ),
        ),
    ]
