# Generated by Django 3.2.12 on 2022-03-15 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel', '0056_rename_ssavalue_stock_ssa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aadharportalcashreport',
            name='csc',
        ),
        migrations.AddField(
            model_name='aadharportalcashreport',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_panel.city'),
        ),
        migrations.AlterField(
            model_name='aadharportalcashreport',
            name='ssa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_panel.ssavalue'),
        ),
    ]
