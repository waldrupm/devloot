# Generated by Django 3.0.8 on 2020-08-09 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0009_featuredset'),
    ]

    operations = [
        migrations.AddField(
            model_name='featuredset',
            name='name',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
