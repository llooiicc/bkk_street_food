from django.db import models

# Create your models here.

class Article(models.Model):
    
    titre = models.CharField(max_length=50)
    contenu = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    valide = models.BooleanField(default=False)
    
    
class Position(models.Model):
    
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    lat = models.FloatField()
    lng = models.FloatField()


class Commentaire(models.Model):
    
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    contenu = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    


