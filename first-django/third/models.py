from django.db import models

# Create your models here.


class Restaurand(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)

    image = models.CharField(max_length=500, default=None, null=True)
    password = models.CharField(max_length=20, default=None, null=True)
# 기존 모델에 column 추가

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Review(models.Model):
    point = models.IntegerField()
    comment = models.CharField(max_length=500)

    restaurant = models.ForeignKey(Restaurand, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)