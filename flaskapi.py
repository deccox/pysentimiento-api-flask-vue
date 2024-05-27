from flask import Flask, request, jsonify
from flask_cors import CORS
from pysentimiento import create_analyzer
from pysentimiento.preprocessing import preprocess_tweet
import pandas as pd

app = Flask(__name__)
CORS(app)  # Adiciona suporte a CORS ao seu aplicativo Flask
analyzer = create_analyzer(task="sentiment", lang="pt")


@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    # Verifica se o arquivo CSV foi enviado
    if 'file' not in request.files:
        return jsonify({"error": "Arquivo CSV não encontrado."}), 400

    file = request.files['file']

    # Verifica se o arquivo é CSV
    if file.filename == '':
        return jsonify({"error": "Nome de arquivo vazio."}), 400
    if not file.filename.endswith('.csv'):
        return jsonify({"error": "Arquivo não é CSV."}), 400

    # Lê o CSV
    try:
        
        
        print(f"tentando ler")
        dataset = pd.read_csv(file)
    except Exception as e:
        return jsonify({"error": f"Erro ao ler arquivo CSV: {str(e)}"}), 400

    texto = dataset['text']
    output = []

    for text in texto:
        output.append(analyzer.predict(preprocess_tweet(str(text), lang="pt")))

    total_probas = {"NEU": 0, "POS": 0, "NEG": 0}
    total_samples = len(output)

    for out in output:
        for sentiment, proba in out.probas.items():
            total_probas[sentiment] += proba / total_samples

    result = {"Porcentagens de cada sentimento:": total_probas}

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
