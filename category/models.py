from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=225, blank=True, null=True, verbose_name='нзвание')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'категрия'
        verbose_name_plural = 'категории'
        ordering = ('-id',)   
    


class Tag(models.Model):
    tag = models.CharField(max_length=225, blank=True, null=True, verbose_name='тег')
   
    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'
        ordering = ('-id',) 
