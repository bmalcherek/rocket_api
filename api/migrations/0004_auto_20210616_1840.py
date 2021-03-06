# Generated by Django 3.2.4 on 2021-06-16 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booster',
            name='expended',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='booster',
            name='launches_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='booster',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.rocketmodel'),
        ),
        migrations.AlterField(
            model_name='launch',
            name='booster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.booster'),
        ),
        migrations.AlterField(
            model_name='launch',
            name='launch_platform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.launchplatform'),
        ),
        migrations.AlterField(
            model_name='launch',
            name='payload',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.payload'),
        ),
    ]
