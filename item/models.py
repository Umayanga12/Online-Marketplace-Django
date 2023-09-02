from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    # can add option for the model
    class Meta:
        # iterable item - sorting the rows
        ordering = ('name',)
        verbose_name_plural = 'catogries'

    def __str__(self):
        return self.name


# creating the item db model
class items(models.Model):
    # adding the frogine key of the category
    item_cat = models.ForeignKey(Category, related_name='item', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    # accepting the null and blank values
    discription = models.TextField(blank=True, null=True)
    # creating the field to upload the images
    item_img = models.ImageField(upload_to='item_image', blank=True, null=True)
    price = models.FloatField()
    is_sold = models.BooleanField(default=False)
    # adding the frogine key of the user
    created_by = models.ForeignKey(User, related_name='item', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    # can add option for the model
    class Meta:
        # iterable item - sorting the rows
        ordering = ('name',)
        verbose_name_plural = 'items'

    def __str__(self):
        return self.name
