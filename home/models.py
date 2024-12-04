from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model) :
    sun_category=models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='sub')
    sub_cat=models.BooleanField(default=False)

    name = models.CharField(max_length=100)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(allow_unicode=True , unique=True,blank=True , null=True)
    image = models.ImageField(upload_to='Category',null=True,blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return  reverse('home:category', args=[self.slug, self.id])



class Product(models.Model) :
    category = models.ManyToManyField(Category,blank=True)
    name = models.CharField(max_length=100)
    amount = models.PositiveSmallIntegerField()
    unit_price = models.PositiveIntegerField()
    discount = models.PositiveSmallIntegerField(blank=True , null=True)
    total_price = models.PositiveIntegerField()
    information = models.TextField(blank=True , null=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='Product')

    def __str__(self):
        return self.name

    @property
    def total_price(self):
        if not self.discount :
            return self.unit_price
        elif self.discount :
            total = (self.discount * self.unit_price) / 100
            return int(self.unit_price - total)
        return self.total_price






