# Generated by Django 3.0.8 on 2020-08-04 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='asset_type',
            field=models.CharField(choices=[('3d', '3D'), ('2d', '2D'), ('addons', 'Add-on'), ('rigged_models', 'Rigged Models'), ('essentials', 'Essentials'), ('gui', 'GUI'), ('templates', 'Templates'), ('audio', 'Audio'), ('tools', 'Tools'), ('vfx', 'VFX')], max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
