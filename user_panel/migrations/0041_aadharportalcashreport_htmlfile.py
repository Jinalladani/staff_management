# Generated by Django 3.2.12 on 2022-03-10 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel', '0040_auto_20220310_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='aadharportalcashreport',
            name='HTMLFile',
            field=models.FileField(blank=True, null=True, upload_to='media/aadharPortalCashReoprt/', verbose_name='file'),
        ),
    ]
