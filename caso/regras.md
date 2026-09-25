# Fila Clara — cenário e contrato

Fila Clara é uma organização fictícia que mantém chamados internos de duas áreas: Oficina e Laboratório. A equipe quer experimentar apoio de IA para compreender regras, propor testes, revisar código e documentar mudanças. Resultados plausíveis precisam de evidências antes de uma decisão de uso.

O caso acompanha as seis aulas da disciplina D1.1. Seu código curto serve à análise do trabalho de engenharia: ler um requisito, verificar um artefato, registrar uma decisão e identificar o que a evidência ainda não permite concluir.

| Regra | Comportamento esperado |
|---|---|
| R1 — prioridade | `impacto` e `urgencia` são inteiros de 1 a 3. O escore é a soma. Escore maior ou igual a 5 produz `alta`; maior ou igual a 3 e menor que 5 produz `media`; menor que 3 produz `baixa`. |
| R2 — chamados ativos | `listar_ativos` inclui os estados `aberto` e `em_andamento`, exclui `fechado` e preserva a ordem de entrada. |
| R3 — visibilidade | `pode_visualizar` permite acesso somente à pessoa do mesmo departamento do chamado, independentemente de estado ou prioridade. Os nomes de departamentos vêm dos dados controlados do caso. |
| R4 — documentação | A documentação descreve essas mesmas regras. Teste e texto gerados com apoio de IA precisam ser confrontados com este contrato. |

As funções são `prioridade(impacto, urgencia)`, `listar_ativos(chamados)` e `pode_visualizar(chamado, departamento)`. A prioridade é calculada; os registros contêm somente `id`, `departamento`, `estado`, `impacto` e `urgencia`. A grafia de saída `media` não usa acento.

## Escopo

As entradas são válidas e pertencem ao conjunto fictício conhecido. Validação de entradas externas é uma lacuna para discussão, não um requisito oculto. Não há banco de dados, autenticação real, API, dados pessoais ou persistência. A decisão de visibilidade é uma regra didática; não constitui um sistema de segurança pronto para uso.

Todos os registros de [chamados.json](chamados.json) são sintéticos. O contrato é a referência para comparar implementação, documentação e resultados dos testes.
