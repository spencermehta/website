from django.db import models
from django.shortcuts import reverse


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=[('y1', 'UG Year 1 Coursework'), ('y2', 'UG Year 2 coursework'), ('ind', 'Independent project')], default='y1')
    mark = models.IntegerField(blank=True, null=True)
    github = models.URLField()
    date = models.DateField()
    image = models.ImageField(upload_to='project_img/')
    icon = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse("project-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title
