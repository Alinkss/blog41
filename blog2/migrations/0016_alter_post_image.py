# Generated by Django 5.0.6 on 2024-07-22 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog2', '0015_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='post_images'),
        ),
    ]
