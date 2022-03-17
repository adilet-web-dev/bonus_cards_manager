# Generated by Django 4.0.3 on 2022-03-17 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.IntegerField()),
                ('number', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('ends_at', models.DateTimeField()),
                ('amount', models.IntegerField()),
                ('_status', models.CharField(max_length=50)),
            ],
        ),
    ]
