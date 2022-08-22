# Generated by Django 3.2.12 on 2022-03-10 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel', '0038_chequedetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csc', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='dailybsnlwork',
            name='HTMLFile',
            field=models.FileField(blank=True, null=True, upload_to='media/aadharwork/', verbose_name='file'),
        ),
        migrations.CreateModel(
            name='AadharPortalCashReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_id', models.CharField(blank=True, max_length=255, null=True)),
                ('ssa', models.CharField(blank=True, max_length=255, null=True)),
                ('csc', models.CharField(blank=True, max_length=255, null=True)),
                ('newEnrollment', models.FloatField(blank=True, null=True)),
                ('AadharMandatoryUpdate', models.FloatField(blank=True, null=True)),
                ('AadharDemographicUpdate', models.FloatField(blank=True, null=True)),
                ('AadharBiometricUpdate', models.FloatField(blank=True, null=True)),
                ('totalAmount', models.FloatField(blank=True, null=True)),
                ('staff_key', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_panel.staff')),
            ],
        ),
        migrations.AddField(
            model_name='staff',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Station', to='user_panel.city'),
        ),
    ]
