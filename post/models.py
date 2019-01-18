from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=124)
    content = models.TextField()
    timesstamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entry"
        ordering = ["-timesstamp"]