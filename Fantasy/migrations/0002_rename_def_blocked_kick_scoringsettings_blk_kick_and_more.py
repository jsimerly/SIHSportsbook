# Generated by Django 4.0 on 2022-09-24 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Fantasy', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scoringsettings',
            old_name='def_blocked_kick',
            new_name='blk_kick',
        ),
        migrations.RenameField(
            model_name='scoringsettings',
            old_name='def_forced_fum',
            new_name='def_st_ff',
        ),
        migrations.RenameField(
            model_name='scoringsettings',
            old_name='def_fum_rec',
            new_name='def_st_fum_rec',
        ),
        migrations.RenameField(
            model_name='scoringsettings',
            old_name='def_int',
            new_name='def_st_td',
        ),
        migrations.RenameField(
            model_name='scoringsettings',
            old_name='def_pa_27',
            new_name='ff',
        ),
        migrations.RenameField(
            model_name='scoringsettings',
            old_name='fg_0_19',
            new_name='fgm_0_19',
        ),
        migrations.RenameField(
            model_name='scoringsettings',
            old_name='fg_30_39',
            new_name='fgm_20_29',
        ),
        migrations.RenameField(
            model_name='scoringsettings',
            old_name='fg_20_29',
            new_name='fgm_30_39',
        ),
        migrations.RenameField(
            model_name='scoringsettings',
            old_name='def_pa_13',
            new_name='fgm_40_49',
        ),
        migrations.RenameField(
            model_name='scoringsettings',
            old_name='fg_50_plus',
            new_name='fgm_50p',
        ),
        migrations.RenameField(
            model_name='scoringsettings',
            old_name='def_pa_35_plus',
            new_name='fgmiss',
        ),
        migrations.RenameField(
            model_name='scoringsettings',
            old_name='fg_miss',
            new_name='fum',
        ),
        migrations.RenameField(
            model_name='scoringsettings',
            old_name='fumble_lost',
            new_name='fum_lost',
        ),
        migrations.RenameField(
            model_name='scoringsettings',
            old_name='def_sack',
            new_name='fum_rec',
        ),
        migrations.RenameField(
            model_name='scoringsettings',
            old_name='def_saftey',
            new_name='fum_rec_td',
        ),
        migrations.RenameField(
            model_name='scoringsettings',
            old_name='pass_2pts',
            new_name='int',
        ),
        migrations.RenameField(
            model_name='scoringsettings',
            old_name='rec_2pts',
            new_name='pass_2pt',
        ),
        migrations.RenameField(
            model_name='scoringsettings',
            old_name='pass_ints',
            new_name='pass_int',
        ),
        migrations.RenameField(
            model_name='scoringsettings',
            old_name='fg_40_49',
            new_name='pass_td',
        ),
        migrations.RenameField(
            model_name='scoringsettings',
            old_name='pass_yds',
            new_name='pass_yd',
        ),
        migrations.RenameField(
            model_name='scoringsettings',
            old_name='def_pa_0',
            new_name='pts_allow_0',
        ),
        migrations.RenameField(
            model_name='scoringsettings',
            old_name='rush_2pts',
            new_name='pts_allow_14_20',
        ),
        migrations.RenameField(
            model_name='scoringsettings',
            old_name='def_pa_6',
            new_name='pts_allow_1_6',
        ),
        migrations.RenameField(
            model_name='scoringsettings',
            old_name='xp_made',
            new_name='pts_allow_21_27',
        ),
        migrations.RenameField(
            model_name='scoringsettings',
            old_name='def_pa_34',
            new_name='pts_allow_28_34',
        ),
        migrations.RenameField(
            model_name='scoringsettings',
            old_name='fumble',
            new_name='pts_allow_35p',
        ),
        migrations.RenameField(
            model_name='scoringsettings',
            old_name='pass_tds',
            new_name='pts_allow_7_13',
        ),
        migrations.RenameField(
            model_name='scoringsettings',
            old_name='ppr',
            new_name='rec',
        ),
        migrations.RenameField(
            model_name='scoringsettings',
            old_name='rec_tds',
            new_name='rec_td',
        ),
        migrations.RenameField(
            model_name='scoringsettings',
            old_name='rec_yds',
            new_name='rec_yd',
        ),
        migrations.RenameField(
            model_name='scoringsettings',
            old_name='rush_tds',
            new_name='rush_td',
        ),
        migrations.RenameField(
            model_name='scoringsettings',
            old_name='rush_yds',
            new_name='rush_yd',
        ),
        migrations.RenameField(
            model_name='scoringsettings',
            old_name='xp_miss',
            new_name='xpmiss',
        ),
        migrations.AddField(
            model_name='scoringsettings',
            name='rec_2pt',
            field=models.DecimalField(decimal_places=3, default=2, max_digits=6),
        ),
        migrations.AddField(
            model_name='scoringsettings',
            name='rush_2pt',
            field=models.DecimalField(decimal_places=3, default=2, max_digits=6),
        ),
        migrations.AddField(
            model_name='scoringsettings',
            name='sack',
            field=models.DecimalField(decimal_places=3, default=1, max_digits=6),
        ),
        migrations.AddField(
            model_name='scoringsettings',
            name='safe',
            field=models.DecimalField(decimal_places=3, default=1, max_digits=6),
        ),
        migrations.AddField(
            model_name='scoringsettings',
            name='st_ff',
            field=models.DecimalField(decimal_places=3, default=1, max_digits=6),
        ),
        migrations.AddField(
            model_name='scoringsettings',
            name='st_fum_rec',
            field=models.DecimalField(decimal_places=3, default=2, max_digits=6),
        ),
        migrations.AddField(
            model_name='scoringsettings',
            name='st_td',
            field=models.DecimalField(decimal_places=3, default=6, max_digits=6),
        ),
        migrations.AddField(
            model_name='scoringsettings',
            name='xpm',
            field=models.DecimalField(decimal_places=3, default=1, max_digits=6),
        ),
        migrations.AlterField(
            model_name='fantasyteam',
            name='league',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='teams', to='Fantasy.fantasyleague'),
        ),
    ]