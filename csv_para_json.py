import pandas as pd
import json

def csv_para_json(caminho_csv, caminho_json):

    df = pd.read_csv(caminho_csv)
    
    df = df.fillna("-")
    
    json_data = df.to_dict(orient='records')
    
    with open(caminho_json, 'w', encoding='utf-8') as arquivo_json:
        json.dump(json_data, arquivo_json, indent=4, ensure_ascii=False)
    
    print(f"Arquivo JSON criado com sucesso em {caminho_json}")

caminho_csv = input("Digite o caminho do arquivo CSV: ")
caminho_json = input("Digite o caminho para salvar o arquivo JSON: ")
csv_para_json(caminho_csv, caminho_json)

