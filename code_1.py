from pysentimiento import create_analyzer
from pysentimiento.preprocessing import preprocess_tweet
import pandas as pd


analyzer = create_analyzer(task="sentiment", lang="pt")


# import dataset
dataset = pd.read_csv('dataset.csv')


texto = dataset['text']
output = []


for text in texto:
    output.append(analyzer.predict(preprocess_tweet(str(text), lang="pt")))
    

total_probas = {"NEU": 0, "POS": 0, "NEG": 0}
total_samples = len(output)

for out in output:
    for sentiment, proba in out.probas.items():
        total_probas[sentiment] += proba / total_samples

print("Porcentagens de cada sentimento:")
for sentiment, proba in total_probas.items():
    print(f"{sentiment}: {proba * 100:.2f}%")