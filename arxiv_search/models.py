from django.db import models

class Paper(models.Model):
    arxiv_id = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=500)
    summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title