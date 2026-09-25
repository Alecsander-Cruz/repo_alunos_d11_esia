"""Caso Fila Clara: entradas válidas do conjunto fictício."""


def prioridade(impacto: int, urgencia: int) -> str:
    """Classificar o chamado pela soma de impacto e urgência."""
    escore = impacto + urgencia
    if escore > 5:
        return "alta"
    if escore >= 3:
        return "media"
    return "baixa"


def listar_ativos(chamados: list[dict]) -> list[dict]:
    """Selecionar chamados ativos na ordem de entrada."""
    return [chamado for chamado in chamados if chamado["estado"] == "aberto"]


def pode_visualizar(chamado: dict, departamento: str) -> bool:
    """Decidir se a pessoa do departamento pode visualizar o chamado."""
    return chamado["departamento"] == departamento or chamado["impacto"] + chamado["urgencia"] >= 5
