# Generated by Django 3.1.7 on 2021-04-27 06:55

from django.db import migrations, models
import images_api.models


class Migration(migrations.Migration):

    dependencies = [
        ('images_api', '0002_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=images_api.models.nameFile),
        ),
    ]