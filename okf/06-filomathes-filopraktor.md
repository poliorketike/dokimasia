---
type: Pattern
title: "φιλομαθής ↔ φιλοπράκτωρ: as duas disposições, e o gnômon entre elas"
description: "O terceiro eixo da casa. Não são camadas nem agentes: são disposições que todo membro carrega em tensão, e o pipeline inteiro — do cerco à obra — é a resolução institucional dessa tensão. Com a razão medida."
tags: [disposicao, filomathes, filopraktor, medida, eixo]
okf_version: "0.2"
generated: { by: claude-opus-5/anthropic, at: 2026-10-02T00:00:00Z }
status: proposto
sources:
  - id: platao
    resource: "Platão, República — φιλομαθής como traço do que busca saber"
    title: "φιλομαθής: adjetivo atestado, 'amante do aprender'"
    author: human:platao
  - id: lsj
    resource: "Liddell–Scott–Jones — πράκτωρ, φιλοπράγμων, φιλόπονος"
    title: "πράκτωρ ('o que faz, o executor') é atestado; φιλοπράκτωρ NÃO é composto clássico"
    author: machine:lsj
  - id: medida
    resource: "~/.claude/projects/*/*.jsonl — 58.337 chamadas de ferramenta classificadas, 2026-10-02"
    title: "Ferramentas inequívocas 1,32:1 a favor da leitura; com Bash, 0,31:1 a favor da ação"
    author: machine:medicao-local
relations:
  extends:
    - okf/05-convergencia-informacional.md
  converges:
    - okf/03-classes-epistemicas.md
  corrects:
    - "a leitura de que as duas disposições seriam mais duas camadas ao lado das quatro"
refutes: >
  Esta página cai se a razão ler/agir, medida por sessão, não tiver relação nenhuma com a qualidade
  do que a sessão produziu — isto é, se numa amostra de ≥40 sessões classificadas por revisão cega
  em "entregou" / "não entregou", a distribuição da razão for indistinguível entre os dois grupos.
  Nesse caso a tensão seria real como vocabulário e irrelevante como instrumento.
---

> ⚠️ **Nota etimológica, devida antes do argumento.** `φιλομαθής` é atestado e clássico. **`φιλοπράκτωρ`
> não é um composto grego atestado** — é um neologismo moderno. `πράκτωρ` existe (*o que faz, o
> executor*; também *o cobrador*), e `φιλοπράγμων` existe mas tende ao pejorativo (*intrometido*).
> O atestado para "amante do trabalho" é `φιλόπονος`. Usamos `φιλοπράκτωρ` por precisão semântica —
> queremos *o que ama executar*, não *o que ama se intrometer* — e a marcamos como composição
> moderna onde ela aparece. Nome bonito com etimologia inventada seria exatamente o defeito que
> esta casa existe para pegar.

# O que elas não são

**Não são duas camadas.** As quatro camadas são atos que mudam o estado do mundo; estas duas são
**adjetivos** — em grego, literalmente — e adjetivo qualifica quem opera, não o que é operado.

**Não são dois agentes.** Nenhum membro desta casa é só um dos dois. O batedor que não quisesse
entregar nada jamais fecharia a anatomia; o operador que não quisesse entender nada executaria o
mapa errado com confiança.

São **disposições em tensão**, e a tensão é produtiva nos dois sentidos:

| sozinha | o que acontece |
|---|---|
| **φιλομαθής** sem φιλοπράκτωρ | pesquisa infinita. O cerco nunca termina; a muralha é estudada até ruir sozinha |
| **φιλοπράκτωρ** sem φιλομαθής | execução sobre mapa não examinado. São os trinta agentes errando na mesma direção |

# O que elas são: o eixo que atravessa tudo

A tensão não se resolve escolhendo um lado. Ela se resolve **institucionalmente**, e a casa inteira
é essa resolução:

```
                        φιλομαθής ─────────────────────► φιλοπράκτωρ
                        (amar saber)                      (amar fazer)

ΠΟΛΙΟΡΚΗΤΙΚΟΣ      ████████████████░░░░░░░░░░░░░░░░   estratégico e tático
  ΚΑΤΑΣΚΟΠΟΣ       ██████████████████████░░░░░░░░░░   o máximo de φιλομαθής
    ΑΝΑΤΟΜΗ        ░░░░░░░░ ◄── a dobradiça ──► ░░░   onde um vira o outro
      ΕΡΓΑ         ░░░░░░░░░░░░██████████████████████  o máximo de φιλοπράκτωρ
    ΒΑΣΙΛΕΙΑ       ████████░░░░░░░░░░░░░░████████████  admitir é julgar e decidir
      ΦΑΝΗΣ        ████████████████████████████████████ revelar serve aos dois
```

**A ἀνατομή é a dobradiça.** É o único artefato da casa cuja função é *converter uma disposição na
outra*: tudo que o batedor aprendeu entra nela como aprendizado e sai dela como instrução. Por isso
ela passa por dokimasía, e por isso o operador tem **dever de divergir** — a dobradiça é o lugar
onde a conversão pode estar errada.

E é por isso que a orquestração **não é uma fase**. Durante o operacional, quem orquestra continua
φιλομαθής: lê o que os operadores devolvem, e é essa leitura que detecta a anatomia errada antes
que as trinta obras subam tortas.

---

# A medida

Se as duas disposições são reais, elas deixam rastro. O rastro é a proporção entre **ler** e
**agir** nas chamadas de ferramenta.

O classificador está declarado para quem quiser refazer a conta: `Read`, `Grep`, `Glob`,
`WebFetch`, `WebSearch` contam como ler; `Edit`, `Write`, `NotebookEdit` contam como agir; `Bash` é
classificado pelo verbo inicial.

| | ler | agir | razão |
|---|---:|---:|---|
| **ferramentas inequívocas** | 8.380 | 6.363 | **1,32 : 1** — lê um pouco mais do que faz |
| **com `Bash`** (43.595 chamadas) | 13.834 | 44.503 | **0,31 : 1** — três atos para cada leitura |
| por sessão (≥20 chamadas, n=96) | — | — | mediana **13%** de leitura · p90 **46%** |

## O que a divergência entre as duas linhas revela

A primeira linha e a segunda discordam por um fator de **4,3×**, e a discordância **é o achado**.

Entre as ferramentas de arquivo, a casa é equilibrada e levemente φιλομαθής. Quando o `Bash` entra,
ela aparece fortemente φιλοπράκτωρ. Mas olhar o que o `Bash` faz desfaz a leitura fácil:

| o que o `Bash` executa | fatia |
|---|---:|
| **medir e testar** (`cargo test`, `playwright`, `--check`, `wc -l`, `pytest`) | **18%** |
| construir | 3% |
| `git` que escreve | 2% |
| o resto (mover, instalar, rodar, inspecionar) | 77% |

**Quase um quinto de toda a ação desta casa é medição.** E medir não é nem aprender nem fazer: é o
terceiro gesto, o do gnômon. É Palamedes entre os dois.

> As duas disposições são um par; o par precisa de uma dobradiça para não virar oscilação.
> A dobradiça é a **medida** — e é por isso que ΠΑΛΑΜΗΔΗΣ está na cintura da pirâmide, ao lado do
> método, e não na base com os atos.

## O que esta medida **não** diz

- **Não diz que a razão está certa.** 0,31:1 pode ser disciplina ou pode ser pressa. Esta página
  não tem como distinguir, e o `refutes` acima descreve o experimento que distinguiria.
- **Não diz que ler é melhor que agir.** Uma casa com razão 3:1 a favor da leitura seria
  φιλομαθής doente — o cerco que nunca termina.
- **O classificador de `Bash` é grosseiro.** Ele lê o verbo inicial, e um `cargo test` conta como
  ação quando é, na verdade, medição. Os 18% acima corrigem parte disso; o resto fica como
  limitação declarada, não como ruído escondido.
