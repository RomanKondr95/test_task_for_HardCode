from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User,on_delete = models.CASCADE)

class Lesson(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    duraton = models.IntegerField()
    products = models.ManyToManyField(Product,related_name='lessons')

class Access(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class LessonView(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE)
    time_viewed = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    
    def is_viewed(self):
        if (self.time_viewed/self.lesson.duraton) >= 0.8:
            self.status = True
        else:
            self.status = False

