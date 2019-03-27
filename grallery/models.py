from django.db import models

# Create your models here.
class Grallery(models.Model):
    #    django功能，文本区域描述
    description = models.CharField(default='在这里写作品的简介', max_length=100)
    #   添加图片模块功能
    image = models.ImageField(default='default.png', upload_to='images/')
    #    标题
    title = models.CharField(default='作品标题', max_length=50)


    def __str__(self):
        #      返回值作为后台显示名字
       return self.title
