# Generated by Django 4.2.3 on 2023-08-17 10:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("roombooking", "0008_rename_reviews_review"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="rating",
            field=models.FloatField(),
        ),
    ]
