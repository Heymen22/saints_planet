# Generated by Django 4.0.5 on 2022-06-07 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='static/uploaded_img/'),
        ),
    ]