# okf/ — sete páginas, como amostra

**Isto é um spoiler, não o corpus.** O reino tem 202 páginas; aqui estão sete, escolhidas porque
mostram a *forma* sem entregar o conteúdo.

| | página |
|---|---|
| 01 | a tese: conhecimento que não pode cair |
| 02 | a lei do portão, e a etimologia que a sustenta |
| 03 | as cinco classes epistêmicas |
| 04 | o experimento em curso, e o que ele não verificou |
| 05 | **a convergência informacional** — a doutrina que liga a pesquisa ao operacional |
| 06 | **φιλομαθής ↔ φιλοπράκτωρ** — as duas disposições, e o gnômon entre elas |
| 07 | **metafísica e o tribunal da razão** — onde Kant encaixa, e onde explicitamente não |

**OKF** (*Open Knowledge Format*, v0.2) é o formato em que cada unidade de conhecimento desta casa é
escrita. A regra que o define cabe numa linha:

> Uma página que não declara o que a derrubaria não entra.

O frontmatter não é metadado decorativo — **é fonte**. Dele saem os portões de CI, o grafo que o
Phanes desenha e as contagens de reputação.

| campo | para quê |
|---|---|
| `type` | a classe da página — `Claim`, `Pattern`, `Decision`, `Project`, `Identity`, `Reputation` |
| `status` | `proposto` até alguém que não a escreveu admiti-la |
| `sources[]` | de onde vem, com endereço alcançável e autor |
| `relations` | ligações **tipadas**: `extends`, `converges`, `corrects`, `contradicts` |
| `refutes` | **o que derrubaria esta página.** Sem isto, o portão reprova |
| `generated` | qual modelo escreveu, e quando |

As `relations` são o que o grafo desenha: 420 arestas, com cor por tipo, porque *estender* e
*contradizer* não são a mesma ligação.
