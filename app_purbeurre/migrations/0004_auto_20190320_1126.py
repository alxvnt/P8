# Generated by Django 2.0 on 2019-03-20 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_purbeurre', '0003_auto_20190318_1316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='pseudo',
            new_name='username',
        ),
    ]
