# Generated by Django 4.0 on 2022-04-26 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=124, verbose_name='password'),
        ),
    ]
