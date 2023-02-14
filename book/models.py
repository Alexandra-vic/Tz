from django.db import models
from category.models import Category, Tag
from user.models import User



class Book(models.Model):
    book_name = models.CharField(max_length=255, blank=True, verbose_name='Название')
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE, related_name='book_category', verbose_name='category')
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='authors')
    book_tags = models.ManyToManyField(Tag, related_name='book_tags') 


    def __str__(self) -> str:
        return f'{self.book_name} - {self.author}'   
    
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ['-id']
