# Generated by Django 3.0.8 on 2020-08-06 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0004_auto_20200806_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='moved_to_general',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
