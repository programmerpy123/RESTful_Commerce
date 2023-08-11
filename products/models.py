from django.db import models
from django.core.exceptions import ValidationError


def validate_positive(value):
    if value <= 0:
        raise ValidationError('Price must be a positive integer.')


class Product(models.Model):
    title = models.CharField(max_length=80,verbose_name= 'عنوان')
    price = models.IntegerField(validators=[validate_positive],verbose_name='قیمت')
    slug = models.SlugField(blank=False,unique=True,db_index=True,verbose_name='عنوان در url')
    short_description = models.CharField(max_length=50,blank=True,verbose_name='توضیحات کوتاه محصول')
    description = models.TextField(max_length=300,blank=False,verbose_name='توضیحات محصول')

    def __str__(self):
        return f"{self.title}-{self.short_description}"

    def get_absloute_url(self):
        raise NotImplemented


