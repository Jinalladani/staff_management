# Generated by Django 3.2.12 on 2022-03-01 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel', '0003_alter_tasksheet_taskstatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100)),
                ('value', models.TextField()),
            ],
        ),
    ]