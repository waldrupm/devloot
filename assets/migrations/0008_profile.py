# Generated by Django 3.1 on 2020-08-07 04:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assets', '0007_asset_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=150)),
                ('role', models.CharField(choices=[('user', 'User'), ('contributor', 'Contributor'), ('moderator', 'Moderator')], default='user', max_length=25, null=True)),
                ('payment_email', models.EmailField(max_length=150, null=True)),
                ('contributor_link', models.CharField(max_length=200, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
