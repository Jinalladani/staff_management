# Generated by Django 3.2.12 on 2022-03-01 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel', '0009_dailyfileattach'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyfileattach',
            name='taskStatus',
            field=models.BooleanField(default=True),
        ),
    ]
