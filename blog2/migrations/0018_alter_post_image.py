# Generated by Django 5.0.6 on 2024-07-22 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog2', '0017_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='post_images/900x300', upload_to='post_images'),
        ),
    ]
