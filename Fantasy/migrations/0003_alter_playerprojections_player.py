# Generated by Django 4.0 on 2022-06-06 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Fantasy', '0002_alter_scoringsettings_def_blocked_kick_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playerprojections',
            name='player',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='proj', to='Fantasy.player'),
        ),
    ]
