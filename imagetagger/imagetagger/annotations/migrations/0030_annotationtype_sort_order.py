# Generated by Django 2.0.13 on 2019-11-27 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotations', '0029_auto_20191121_0936'),
    ]

    operations = [
        migrations.AddField(
            model_name='annotationtype',
            name='sort_order',
            field=models.IntegerField(default=0),
        ),
    ]