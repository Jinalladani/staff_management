# Generated by Django 3.2.12 on 2022-03-25 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel', '0068_otf'),
    ]

    operations = [
        migrations.AddField(
            model_name='depositecash',
            name='fileStore',
            field=models.FileField(blank=True, null=True, upload_to='media/depositeRecepite/', verbose_name='file'),
        ),
        migrations.AddField(
            model_name='depositecash',
            name='personName',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='depositecash',
            name='transaction_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
