# Generated by Django 2.1 on 2018-08-19 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('location', models.FloatField(blank=True, null=True)),
                ('contact_no', models.CharField(max_length=20)),
                ('alternative_no', models.CharField(max_length=20)),
            ],
        ),
    ]