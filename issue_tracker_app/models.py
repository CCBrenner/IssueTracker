from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# from django.urls import reverse


class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Issue(models.Model):
    parent_project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    content = models.TextField()
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='creator')
    worker = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='worker')

    PRIORITY_CHOICES = [
        ('-', '-'),
        ('P1', 'P1'),
        ('P2', 'P2'),
        ('P3', 'P3'),
        ('P4', 'P4'),
        ('P5', 'P5')
    ]
    priority = models.CharField(
        max_length=2,
        choices=PRIORITY_CHOICES,
        default='-'
    )

    STATUS_CHOICES = [
        ('To Do', 'To Do'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done')
    ]
    status = models.CharField(
        max_length=11,
        choices=STATUS_CHOICES,
        default='To Do'
    )

    DIFFICULTY_CHOICES = [
        ('-', '-'),
        ('2', '2'),
        ('3', '3'),
        ('5', '5'),
        ('8', '8'),
        ('13', '13'),
        ('21', '21'),
        ('34', '34'),
        ('55', '55')
    ]
    difficulty = models.CharField(
        max_length=2,
        choices=DIFFICULTY_CHOICES,
        default='-'
    )

    def __str__(self):
        return self.title
