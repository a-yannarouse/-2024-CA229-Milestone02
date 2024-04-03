# Generated by Django 4.2.9 on 2024-04-03 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Page",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=60)),
                ("permalink", models.CharField(max_length=12, unique=True)),
                ("bodytext", models.TextField(blank=True, verbose_name="Page Content")),
            ],
        ),
    ]