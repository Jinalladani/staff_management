# Generated by Django 3.2.12 on 2022-03-10 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel', '0047_auto_20220310_1152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ssavalue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ssa', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='ssavalue',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_panel.ssavalue'),
        ),
    ]
