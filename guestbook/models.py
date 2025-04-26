from django.db import models

class Guestbook(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=10)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return f"[{self.title}] {self.name}"

