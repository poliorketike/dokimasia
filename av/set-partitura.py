"""A PARTITURA DO SET — uma só, lida pelos dois lados.

O navegador executa estes eventos enquanto o vídeo grava; o renderizador offline
lê os MESMOS eventos para produzir o áudio. É a mesma regra da cena do grafo: uma
leitura, dois consumidores — se houvesse duas listas, elas divergiriam.

A tônica não é aleatória: anda pelos graus da dórica sobre D, então as trocas
caem dentro da escala em vez de cortá-la.
"""
import json

D2, E2, F2, G2, A2 = 73.42, 82.41, 87.31, 97.999, 110.0

SET = [
    (0.0,  {"timbres": ["cachoeira"], "tonica": D2, "periodo": 2.6, "brilho": 1.0,
            "ressonancia": 1.0, "cauda": 1.0, "dispersao": 0.0, "registro": "uníssono"}),
    (6.0,  {"timbres": ["cachoeira", "cordas"], "brilho": 1.6}),
    (12.0, {"ruido": True, "registro": "quintas"}),
    (18.0, {"timbres": ["cachoeira", "cordas", "cristal"], "tonica": F2, "periodo": 1.9}),
    (24.0, {"ruido": False, "timbres": ["cristal", "sino"], "brilho": 2.4, "cauda": 1.6}),
    (30.0, {"medieval": True, "registro": "oitavas", "tonica": A2, "periodo": 1.4}),
    (36.0, {"timbres": ["sino", "vidro", "sopro"], "dispersao": 16.0, "ressonancia": 5.0}),
    (42.0, {"medieval": False, "timbres": ["vidro", "sopro"], "tonica": G2, "brilho": 1.2}),
    (48.0, {"timbres": ["bordao", "pulso"], "periodo": 4.0, "tonica": D2,
            "registro": "uníssono", "dispersao": 0.0, "ressonancia": 1.0, "cauda": 2.2}),
    (54.0, {"timbres": ["cachoeira"], "periodo": 2.6, "brilho": 1.0, "cauda": 1.0}),
]
DURACAO = 60.0

def estado_em(t):
    """O estado acumulado no instante t — os eventos são deltas, não quadros completos."""
    e = {}
    for quando, ev in SET:
        if quando <= t:
            e.update(ev)
    return e

if __name__ == "__main__":
    json.dump({"set": [[t, ev] for t, ev in SET], "duracao": DURACAO},
              open("set.json", "w"), ensure_ascii=False, indent=1)
    print(f"{len(SET)} eventos · {DURACAO:.0f} s")
