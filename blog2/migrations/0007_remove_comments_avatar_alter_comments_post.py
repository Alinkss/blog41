# Generated by Django 5.0.6 on 2024-07-14 12:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog2', '0006_alter_comments_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='avatar',
        ),
        migrations.AlterField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog2.post'),
        ),
    ]
