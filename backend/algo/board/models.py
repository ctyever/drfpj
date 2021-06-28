from django.db import models


class Post(models.Model):
    Title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'posts'
