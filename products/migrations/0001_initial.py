# Generated by Django 4.2.4 on 2023-08-11 14:11

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug_url', models.CharField(max_length=100, verbose_name='url دسته بندی')),
                ('title', models.CharField(default='', max_length=40, verbose_name='عنوان دسته بندی')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال یا غیر فعال')),
                ('is_delete', models.BooleanField(default=False, verbose_name='حذف شده یا نشده')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='عنوان')),
                ('price', models.IntegerField(validators=[products.models.validate_positive], verbose_name='قیمت')),
                ('slug', models.SlugField(unique=True, verbose_name='عنوان در url')),
                ('short_description', models.CharField(blank=True, max_length=50, verbose_name='توضیحات کوتاه محصول')),
                ('description', models.TextField(max_length=300, verbose_name='توضیحات محصول')),
                ('rating', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='امتیاز محصول')),
                ('count', models.SmallIntegerField(verbose_name='تعداد محصول')),
                ('is_active', models.BooleanField(blank=True, default=True, verbose_name='فعال و غیر فعال')),
                ('is_delete', models.BooleanField(default=False, verbose_name='حذف شده یا نشده')),
                ('categories', models.ManyToManyField(related_name='product_category', to='products.categoryproduct', verbose_name='دسته بندی ها')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
            },
        ),
        migrations.CreateModel(
            name='BrandProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('slug_url', models.SlugField(verbose_name='عنوان درurl')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_brand', to='products.product')),
            ],
        ),
    ]
