from django.db import models

# Create your models here.

class Utilisateur(models.Model):
    
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField()
    derniere_connexion = models.DateTimeField(auto_now_add=True)
    
    