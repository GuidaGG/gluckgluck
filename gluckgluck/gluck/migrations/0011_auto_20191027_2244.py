# Generated by Django 2.2.6 on 2019-10-27 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gluck', '0010_auto_20191027_2234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='section',
            old_name='Image',
            new_name='image',
        ),
    ]
