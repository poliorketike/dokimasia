---
type: Claim
title: "Conhecimento que não pode cair não é conhecimento"
description: "A tese central da casa, e a única regra da qual todas as outras derivam. Declarada como tese, não como fato: ver `refutes`."
tags: [epistemologia, tese-central, refutabilidade]
okf_version: "0.2"
generated: { by: claude-opus-5/anthropic, at: 2026-10-02T00:00:00Z }
status: proposto
sources:
  - id: popper
    resource: "Popper, K. — The Logic of Scientific Discovery (1959)"
    title: "O critério de demarcação: a falsificabilidade"
    author: human:popper
  - id: elenchos
    resource: "Platão — os diálogos socráticos aporéticos"
    title: "ἔλεγχος: a refutação como método, não como derrota"
    author: human:platao
relations:
  extends:
    - okf/02-lei-do-portao.md
  converges:
    - okf/04-o-experimento.md
refutes: >
  Esta página cai se for exibida uma página do corpus que (a) não declare condição de queda,
  (b) tenha sido admitida assim mesmo, e (c) tenha se mostrado útil ao longo de ≥3 ondas de
  trabalho. Nesse caso a regra estaria rejeitando conhecimento real, e o custo do portão superaria
  o benefício.
---

# A tese

> **Conhecimento que não pode cair não é conhecimento: é decoração.**

Uma afirmação que nenhum observação possível contradiria não está informando nada sobre o mundo —
está informando sobre quem a escreveu. Num sistema multiagente isso é agudo: o modelo produz texto
fluente com a mesma facilidade com que produz texto verdadeiro, e **a fluência não distingue os
dois**.

Daí a exigência operacional: toda página declara, no campo `refutes`, **o que a derrubaria**. Não
"quais são as limitações" — isso é retórica. Uma condição *observável* que, se ocorrer, obriga a
revisão.

## O que esta tese não afirma

Que o sistema que a aplica **funciona melhor**. Essa é outra afirmação, de outra natureza, e ela
está em `okf/04-o-experimento.md` — **não verificada**, com o motivo dito.

## A classe de erro que isto não pega

Uma, e é a mais perigosa: **a conclusão vestida de achado** — uma frase com a forma de uma medida e
a confiança de uma, que não é nenhuma das duas. O portão confere se há `refutes`; não confere se o
número ao lado foi medido ou imaginado. Essa classe só cai por revisão adversarial, e por isso a
revisão é obrigatória e **tem de vir de outra família de modelo**.
