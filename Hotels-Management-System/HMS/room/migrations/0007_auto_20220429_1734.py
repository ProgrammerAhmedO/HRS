# Generated by Django 3.1.4 on 2022-04-29 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0006_auto_20220429_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='capacity',
            field=models.SmallIntegerField(),
        ),
    ]
