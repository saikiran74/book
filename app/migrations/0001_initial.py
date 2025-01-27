# Generated by Django 4.0.3 on 2022-03-07 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='All',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='None', max_length=2000)),
                ('firstname', models.CharField(default='None', max_length=2000)),
                ('lastname', models.CharField(default='None', max_length=5000)),
                ('email', models.CharField(default='None', max_length=5000)),
                ('country', models.CharField(default='None', max_length=500)),
                ('history', models.CharField(default='', max_length=50000)),
                ('age', models.IntegerField(default=0)),
            ],
        ),
    ]
