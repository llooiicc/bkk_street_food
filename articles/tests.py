from django.test import TestCase
from articles.models import *


# Create your tests here.

class ArticleTestCase(TestCase):
    
    def setup(self):
        Article.objects.create(titre="t1", contenu="contenu 1")
        Article.objects.create(titre="t2", contenu="contenu 2")
        Article.objects.create(titre="t3", contenu="contenu 3")

    def read(self):
        
        art_1 = Article.objects.filter(titre="t1")
        art_2 = Article.objects.filter(titre="t2")
        art_3 = Article.objects.filter(titre="t3")
        
        self.assertEqual(1, len(art_1))
        self.assertEqual(1, len(art_2))
        self.assertEqual(1, len(art_3))
        