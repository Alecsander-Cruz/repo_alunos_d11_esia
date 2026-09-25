# Seis saídas didáticas simuladas — experimento de B2

**SIMULAÇÃO DIDÁTICA: os seis textos abaixo foram redigidos para análise em aula. Não foram coletados de um modelo real. Não informam taxa de erro, velocidade, custo ou desempenho de qualquer fornecedor.** A numeração identifica exemplos; não representa uma sequência observada de chamadas.

## Tarefa comum e protocolo

A tarefa é classificar prioridade de três registros fictícios: FC-001, impacto 1 e urgência 1; FC-002, impacto 2 e urgência 3; FC-004, impacto 2 e urgência 2. Estados e departamentos não participam desta tarefa de classificação.

No caminho com modelo, o professor registra o critério de aceitação antes das tentativas, executa três repetições por condição em sessões novas, mantém a tarefa e a interface/modelo constantes quando identificáveis e registra as condições visíveis. As instruções abaixo orientam a demonstração. Se acesso, cota ou tempo impedirem completar as seis respostas, usar o conjunto simulado completo e manter eventuais respostas reais separadas. A ordem A/B e mudanças ocultas do produto limitam a comparação: esta é uma observação exploratória pequena.

No caminho textual, analisar estes seis exemplos contra o contrato do caso e descrever como o experimento seria executado. Ferramenta/modelo, tokens, custo e latência ficam como **não aplicável — simulação**, sem números inventados. Em ambos os caminhos, respostas iguais são aceitas como resultado; não é preciso produzir dispersão.

## Condição A — sem contrato de prioridade

Instrução comum A:

```text
Classificar os registros em alta, media ou baixa e explicar o critério usado:
FC-001: impacto 1, urgencia 1.
FC-002: impacto 2, urgencia 3.
FC-004: impacto 2, urgencia 2.
Os valores vão de 1 a 3.
```

### A1 — exemplo simulado

FC-001: baixa. FC-002: alta. FC-004: alta. Usei alta sempre que impacto e urgência forem pelo menos 2; os dois fatores já tornam o chamado relevante.

### A2 — exemplo simulado

FC-001: baixa. FC-002: alta. FC-004: media. Somei impacto e urgência e adotei os cortes 5 para alta e 3 para media. Esses cortes são uma hipótese minha, pois não foram informados na tarefa.

### A3 — exemplo simulado

Não há regra suficiente para atribuir as prioridades com segurança. Consigo informar as somas 2, 5 e 4, respectivamente. A classificação depende dos limites definidos pela organização; preciso desse contrato para concluir.

## Condição B — com contrato de prioridade

Instrução comum B: a mesma entrada A, acrescida de:

```text
Contrato R1: escore = impacto + urgencia.
Se escore >= 5, prioridade alta.
Se 3 <= escore < 5, prioridade media.
Se escore < 3, prioridade baixa.
O contrato é a referência. Não criar exceções.
```

### B1 — exemplo simulado

FC-001: escore 2, baixa. FC-002: escore 5, alta. FC-004: escore 4, media. A classificação usa os limites informados no contrato.

### B2 — exemplo simulado

| Registro | Soma | Prioridade |
|---|---:|---|
| FC-001 | 2 | baixa |
| FC-002 | 5 | alta |
| FC-004 | 4 | media |

Não usei departamento ou estado para calcular a prioridade.

### B3 — exemplo simulado

FC-001: baixa. FC-002: media. FC-004: media. Interpretei prioridade alta como escore maior que 5, preservando o limite para os casos mais graves.

## Registro de análise

Para cada saída, registrar: atende ao contrato? Há hipótese inventada, informação faltante ou conflito? A explicação permite conferir o resultado? Que intervenção seria necessária? Uma resposta que coincide com o esperado por uma hipótese não informada merece a mesma confiança que uma resposta ancorada no contrato?

Os exemplos servem para discutir hipóteses e verificação. A comparação desta coleção artificial não demonstra que contexto aumente a qualidade em determinada porcentagem nem estima o comportamento de um modelo.
