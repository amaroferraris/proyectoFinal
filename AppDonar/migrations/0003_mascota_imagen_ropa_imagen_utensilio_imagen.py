# Generated by Django 4.1.1 on 2022-10-18 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppDonar', '0002_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='articulos'),
        ),
        migrations.AddField(
            model_name='ropa',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='articulos'),
        ),
        migrations.AddField(
            model_name='utensilio',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='articulos'),
        ),
    ]
