# ────────────────────────────────────────────────────────────────
# 1) IMPORTS
# ────────────────────────────────────────────────────────────────
import random
from itertools import count
from faker import Faker
from django.db import transaction               
from apps.gestor.models.aluno import Aluno
from apps.gestor.models.curso import Curso

fake = Faker("pt_BR")
matriculas = count(start=202500001)                

# ────────────────────────────────────────────────────────────────
# 2) LISTA DE CURSOS DE REFERÊNCIA
# ────────────────────────────────────────────────────────────────
CURSOS_PADRAO = [
    {"nome": "Engenharia Civil",          "nivel": "GR"},
    {"nome": "Engenharia de Software",    "nivel": "GR"},
    {"nome": "Administração",             "nivel": "GR"},
    {"nome": "Direito",                   "nivel": "GR"},
    {"nome": "Ciência da Computação",     "nivel": "GR"},
    {"nome": "Medicina",                  "nivel": "GR"},
    {"nome": "Data Science",              "nivel": "PG"},
    {"nome": "Gestão de Projetos",        "nivel": "PG"},
    {"nome": "Engenharia Elétrica",       "nivel": "PG"},
    {"nome": "Inteligência Artificial",   "nivel": "PG"},
    {"nome": "Marketing Digital",         "nivel": "EX"},
    {"nome": "Fotografia",                "nivel": "EX"},
    {"nome": "Design de Jogos",           "nivel": "EX"},
    {"nome": "Finanças Pessoais",         "nivel": "EX"},
    {"nome": "Inglês para Negócios",      "nivel": "EX"},
]

# ────────────────────────────────────────────────────────────────
# 3) CRIA ALUNOS VINCULANDO AO CURSO
# ────────────────────────────────────────────────────────────────
curso_objs = {}
for data in CURSOS_PADRAO:
    curso, _created = Curso.objects.get_or_create(nome=data["nome"], defaults=data)
    curso_objs[curso.nome] = curso
print(f"✔︎  Total de cursos disponíveis: {Curso.objects.count()}")

# ────────────────────────────────────────────────────────────────
# 4) GERA ALUNOS (20–40 POR CURSO)
# ────────────────────────────────────────────────────────────────
total_alunos_criados = 0
with transaction.atomic():                       
    for curso in curso_objs.values():
        qtd = random.randint(20, 60)
        alunos_novos = [
            Aluno(
                nome=fake.name(),
                matricula=str(next(matriculas)),
                curso=curso
            )
            for _ in range(qtd)
        ]
        Aluno.objects.bulk_create(alunos_novos, batch_size=1000)
        print(f"   • {qtd:2d} alunos para {curso.nome}")
        total_alunos_criados += qtd

print(f"\n🎉  Total de alunos criados: {total_alunos_criados}")
