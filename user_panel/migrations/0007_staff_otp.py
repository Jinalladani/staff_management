# Generated by Django 3.2.12 on 2022-03-01 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel', '0006_remove_tasksheet_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='otp',
            field=models.CharField(default=359, max_length=6),
        ),
    ]