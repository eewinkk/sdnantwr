# Generated by Django 4.0.3 on 2022-03-10 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master_data', '0003_alter_guru_options_alter_kelas_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guru',
            old_name='Kota',
            new_name='kota',
        ),
        migrations.RenameField(
            model_name='santri',
            old_name='Kota',
            new_name='kota',
        ),
    ]
