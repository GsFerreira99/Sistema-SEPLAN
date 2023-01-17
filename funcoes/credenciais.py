import json

def carregar_credenciais(caminho):
    try:
        with open(caminho, encoding='utf-8') as meu_json:
            return json.load(meu_json)
    except:
        dictionary = {
                        "host":"localhost",
                        "user":"",
                        "password":"",
                        "porta":"3306"
                    }
        
        json_object = json.dumps(dictionary, indent = 4)
        with open(caminho, "w") as meu_json:
            meu_json.write(json_object)
            return carregar_credenciais(caminho)