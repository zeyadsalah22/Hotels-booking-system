# Generated by Django 5.0.6 on 2024-06-29 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotels_web', '0002_hotel_feedback_room_booking_services'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='description',
            field=models.TextField(default='No description'),
        ),
    ]
