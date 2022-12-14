# Generated by Django 3.2.12 on 2022-03-04 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel', '0020_auto_20220304_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depositName', models.CharField(blank=True, max_length=255, null=True)),
                ('csc', models.CharField(blank=True, max_length=255, null=True)),
                ('totalAmount', models.FloatField(blank=True, max_length=255, null=True)),
                ('depositAmount', models.FloatField(blank=True, max_length=255, null=True)),
                ('cashInHand', models.FloatField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('simValue', models.CharField(blank=True, max_length=255, null=True)),
                ('csc', models.CharField(blank=True, max_length=255, null=True)),
                ('stock', models.IntegerField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
