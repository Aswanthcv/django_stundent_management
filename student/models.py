from django.db import models

# Create your models here.

STATUS_CHOICES = (
  ('Mern stack','Mern stack'),
  ('Python stack','Python stack'),
  ('Spring boot','Spring boot')
)

class Students(models.Model):
  name = models.CharField(max_length=30)
  email = models.EmailField(max_length=30,unique=True)
  course = models.CharField(max_length=20,choices=STATUS_CHOICES)