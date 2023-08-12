from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify


def validate_positive(value):
    if value <= 0:
        raise ValidationError('Price must be a positive integer.')


class Product(models.Model):
    title = models.CharField(max_length=80, verbose_name='عنوان')
    price = models.IntegerField(validators=[validate_positive], verbose_name='قیمت')
    slug = models.SlugField(blank=False, unique=True, db_index=True, verbose_name='عنوان در url')
    short_description = models.CharField(max_length=50, blank=True, verbose_name='توضیحات کوتاه محصول')
    description = models.TextField(max_length=300, blank=False, verbose_name='توضیحات محصول')
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],
                                              blank=True, null=True, verbose_name='امتیاز محصول')
    count = models.SmallIntegerField(verbose_name='تعداد محصول')
    is_active = models.BooleanField(default=True, blank=True, verbose_name='فعال و غیر فعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف شده یا نشده')
    categories = models.ManyToManyField('CategoryProduct', related_name='product_category',null=True, verbose_name='دسته بندی ها')

    def __str__(self):
        return f"{self.title}-{self.short_description}"

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def get_absolute_url(self):
           raise NotImplemented


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class CategoryProduct(models.Model):
    slug_url = models.CharField(max_length=100, null=False, verbose_name='url دسته بندی')
    title = models.CharField(max_length=40,default="", verbose_name='عنوان دسته بندی')
    is_active = models.BooleanField(default=True, verbose_name='فعال یا غیر فعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف شده یا نشده')

    def __str__(self):
        return f"({self.title})"

    def get_absolute_url(self):
           raise NotImplemented

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)




class BrandProduct(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_brand')
    title = models.CharField(max_length=50,verbose_name='عنوان')
    slug_url = models.SlugField(blank=False,db_index=True,verbose_name='عنوان درurl')

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
           raise NotImplemented

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)







