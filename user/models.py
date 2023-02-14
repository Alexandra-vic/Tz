from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50, blank=False, verbose_name='автор')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'автор'
        verbose_name_plural = 'авторы'
        ordering = ('-id',)          
