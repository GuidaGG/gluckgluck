# Generated by Django 2.2.6 on 2019-10-27 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gluck', '0009_auto_20191027_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='Image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='section',
            name='text',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='section_title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
