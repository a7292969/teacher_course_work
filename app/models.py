from django.db import models


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=50)
    text = models.CharField(max_length=500)

    def __str__(self) -> str:
        return f"{self.author} {self.text}"
