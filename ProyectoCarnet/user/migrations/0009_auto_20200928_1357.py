# Generated by Django 3.1 on 2020-09-28 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_nacionalidad_cantidad_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nacionalidad',
            name='cantidad_users',
            field=models.IntegerField(blank=True),
        ),
    ]
