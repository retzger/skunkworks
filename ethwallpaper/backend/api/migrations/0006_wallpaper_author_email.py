# Generated by Django 2.0 on 2017-12-26 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20171226_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallpaper',
            name='author_email',
            field=models.EmailField(blank=True, max_length=255),
        ),
    ]
