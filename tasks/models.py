from django.db import models
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255,db_index=True)
    def __str__(self):
        return self.title



class Task(models.Model):
    PRIORITY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    )
    STATUS_CHOICES = (
        ('pending', 'pending'),
        ('completed', 'completed'),

    )
    title = models.CharField(max_length=255,db_index=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending',
    )
    priority = models.CharField(
        max_length=6,
        choices=PRIORITY_CHOICES,
        default='medium',
    )
    description = models.CharField(max_length=255)
    due_date = models.DateField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    def __str__(self):
        return self.title