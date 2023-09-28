from django.db import models

# Create your models here.
class Empresa(models.Model):
    nome = models.CharField(max_length= 50, help_text='Nome da empresa')


    def __str__(self):
        return self.nome

    class Meta:
        db_table = ''
        managed = True
        verbose_name =  'Empresa'
        verbose_name_plural =  'Empresas'