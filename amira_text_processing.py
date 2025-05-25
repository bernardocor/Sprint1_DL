
import json
import pickle
import csv
import spacy

# Intenta cargar modelo de spaCy en español, si no existe usa inglés
try:
    nlp = spacy.load("es_core_news_sm")
except:
    nlp = spacy.load("en_core_web_sm")

# Cargar datos del archivo conversations.json
with open("conversations.json", "r", encoding="utf-8") as f:
    data = json.load(f)

vocabulario = set()
tags = []
all_patterns = []

for entry in data:
    tag = entry["tag"]
    tags.append(tag)
    for pattern in entry["patterns"]:
        doc = nlp(pattern.lower())
        tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
        vocabulario.update(tokens)
        all_patterns.append((tokens, tag))

# Guardar vocabulario y tags en archivos pickle
with open("vocabulario.pkl", "wb") as f:
    pickle.dump(sorted(list(vocabulario)), f)

with open("tags.pkl", "wb") as f:
    pickle.dump(sorted(list(set(tags))), f)

# Crear la bolsa de palabras para cada pattern
vocabulario = sorted(list(vocabulario))
bow_data = []

for tokens, tag in all_patterns:
    bow_vector = [1 if word in tokens else 0 for word in vocabulario]
    bow_data.append([tag] + bow_vector)

# Guardar la bolsa de palabras como CSV
header = ["tag"] + vocabulario
with open("bow_amira_patterns.csv", "w", encoding="utf-8", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    writer.writerows(bow_data)

print("Procesamiento completado: vocabulario.pkl, tags.pkl y bow_amira_patterns.csv generados.")
