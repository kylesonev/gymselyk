import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline


df = pd.read_csv("../data/alunos.csv")

X = df.drop("split", axis=1)
y = df["split"]

colunas_categoricas = ["sexo", "nivel"]
colunas_numericas = [
    "idade", "peso", "altura",
    "dias_disponiveis", "tempo_disponivel"
]

preprocessador = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), colunas_categoricas),
        ("num", "passthrough", colunas_numericas)
    ]
)

model = Pipeline(steps=[
    ("preprocessamento", preprocessador),
    ("modelo", RandomForestClassifier(
        n_estimators=100,
        random_state=42
    ))
])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model.fit(X_train, y_train)

modelo_treinado = "../model/model.pkl"

with open(modelo_treinado, 'wb') as f:
    pickle.dump(model, f)

print(f"Modelo salvo com sucesso em: {modelo_treinado}")