# Generated by Django 3.2.12 on 2022-03-02 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel', '0014_alter_weeklyfileattach_type_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasksheet',
            name='staff_key',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_panel.staff'),
        ),
    ]
