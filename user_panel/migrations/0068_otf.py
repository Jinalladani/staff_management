# Generated by Django 3.2.12 on 2022-03-21 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel', '0067_alter_stockupdate_normalsimsale'),
    ]

    operations = [
        migrations.CreateModel(
            name='Otf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_id', models.CharField(blank=True, max_length=255, null=True)),
                ('ssa', models.CharField(blank=True, max_length=255, null=True)),
                ('csc', models.CharField(blank=True, max_length=255, null=True)),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField()),
                ('amount', models.FloatField()),
                ('staff_key', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_panel.staff')),
            ],
        ),
    ]