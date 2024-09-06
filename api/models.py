from typing import Any
from django.db import models
# CharField é um espaço para campos de texto curto, como o ano não vai ser usado paara nenhum calculo, não precisa usar o IntegerField, que é um campo para números inteiros.

class Movies(models.Model):                                 # FILMES
    title = models.CharField(max_length=255)                # TÍTULO
    genre = models.CharField(max_length=255)                # GENERO
    year = models.CharField(max_length=255)                 # ANO
    language = models.CharField(max_length=255)             # IDIOMA
    age_rating = models.CharField(max_length=255)           # CLASSIFICAÇÃO DE IDADE
    
class allGenre(models.Model):
    genre = models.CharField(max_length=255)
       