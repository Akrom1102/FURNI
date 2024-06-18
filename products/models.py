from django.contrib.auth.models import User
from django.db import models
from .helps import SaveMediaFiles



class Users(models.Model):
    full_name = models.CharField(verbose_name='Full Name', max_length=100, null=True, blank=True)
    username = models.CharField(verbose_name='Username', max_length=100, unique=True)
    telegram_id = models.CharField(verbose_name='Telegram ID', unique=True)
    create_date = models.DateTimeField(auto_now_add=True)


class PriceType(models.TextChoices):
    EURO = 'EURO', 'EURO'
    DOLLAR = '$', '$'
    SUM = 'SO`M', 'SO`M'


class Product(models.Model):
    image = models.ImageField(upload_to=SaveMediaFiles.product_image_path)
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    price_type = models.CharField(max_length=4, choices=PriceType.choices)
    description = models.TextField()

    category_code = models.CharField(verbose_name='Kategoriya kodi', max_length=50, null=False, blank=False)
    category_name = models.CharField(verbose_name='Kategoriya nomi', max_length=20)
    subcategory_code = models.CharField(verbose_name='Ost-kategoriya-kodi', max_length=50, null=True, blank=True)
    subcategory_name = models.CharField(verbose_name='Ost-kategoriya-nomi', max_length=20)


    class Meta:
        ordering = ('id',)
        indexes = [
            models.Index(fields=['id'])
        ]

    def __str__(self):
        return self.name


class ClientComment(models.Model):
    image = models.ImageField(upload_to=SaveMediaFiles.clientcomment_image_path)
    name = models.CharField(max_length=150)
    comment = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('id',)
        indexes = [
            models.Index(fields=['id'])
        ]

    def __str__(self):
        return self.name


class TeamSays(models.Model):
    image = models.ImageField(upload_to=SaveMediaFiles.clientcomment_image_path)
    name = models.CharField(max_length=80)
    staff_type = models.CharField(max_length=150)
    title = models.CharField(max_length=80)

    class Meta:
        ordering = ('id',)
        indexes = [
            models.Index(fields=['id'])
        ]

    def __str__(self):
        return self.name


class Blog(models.Model):
    image = models.ImageField(upload_to=SaveMediaFiles.blog_image_path)
    name = models.CharField(max_length=150)
    by_who = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('id',)
        indexes = [
            models.Index(fields=['id'])
        ]

    def __str__(self):
        return self.name