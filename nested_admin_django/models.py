from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField()

    def __str__(self):
        return f'{self.id}'

class Attachment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
    like = models.IntegerField()

class StatusEmot(models.Model):
    attachment = models.ForeignKey(Attachment, on_delete=models.CASCADE, null=True, blank=True)
    emot = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.emot}'