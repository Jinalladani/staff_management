# Generated by Django 3.2.12 on 2022-03-15 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel', '0060_aadharportalcashreport'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aadharportalcashreport',
            name='csc',
        ),
        migrations.RemoveField(
            model_name='balance',
            name='csc',
        ),
        migrations.RemoveField(
            model_name='chequedetail',
            name='csc',
        ),
        migrations.RemoveField(
            model_name='dailybsnlwork',
            name='csc',
        ),
        migrations.RemoveField(
            model_name='dailycashreport',
            name='csc',
        ),
        migrations.RemoveField(
            model_name='depositecash',
            name='csc',
        ),
        migrations.RemoveField(
            model_name='tasksheet',
            name='csc',
        ),
        migrations.AddField(
            model_name='aadharportalcashreport',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_panel.city'),
        ),
        migrations.AddField(
            model_name='balance',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_panel.city'),
        ),
        migrations.AddField(
            model_name='chequedetail',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_panel.city'),
        ),
        migrations.AddField(
            model_name='dailybsnlwork',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_panel.city'),
        ),
        migrations.AddField(
            model_name='dailycashreport',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_panel.city'),
        ),
        migrations.AddField(
            model_name='depositecash',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_panel.city'),
        ),
        migrations.AddField(
            model_name='tasksheet',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_panel.city'),
        ),
        migrations.AlterField(
            model_name='aadharportalcashreport',
            name='ssa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_panel.ssavalue'),
        ),
        migrations.AlterField(
            model_name='balance',
            name='ssa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_panel.ssavalue'),
        ),
        migrations.AlterField(
            model_name='chequedetail',
            name='ssa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_panel.ssavalue'),
        ),
        migrations.AlterField(
            model_name='dailybsnlwork',
            name='ssa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_panel.ssavalue'),
        ),
        migrations.AlterField(
            model_name='dailycashreport',
            name='ssa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_panel.ssavalue'),
        ),
        migrations.AlterField(
            model_name='depositecash',
            name='ssa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_panel.ssavalue'),
        ),
        migrations.AlterField(
            model_name='tasksheet',
            name='ssa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_panel.ssavalue'),
        ),
    ]