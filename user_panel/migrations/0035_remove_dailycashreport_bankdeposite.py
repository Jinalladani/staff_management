# Generated by Django 3.2.12 on 2022-03-09 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel', '0034_alter_staff_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailycashreport',
            name='bankDeposite',
        ),
    ]
