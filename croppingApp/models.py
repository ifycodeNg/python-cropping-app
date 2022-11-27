from django.db import models



class Photo(models.Model):
    IMAGE_CHOICE = [
        ("real", 'real'),
        ("fake", 'fake'),
       
    ]
    file = models.ImageField(upload_to='media')
    category = models.CharField(
        max_length=10,
        choices=IMAGE_CHOICE,
        default=None,
    )

    class Meta:
        verbose_name = 'photo'
        verbose_name_plural = 'photos'
