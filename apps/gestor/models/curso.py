from django.db import models
from django.utils import timezone

class Curso(models.Model):
    NIVEL_CHOICES = (
        ('TC', 'Técnico'),
        ('GR', 'Graduação'),
        ('PG', 'Pós-Graduação'),
        ('EX', 'Extensão'),
    )
    nome = models.CharField(max_length=100)  # Nome do curso
    nivel = models.CharField(max_length=2, choices=NIVEL_CHOICES)  # Nível acadêmico
    data_criacao = models.DateField(default=timezone.now)  # Data de criação do curso

    def __str__(self):
        return f'({self.id}) {self.nome} ({self.get_nivel_display()})'