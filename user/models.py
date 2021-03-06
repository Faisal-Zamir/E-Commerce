from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_img')
    phon = models.IntegerField(blank=True, null=True, default="0")
    address = models.CharField(max_length=300, default="None")

    def __str__(self):
        return f'{self.user.username} Profile'
    
    # def save(self):
    #     super().save()
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

