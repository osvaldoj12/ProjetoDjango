# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

#Tinha mais classes conectando a outras tabelas, mais apaguei para entender melhor
class Sugestoes(models.Model):
  
    titulo = models.CharField(max_length=30, blank=True, null=True)
    comentarios = models.CharField(max_length=300)
    def __str__(self):
        return self.titulo
        
    #Essa classe vai ser salvo na tabela sugestoes 
    class Meta:
        db_table = 'sugestoes'

