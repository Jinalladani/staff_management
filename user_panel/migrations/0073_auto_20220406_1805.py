# Generated by Django 3.2.12 on 2022-04-07 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel', '0072_auto_20220406_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='aadharportalcashreport',
            name='machine_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aadharportalcashreport',
            name='user_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tasksheet',
            name='user_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
