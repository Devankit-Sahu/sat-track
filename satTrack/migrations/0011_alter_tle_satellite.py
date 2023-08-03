# Generated by Django 4.1.4 on 2023-08-03 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('satTrack', '0010_alter_tle_satellite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tle',
            name='satellite',
            field=models.ForeignKey(default={'name': '', 'norad_id': 0}, on_delete=django.db.models.deletion.CASCADE, to='satTrack.satellite'),
        ),
    ]
