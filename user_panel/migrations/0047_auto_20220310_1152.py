# Generated by Django 3.2.12 on 2022-03-10 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel', '0046_auto_20220310_1149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='ssa',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='station_id',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='username',
        ),
        migrations.AddField(
            model_name='stock',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
