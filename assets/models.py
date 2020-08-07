from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    ROLE_CHOICES = [
        ('user', 'User'),
        ('contributor', 'Contributor'),
        ('moderator', 'Moderator'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=150)
    role = models.CharField(max_length=25, choices=ROLE_CHOICES, default='user', null=True)
    payment_email = models.EmailField(max_length=150, null=True)
    contributor_link = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Tag(models.Model):
    name = models.CharField(max_length=30, null=True)
    description = models.TextField(max_length=600, blank=True)

    def __str__(self):
        return f"Tag: {self.name}"


class Asset(models.Model):
    TYPE_CHOICES = [
        ('3d', '3D'),
        ('2d', '2D'),
        ('addons', 'Add-on'),
        ('rigged_models', 'Rigged Models'),
        ('essentials', 'Essentials'),
        ('gui', 'GUI'),
        ('templates', 'Templates'),
        ('audio', 'Audio'),
        ('tools', 'Tools'),
        ('vfx', 'VFX'),
    ]
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(max_length=800, null=True)
    asset_type = models.CharField(max_length=25, choices=TYPE_CHOICES, null=True)
    creation_date = models.DateTimeField(auto_now_add=True, null=True)
    moved_to_general = models.DateTimeField(null=True, blank=True)
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ('-creation_date', 'name')

    def __str__(self):
        return f"Asset: {self.name} - {self.id}"
