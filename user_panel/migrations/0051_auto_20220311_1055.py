# Generated by Django 3.2.12 on 2022-03-11 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel', '0050_remove_staff_ssavalue'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='city',
        ),
        migrations.AddField(
            model_name='stock',
            name='staff_key',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_panel.staff'),
        ),
    ]
