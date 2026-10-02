---
type: Project
title: "O experimento em curso, e a tese que ele ainda não verificou"
description: "O estado real do laboratório em 2026-10-02: o que foi construído, o que foi medido, e por que a tese central permanece NÃO VERIFICADA."
tags: [experimento, em-curso, gargalos, g4]
okf_version: "0.2"
generated: { by: claude-opus-5/anthropic, at: 2026-10-02T00:00:00Z }
status: proposto
sources:
  - id: git
    resource: "git rev-list --all --count · gh pr list · wc -l — nos quatro repositórios, 2026-10-02"
    title: "1.040 commits, 172 PRs, 202 páginas, 420 ligações"
    author: machine:medicao-local
  - id: cronologia
    resource: "~/.claude/history.jsonl, re-derivado em 2026-10-02"
    title: "9.323 prompts em 142 dias corridos, 119 deles ativos"
    author: machine:medicao-local
relations:
  extends:
    - okf/01-tese-conhecimento-refutavel.md
  contradicts:
    - "a leitura de que volume de commits demonstra ganho de capacidade"
refutes: >
  Esta página cai no dia em que existir uma medida de capacidade antes-e-depois — um conjunto de
  tarefas de dificuldade conhecida, resolvido com e sem o corpus, por operadores comparáveis. Nesse
  dia, ou a tese central passa a ser VERIFICADA, ou passa a ser REFUTADA. Hoje ela não é nenhuma
  das duas, e é isso que esta página existe para declarar.
---

# O que existe

Quatro repositórios, ainda privados: o método (`verbum`), a pesquisa sob cerco
(`poliorketikos`), o reino do que foi admitido (`regnum`) e o console que revela (`phanes`).
**1.040 commits, 172 PRs, 292 testes, 13 portões de CI, 202 páginas com 420 ligações tipadas.**

O operador: **9.323 prompts em 142 dias corridos**, com atividade em 119 deles — e a curva não tem
manhã: a madrugada é mais densa que o período das 6h às 11h.

# O que foi medido

Coisas pequenas e verificáveis. Que o grafo tem 27 páginas ilhadas e **24 alvos fantasmas** —
citações para o que não existe neste repositório, contadas na cara. Que a razão de revisão é de
1 PR a cada 6 commits. Que o módulo audiovisual passou de 1.341 ms para 403 ms por giro depois de
cinco rodadas de medição com `Performance.getMetrics`.

# O que **não** foi medido, e é o que importa

> **G4 · Não há ground truth de aprendizagem.**

Nenhuma medida de capacidade antes e depois. Enquanto não houver, a tese de que este arranjo
**amplifica** o trabalho — e não apenas o acelera — permanece **não verificada**. E nenhuma das
coisas acima substitui essa medida:

- volume de commits mede atividade, não ganho;
- fluência de sessão mede fluência, e tomá-la por prova é o segundo risco cognitivo da lista desta
  casa;
- satisfação do operador é `DECLARADO_PELO_AUTOR` — vale como dado, não como medição.

# Os outros cinco gargalos, declarados

| # | gargalo | mecanismo em curso |
|---|---|---|
| 1 | convergência cara: cada reenvio chega com **+13 palavras** | porteiro com gate de entendimento |
| 2 | coordenação entre sessões | registro de onda, cristalização |
| 3 | estimativas do agente aceitas sem verificação | previsões com Brier |
| 4 | **revisores todos da mesma família de modelo** | um membro de outra família, obrigatório |
| 5 | segredo colado no prompt sob urgência | hook que **bloqueia**, não avisa |
| 6 | **G4 — nenhum ground truth** | *não há mecanismo. É a próxima coisa a construir.* |

A linha 6 está vazia de propósito. **A casa vazia é o achado** — é a mesma regra do tabuleiro do
cerco, aplicada à própria casa.
