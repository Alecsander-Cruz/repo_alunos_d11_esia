def pode_visualizar_proposta(chamado, departamento):
    return (
        chamado["departamento"] == departamento
        and chamado["estado"] != "fechado"
    )


def pode_visualizar_ajustada(chamado, departamento):
    return chamado["departamento"] == departamento


casos = [
    ("T1", {"id": "V-01", "departamento": "Oficina", "estado": "aberto", "impacto": 1, "urgencia": 1}),
    ("T2", {"id": "V-02", "departamento": "Oficina", "estado": "fechado", "impacto": 1, "urgencia": 1}),
    ("T3", {"id": "V-03", "departamento": "Laboratório", "estado": "aberto", "impacto": 3, "urgencia": 3}),
    ("T4", {"id": "V-04", "departamento": "Laboratório", "estado": "fechado", "impacto": 3, "urgencia": 3}),
]
solicitante = "Oficina"
for nome, chamado in casos:
    print(nome, chamado["id"], solicitante,
          "candidato:", pode_visualizar_proposta(chamado, solicitante),
          "ajustada:", pode_visualizar_ajustada(chamado, solicitante))
