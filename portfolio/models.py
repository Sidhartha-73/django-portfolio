
from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"


class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    technologies = models.CharField(max_length=250)
    image = models.ImageField(
        upload_to="projects/",
        blank=True,
        null=True,
    )
    project_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    live_demo_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
