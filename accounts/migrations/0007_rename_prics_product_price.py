# Generated by Django 3.2.7 on 2021-09-27 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210926_2143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='prics',
            new_name='price',
        ),
    ]
