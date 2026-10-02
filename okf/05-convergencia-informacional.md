---
type: Pattern
title: "Convergência informacional: um paga a anatomia, muitos operam"
description: "A doutrina que liga a pesquisa ao operacional. Em vez de N agentes pagarem N vezes o custo de entender a anatomia de um módulo, um κατάσκοπος paga uma vez e produz a ἀνατομή; os demais reivindicam tarefas e operam. Com a conta, e com o risco que a conta esconde."
tags: [operacional, convergencia, custo-de-contexto, anatomia, kataskopos]
okf_version: "0.2"
generated: { by: claude-opus-5/anthropic, at: 2026-10-02T00:00:00Z }
status: proposto
sources:
  - id: entrada
    resource: "~/.claude/projects/*/*.jsonl — primeiro turno com `usage` de cada sessão, 2026-10-02"
    title: "2.333 sessões · mediana de 28.671 tokens de contexto ANTES do primeiro trabalho útil · 84,0 M somados"
    author: machine:medicao-local
  - id: kataskopos
    resource: "Tucídides; Xenofonte — o κατάσκοπος enviado antes da operação"
    title: "O batedor: quem levanta o terreno uma vez, para a força não o levantar N vezes"
    author: human:tucidides
  - id: brooks
    resource: "Brooks, F. — The Mythical Man-Month (1975)"
    title: "O custo de comunicação cresce com n(n−1)/2; acrescentar gente a um projeto atrasado o atrasa mais"
    author: human:brooks
relations:
  extends:
    - okf/02-lei-do-portao.md
  converges:
    - okf/04-o-experimento.md
  contradicts:
    - "a leitura de que paralelizar agentes é sempre mais barato que serializar"
refutes: >
  Esta página cai se, num módulo com ≥10 tarefas, a execução a partir da ἀνατομή produzir MAIS
  defeitos por tarefa do que a execução com leitura integral da fonte — medido por revisão cega,
  com o mesmo gabarito nos dois braços. Nesse caso a compressão estaria custando mais em erro do
  que economizando em contexto, e a doutrina estaria errada no sinal.
---

# O problema, com a conta

Um módulo complexo tem 30 tarefas. Cada uma exige **entender a anatomia** antes de poder operar:
onde as coisas estão, o que depende do quê, qual invariante não pode ser quebrada. Chame esse custo
de **C** — e suponha duas horas e algumas dezenas de milhares de tokens.

A execução da tarefa em si, depois de entendida a anatomia, é curta: minutos. Chame-a de **E**.

| estratégia | custo |
|---|---|
| **leque ingênuo** — 30 agentes, cada um lê tudo | `30·(C + E)` → **60 horas só de compreensão** |
| **convergência** — um lê, os outros operam | `C + A + 30·(E + ε)` |

Onde **A** é o custo de escrever a anatomia e **ε** é o que cada operador ainda paga para ler o
artefato em vez da fonte inteira.

A convergência paga quando:

```
(N − 1)·C  >  A  +  N·ε
```

Com C em horas, A em dezenas de minutos e ε em minutos, o ponto de equilíbrio cai em **N ≈ 2**.
É por isso que a prática aparece cedo e não só em escala: **a partir de duas tarefas sobre o mesmo
terreno, reler o terreno já é desperdício.**

## O custo de entrada, medido nesta casa

O número que torna isto concreto não é o da anatomia — é o do **simples ato de entrar**.

| | |
|---|---|
| sessões com contabilidade de uso | **2.333** |
| contexto no **primeiro turno**, antes de qualquer trabalho útil | mediana **28.671** tokens · p90 **68.565** |
| somado em todas as sessões | **84,0 M tokens** — 55,1 M novos, 28,9 M lidos de cache |

**84 milhões de tokens gastos apenas para começar.** Isso não é a anatomia de um módulo: é o
piso — o que se paga antes de olhar para o problema. A anatomia vem *depois* disso, e é paga por
cima.

E note a direção do número: apenas **34%** desse primeiro turno veio de cache. O cache resolve a
repetição *dentro* de uma sessão; **entre** sessões, quase tudo é pago de novo. É exatamente o vão
que a convergência existe para cobrir.

---

# A doutrina, em três palavras gregas

O vocabulário já existe, e é do cerco — o que não é coincidência, porque o problema é o mesmo:
**não se assalta terreno que não foi levantado.**

```
ΚΑΤΑΣΚΟΠΟΣ   ──►   ΑΝΑΤΟΜΗ   ──►   ΕΡΓΑ
  o batedor        a anatomia       as obras
  levanta          é escrita        procedem
   (paga C)         (custa A)      (N × (E+ε))
```

**κατάσκοπος** — o batedor, enviado à frente para levantar o terreno. Um, não trinta. O que ele
produz não é opinião: é **descrição endereçável**, com o caminho de cada coisa que afirma existir.

**ἀνατομή** — literalmente *"corte através"*, a dissecação. É o artefato convergido: a anatomia do
módulo, com as dependências, as invariantes e os pontos onde cortar. Não é resumo: resumo é o que
se perde. A anatomia é o que **permite operar sem reler**.

**ἔργα** — as obras. Em contexto de cerco, as obras levantadas contra a muralha; aqui, as tarefas
reivindicadas e executadas pelos operadores, cada um sobre a sua, a partir da mesma anatomia.

## Onde isto se encaixa nas camadas

```
ΠΟΛΙΟΡΚΗΤΙΚΟΣ  →  o estratégico e o tático: o que vale cercar, e por onde
      │
      ▼
 ΚΑΤΑΣΚΟΠΟΣ    →  um agente paga a compreensão UMA vez
      │
      ▼
  ΑΝΑΤΟΜΗ      →  o artefato convergido, que passa por dokimasía como qualquer página
      │
      ▼
   ΕΡΓΑ        →  o operacional: N agentes reivindicam tarefas e executam
      │
      ▼
  ΒΑΣΙΛΕΙΑ     →  o que sobreviveu entra no reino
```

O Poliorketikos **já é o planejamento do operacional**. Quando o cerco é bem desenhado, as tarefas
que os operadores reivindicam já vêm com o ponto de ruptura identificado — e é por isso que a
pesquisa não é uma etapa separada do trabalho: ela é o que torna o trabalho curto.

---

# O risco, que é o lado difícil

> **A convergência troca custo por falha correlacionada.**

O leque ingênuo tem uma virtude acidental: trinta leitores independentes **discordam**. A
divergência entre eles é um código de correção de erro que ninguém projetou. Um leitor e trinta
executores não têm isso: **se a anatomia estiver errada, os trinta erram igual, na mesma direção,
e com confiança.**

Esta é a mesma classe de falha do gargalo 4 desta casa — *revisores todos da mesma família de
modelo* — num nível diferente. Não é analogia: é a mesma estrutura. Reduzir a diversidade de
leitura reduz o custo e reduz a detecção, e os dois caem juntos.

## Os quatro portões que a doutrina exige

Sem estes, a convergência é só economia com risco escondido:

1. **A anatomia passa por dokimasía.** Ela é uma página como qualquer outra: declara `sources` com
   endereço alcançável e declara `refutes` — *o que mostraria que ela está errada*.
2. **Quem escreveu a anatomia não a aprova.** Lei 2, sem exceção para artefato de processo.
3. **O operador tem o dever de divergir.** Se a anatomia disser que o arquivo está em X e ele não
   estiver, a tarefa **para** e a anatomia é contestada. Operador que contorna silenciosamente o
   erro do mapa destrói o único sensor que a doutrina tem.
4. **Uma tarefa de controle, lida da fonte.** Pelo menos uma das N é executada **sem** a anatomia,
   por quem leu o original. Se as duas convergirem, a compressão é fiel; se divergirem, o custo
   economizado era dívida.

O quarto portão é o que impede a doutrina de ser inverificável. Ele custa um C extra — e é
exatamente o preço de saber se os outros N−1 estavam certos.

---

# O que esta página **não** afirma

- **Não afirma que a convergência foi medida nesta casa.** O custo de entrada foi (84,0 M tokens,
  2.333 sessões); o *ganho* da convergência, não. O `refutes` acima descreve o experimento que o
  mediria, e ele ainda não foi corrido.
- **Não afirma que a anatomia substitui a fonte.** Ela é compressão com perda, e o portão 4 existe
  porque toda compressão com perda perde alguma coisa — a pergunta aberta é *o quê*.
- **Não afirma que paralelizar é ruim.** Afirma que paralelizar **a compreensão** é pagar N vezes
  por um bem que não é rival: conhecimento, ao contrário de trabalho, não se divide em partes.
