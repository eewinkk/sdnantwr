# Generated by Django 4.0.3 on 2022-03-10 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_data', '0006_alter_guru_title_guru_alter_guru_ttl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guru',
            name='ttl',
            field=models.DateField(blank=True, verbose_name='TTL'),
        ),
    ]
