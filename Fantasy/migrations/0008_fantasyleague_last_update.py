# Generated by Django 4.0 on 2022-09-28 01:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Fantasy', '0007_rename_idk_tkl_solo_scoringsettings_bonus_def_fum_td_50p_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fantasyleague',
            name='last_update',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]