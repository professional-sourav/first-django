from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name = models.CharField(max_length=200)
    created_at = models.DateTimeField("Date Created", auto_now_add=True)

    def __str__(self):
        return self.topic_name

class Thread(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    content = models.TextField()
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.topic}: {self.content}"