import random
import pandas as pd


def gerar_split_logico(sexo, nivel, dias_disponiveis, tempo_disponivel, idade, peso, altura):
    # INICIANTES
    if nivel == "iniciante":
        if dias_disponiveis == 3:
            return "Full Body 3x"
        if dias_disponiveis == 4:
            return "Upper/Lower 2x" if tempo_disponivel >= 60 else "Full Body 4x"
        if dias_disponiveis == 6:
            return "PPL 2x"
        return "Upper/Lower 3x + Full Body"

    # INTERMEDIÁRIOS
    elif nivel == "intermediario":
        if dias_disponiveis == 3:
            return "Full Body 3x"

        if dias_disponiveis == 4:
            return "Upper/Lower 2x" if tempo_disponivel >= 70 else "Full Body 4x"

        if dias_disponiveis == 5:
            if sexo == "F":
                return "Lower Focus (LULUL)" if idade < 45 else "Upper/Lower 2x + Full Body"
            else:
                return "UL PPL" if tempo_disponivel >= 80 else "Bro Split"

        if dias_disponiveis == 6:
            if tempo_disponivel >= 70:
                return "PPL 2x" if peso < 90 else "Arnold Split"
            return "Upper/Lower 3x"

    # AVANÇADOS
    else:
        if dias_disponiveis == 3:
            return "PPL 1x" if idade < 40 else "Full Body 3x"

        if dias_disponiveis == 4:
            return "Upper/Lower 2x" if tempo_disponivel >= 60 else "Full Body 4x"

        if dias_disponiveis == 5:
            if sexo == "F":
                return "Lower Focus (LULUL)" if peso < 75 else "Upper/Lower 2x + Full Body"
            else:
                return "UL PPL" if idade < 35 else "Bro Split"

        if dias_disponiveis == 6:
            if tempo_disponivel >= 80:
                return "Arnold Split" if idade < 32 else "PPL 2x"
            return "PPL 2x" if tempo_disponivel >= 60 else "Upper/Lower 3x"


data = []
random.seed(42)

for i in range(5000):
    idade = int(random.triangular(16, 70, 25))
    sexo = random.choice(["M", "F"])
    peso = round(random.uniform(55, 120), 1) if sexo == "M" else round(
        random.uniform(45, 95), 1)
    altura = round(random.uniform(1.50, 2.00), 2)
    nivel = random.choices(["iniciante", "intermediario", "avancado"], weights=[
                           0.35, 0.40, 0.25])[0]
    dias_disponiveis = random.randint(3, 6)
    tempo_disponivel = random.choices([40, 50, 60, 70, 80, 90, 100], weights=[
                                      0.1, 0.15, 0.30, 0.25, 0.15, 0.03, 0.02])[0]

    split = gerar_split_logico(
        sexo, nivel, dias_disponiveis, tempo_disponivel, idade, peso, altura)
    data.append([sexo, idade, peso, altura, nivel,
                dias_disponiveis, tempo_disponivel, split])

df = pd.DataFrame(data, columns=['sexo', 'idade', 'peso', 'altura',
                  'nivel', 'dias_disponiveis', 'tempo_disponivel', 'split'])
df.to_csv("../data/alunos.csv", index=False)
