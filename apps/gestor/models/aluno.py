from django.db import models
from django.utils import timezone
from apps.gestor.models.curso import Curso

class Aluno(models.Model):
    nome = models.CharField(max_length=150)  # Nome completo do aluno
    matricula = models.CharField(max_length=20, unique=True)  # Matrícula única
    curso = models.ForeignKey(Curso, on_delete=models.RESTRICT, related_name='alunos')  # Curso do aluno

    def __str__(self):
        return f'{self.nome} - Matrícula: {self.matricula}'