# Generated by Django 4.0.3 on 2022-03-17 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='_status',
            new_name='status',
        ),
    ]