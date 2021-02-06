# Generated by Django 3.0.1 on 2021-01-03 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('electricity', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('role', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('qual', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='basic',
            name='nof',
        ),
    ]