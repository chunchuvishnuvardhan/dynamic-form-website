# Generated by Django 3.0.1 on 2021-01-03 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataapp', '0003_auto_20210103_1140'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='family',
            unique_together={('name', 'electricity')},
        ),
    ]
