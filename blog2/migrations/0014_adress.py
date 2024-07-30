# Generated by Django 5.0.6 on 2024-07-18 12:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog2', '0013_comments_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=200)),
                ('private_house_number', models.IntegerField(blank=True, null=True)),
                ('entrance_number', models.CharField(blank=True, max_length=10, null=True)),
                ('flat_num', models.IntegerField(blank=True, null=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='blog2.profile')),
            ],
        ),
    ]
