# Generated by Django 4.2.3 on 2023-08-20 21:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("roombooking", "0007_remove_room_average_rating"),
    ]

    operations = [
        migrations.AddField(
            model_name="room",
            name="price",
            field=models.FloatField(default=0.0),
        ),
    ]
