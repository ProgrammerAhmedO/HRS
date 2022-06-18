# Generated by Django 3.1.4 on 2022-04-28 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='payment_method',
            field=models.CharField(choices=[('VISA', 'VISA'), ('Cash', 'Cash')], default='Cash', max_length=20),
            preserve_default=False,
        ),
    ]
