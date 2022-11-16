from django.db import models

class Blog(models.Model):
    title=models.CharField(max_length=15, null=True, blank=True)
    summary=models.CharField(max_length=15, null=True, blank=True)
    topic=models.TextField(max_length=300, blank=True, null=True)
    posted=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Blog'
        verbose_name_plural='Blog'
        ordering=['-posted',]

    def __str__(self):
        return self.title    
