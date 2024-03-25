from django.db import models
from django.conf import settings
from users.models import CustomUser
from django.urls import reverse
import pytz
from datetime import datetime
from django.utils.text import slugify
# from django.utils.translation import ugettext_lazy as _


class Posts(models.Model):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=("profile"), on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"slug": self.slug})
    