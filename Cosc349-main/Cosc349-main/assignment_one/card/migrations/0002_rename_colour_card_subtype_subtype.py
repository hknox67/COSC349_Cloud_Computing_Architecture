# Generated by Django 4.1.1 on 2022-09-07 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card_subtype',
            old_name='colour',
            new_name='subtype',
        ),
    ]