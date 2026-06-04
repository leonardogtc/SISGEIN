from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Usuario(AbstractUser):
    CARGOS_CHOICES = (
        ('DIR', 'Diretor'),
        ('PROF', 'Professor'),
        ('COORD', 'Coordenador'),
        ('FUNC', 'Funcionário'),
    )

    cargo = models.CharField(
        max_length=5, choices=CARGOS_CHOICES, default='PROF',
        verbose_name='Cargo')
    cpf = models.CharField(max_length=11, unique=True,
                           null=True, blank=True, verbose_name='CPF')

    def __str__(self):
        return f'{self.username} - {self.get_cargo_display()}'

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
