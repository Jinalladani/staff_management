# Generated by Django 3.2.12 on 2022-04-07 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel', '0074_mailsendreport'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasksheet',
            name='mailSendReport',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='mailSendReport',
        ),
    ]
