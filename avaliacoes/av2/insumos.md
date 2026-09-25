# Insumos de AV2 — proposta isolada de visibilidade

**Origem:** contrato e artefatos didáticos fictícios de Fila Clara. O candidato e o texto abaixo foram escritos para esta avaliação; não são resultados de consulta a modelo real. Sua tarefa é avaliar a proposta, sem presumir que ela esteja correta ou incorreta. [Enunciado](README.md).

## Contrato de referência

- **R3:** `pode_visualizar` permite acesso somente à pessoa do mesmo departamento do chamado, independentemente de estado ou prioridade.
- **R4:** a documentação deve descrever o mesmo comportamento do contrato; código, teste e texto precisam ser confrontados com ele.
- Entradas são válidas. Os departamentos são Oficina e Laboratório; os estados são `aberto`, `em_andamento` e `fechado`; impacto e urgência são inteiros de 1 a 3. O contrato completo está em [regras do caso](../../caso/regras.md).

Não há autenticação real, API, persistência ou dado pessoal no escopo. Não é necessário implementar validação de entradas externas.

## Candidato de código

```python
def pode_visualizar_proposta(chamado, departamento):
    return (
        chamado["departamento"] == departamento
        and chamado["estado"] != "fechado"
    )
```

Este trecho é independente de `caso/fila_clara.py`. Se optar por executar, copie somente esta função e seus casos para um arquivo ou ambiente local separado. Python com biblioteca padrão basta; não altere o kit e não há dependência de rede.

## Documentação candidata — texto fictício

> A função permite que uma pessoa visualize chamados ativos de seu próprio departamento. Chamados abertos ou em andamento ficam disponíveis para o departamento correspondente; chamados fechados ficam indisponíveis. Chamados de outros departamentos não são exibidos. Impacto e urgência não alteram essa decisão.

## Dados disponíveis para construir a matriz

| id | departamento | estado | impacto | urgencia |
|---|---|---|---:|---:|
| V-01 | Oficina | aberto | 1 | 1 |
| V-02 | Oficina | fechado | 1 | 1 |
| V-03 | Laboratório | aberto | 3 | 3 |
| V-04 | Laboratório | fechado | 3 | 3 |

Você pode usar o departamento solicitante `Oficina` nos quatro casos acima ou construir casos equivalentes com entradas válidas. Declare a escolha. Os dados permitem cruzar os dois eixos exigidos sem buscar informações externas. Casos adicionais são opcionais, dentro do mesmo tempo e limite de páginas.

## Duas vias de verificação

**Por inspeção:** avalie cada comparação do código, registre o retorno inferido e explique a combinação lógica. A saída esperada vem de R3. Preencha a matriz do template sem afirmar que executou.

**Por execução opcional:** construa cada dicionário com os campos fornecidos, invoque `pode_visualizar_proposta(chamado, "Oficina")` e registre o retorno. Inclua comando/ambiente e apenas o trecho essencial de saída no anexo. O retorno executado é observado; a previsão anterior e a análise da documentação continuam identificadas separadamente.

As duas vias usam a mesma rubrica. Não são fornecidos resultados prontos de referência ou uma decisão de aceite: a comparação e o parecer fazem parte da avaliação.
