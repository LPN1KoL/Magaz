from django.contrib.auth.models import AbstractUser
from django.db import models




class Tag(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Category(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.PositiveIntegerField
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to='media/products_images')
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def to_json(self):
        return {'name': self.name, 'price': self.price, 'id': self.id, 'tags': self.tags, 'image': self.image.url, 'categories': self.categories}

class Basket(models.Model):
    products = models.ManyToManyField(Product)
    price = models.PositiveIntegerField


    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class Role(models.Model):
    name = models.CharField(max_length=300)
    admin_access = models.BooleanField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'



class User(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, verbose_name='Роль', null=True)
    basket = models.OneToOneField(to=Basket, on_delete=models.SET_NULL, null=True)



    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class Order(models.Model):
    date = models.DateField
    city = models.CharField(max_length=300, null=True)
    price = models.PositiveIntegerField
    products = models.ManyToManyField(Product)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)


    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'





