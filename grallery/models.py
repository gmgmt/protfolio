from django.db import models

# Create your models here.
class Grallery(models.Model):
    #    django功能，文本区域描述
    description = models.CharField(max_length=100)
