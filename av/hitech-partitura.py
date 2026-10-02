"""HITECH-SET — a partitura, e a matemática que a organiza.

Três números organizam tudo, e cada um entra pela propriedade que ele de fato tem.

142857 — o período de 1/7. A propriedade real dele não é "distribuição" (foi por isso que ele
  não serviu para espalhar as fases do campo de fluxo): é que os múltiplos 1..6 são ROTAÇÕES dos
  mesmos dígitos — 285714, 428571, 571428, 714285, 857142 — e o sétimo, 999999, quebra o ciclo.
  Aqui isso vira a estrutura rítmica: seis compassos, cada um com uma rotação da máscara, e o
  SÉTIMO é o drop, porque 7 × 142857 = 999999 e todos os dígitos saturam ao mesmo tempo.

189 BPM — 7 × 27, e 27 = 1+4+2+8+5+7, a soma dos dígitos. Cai dentro da faixa do hi-tech
  (170–200) sem ser escolhido por gosto.

6 contra 16 — a máscara tem 6 células e o compasso tem 16 semicolcheias. Elas só voltam a casar a
  cada 48 passos (3 compassos), e com o ciclo de 7 compassos por cima o alinhamento completo leva
  336 passos — 21 compassos. É o polirritmo que o número produz sozinho.

A afinação é por razões de inteiros pequenos (as divisões do monocórdio: 3/2, 4/3, 5/4, 7/4, 9/8)
e a escala é a raga **Bhairav** — S r G m P d N, semitons 0,1,4,5,7,8,11 — sobre um bordão de Sa e
Pa. É de onde vem a cor indiana, e não de um sample.
"""

BPM = 189.0
BATIDA = 60.0 / BPM
COMPASSO = BATIDA * 4          # 1,270 s
PASSO = COMPASSO / 16          # a semicolcheia
BHAIRAV = [0, 1, 4, 5, 7, 8, 11]
DIGITOS = [1, 4, 2, 8, 5, 7]
SA = 97.999                    # G2 — grave o bastante para o bordão, agudo o bastante para rolar

def mascara(compasso):
    """A máscara do compasso: rotação dos dígitos, e o sétimo satura em noves."""
    if compasso % 7 == 6:
        return [9] * 6
    return DIGITOS[compasso % 6:] + DIGITOS[:compasso % 6]

# seções, em compassos
SECOES = [
    ("intro",    0,  7, dict(kick=False, baixo=False, lead=False, tanpura=True,  tabla=False)),
    ("kick",     7, 14, dict(kick=True,  baixo=False, lead=False, tanpura=True,  tabla=False)),
    ("rolo",    14, 28, dict(kick=True,  baixo=True,  lead=False, tanpura=True,  tabla=True)),
    ("lead",    28, 42, dict(kick=True,  baixo=True,  lead=True,  tanpura=True,  tabla=True)),
    ("quebra",  42, 49, dict(kick=False, baixo=False, lead=True,  tanpura=True,  tabla=True)),
    ("tudo",    49, 63, dict(kick=True,  baixo=True,  lead=True,  tanpura=True,  tabla=True)),
]
COMPASSOS = 63
DURACAO = COMPASSOS * COMPASSO

def secao(c):
    for nome, a, b, f in SECOES:
        if a <= c < b:
            return nome, f
    return "fim", dict(kick=False, baixo=False, lead=False, tanpura=True, tabla=False)

if __name__ == "__main__":
    print(f"{BPM:.0f} BPM · compasso {COMPASSO:.3f} s · semicolcheia {PASSO*1000:.0f} ms")
    print(f"{COMPASSOS} compassos · {DURACAO:.1f} s")
    for c in range(8):
        print(f"  compasso {c+1}: {mascara(c)}  {'← 999999, o drop' if c%7==6 else ''}")
