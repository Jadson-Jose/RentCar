from celery import shared_task
from cars.models import Car
from decimal import Decimal
from cars.services.fipe_api import consultar_preco_parallelum


@shared_task
def atualizar_precos_fipe():
    atualizados = 0
    for carro in Car.objects.all():
        if carro.marca_id and carro.modelo_id and carro.ano_codigo:
            preco = consultar_preco_parallelum(carro.marca_id, carro.modelo_id, carro.ano_codigo)
            if preco:
                carro.save()
                atualizados += 1
    return f"{atualizados} carros atualizados com preço da Tabela Fipe"

