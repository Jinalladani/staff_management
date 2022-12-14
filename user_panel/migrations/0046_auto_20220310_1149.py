# Generated by Django 3.2.12 on 2022-03-10 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel', '0045_rename_portalcashreport_aadharportalcashreport'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='csc',
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_id', models.CharField(blank=True, max_length=255, null=True)),
                ('ssa', models.CharField(blank=True, max_length=255, null=True)),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('CBPValue', models.IntegerField(blank=True, null=True)),
                ('C_TopValue', models.IntegerField(blank=True, null=True)),
                ('NormalSimSale', models.IntegerField(blank=True, null=True)),
                ('MnpSim', models.IntegerField(blank=True, null=True)),
                ('Swapping', models.IntegerField(blank=True, null=True)),
                ('PostpaidSim', models.IntegerField(blank=True, null=True)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_panel.city')),
            ],
        ),
    ]
