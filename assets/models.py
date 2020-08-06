from django.db import models


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
