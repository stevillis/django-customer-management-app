# Generated by Django 3.2.7 on 2021-09-27 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_rename_prics_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.CharField(max_length=400, null=True),
        ),
    ]
