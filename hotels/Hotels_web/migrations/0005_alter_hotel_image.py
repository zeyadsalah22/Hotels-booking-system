# Generated by Django 5.0.6 on 2024-06-29 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotels_web', '0004_alter_hotel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='image',
            field=models.ImageField(upload_to='hotels\\images'),
        ),
    ]
