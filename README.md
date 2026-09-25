# Fila Clara — apoio à disciplina D1.1

Este pacote apoia as seis aulas de **Engenharia de Software na Era da IA Generativa (24h)**. Fila Clara é um caso fictício de chamados internos. Alguns exercícios contêm código legado a ser corrigido. As decisões e sua verificação são o foco da disciplina.

O caso e suas verificações já podem ser executados. O professor conduz as demonstrações; em B3, há também [25min de execução acompanhada](apoio/execucao-acompanhada-b3.md) no próprio ambiente, sem entrega ou nota. Cada bloco reserva 35min a um desafio avaliativo individual com consulta; as instruções indicam insumos próprios, entregável e rubrica. Não há entrega coletiva ou síntese adicional obrigatória.

## Preparação do ambiente

Obtenha o pacote disponibilizado pelo professor e abra esta pasta. A execução local usa Python e sua biblioteca padrão; o ambiente de preparação foi verificado com **Python 3.13.3**. Não há dependências adicionais. Um assistente de IA no navegador pode apoiar as práticas; não é necessário contratar API. O caminho textual usa os materiais de `apoio/` quando não houver acesso à ferramenta ou ao ambiente local. A instalação local não é condição para demonstrar os objetivos da disciplina.

## Navegação

| Pasta | Conteúdo |
|---|---|
| `caso/` | Cenário, regras, dados sintéticos e funções pequenas |
| `testes/` | Verificações reproduzíveis do caso |
| `apoio/` | Respostas simuladas identificadas e transcrição de execução |
| `exercicios/aula-1/` a `aula-6/` | Instruções e registros de cada aula |

## Fluxo de trabalho

Desafios AV1: [B1 — delegação](exercicios/aula-1/README.md) · [B2 — contexto](exercicios/aula-2/README.md) · [B3 — ciclo de desenvolvimento](exercicios/aula-3/README.md) · [B4 — verificação](exercicios/aula-4/README.md) · [B5 — política de uso](exercicios/aula-5/README.md) · [B6 — maturidade](exercicios/aula-6/README.md).

1. Leia a atividade da aula e o contrato do caso.
2. Registre sua modalidade: execução própria, transcrição verificada ou simulação.
3. Inspecione o artefato, registre decisões e execute as verificações quando aplicável.
4. Entregue a evidência solicitada no canal informado pelo professor, declarando a assistência utilizada.

Execute nesta pasta:

```text
python -B testes/test_fila_clara.py --codigo caso/fila_clara.py
```

Há nove verificações. No material inicial, seis passam e três apontam divergências em relação ao contrato. O processo retorna código de saída `1` quando há falha e `0` quando todas as verificações passam. Esses testes verificam o material e não atribuem nota ao aluno. Uma execução verde se limita ao que foi testado; documentação e decisões exigem revisão.

Consulte [testes/README.md](testes/README.md) para executar uma verificação isolada e [apoio/resultado-textual.md](apoio/resultado-textual.md) para ler a transcrição de uma execução. Utilize apenas os dados fictícios fornecidos.

## Avaliações da pós-graduação

- [Índice dos enunciados e modelos: AV1, AV2 e AV3](avaliacoes/README.md)
- [AV2 — estudo técnico de verificação](avaliacoes/av2/README.md)
- [AV3 — parecer integrador fundamentado](avaliacoes/av3/README.md)

Composição: AV1 20% (média dos desafios dos blocos com presença), AV2 30%, AV3 50%. As 6h autônomas são leitura L0 2h + AV2 2h + AV3 2h. AV3 aplica duas referências já lidas à decisão sobre o caso. As rubricas avaliam aplicação, evidência e argumentação individuais.

## Documentos da disciplina

- [Plano de ensino da turma](ementa.md)

- [Boas-vindas e preparação](boas-vindas.md)
- [Avaliação e critérios](avaliacao.md)
- [Estudo autônomo e prazos](estudo-autonomo.md)
- [Glossário](glossario.md)
- [Diagnóstico sem nota](diagnostico.md)

Datas: 25–26/09 e 02–03/10/2026. As aulas e entregas usam horário de Brasília. O pacote funciona localmente e o canal acadêmico de envio será informado pelo professor.
