# Generated by Django 2.0.6 on 2018-09-07 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20180904_0911'),
    ]

    operations = [
        migrations.AddField(
            model_name='profession',
            name='detailed_description',
            field=models.TextField(default=''),
        ),
    ]
