import json
import requests



def buscar_dados_uf():
    request = requests.get(f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/SE/distritos")
    todo = json.loads(request.content)
    # print(todo)
    for i in todo:
        print(i['nome'])
    

if __name__ == '__main__':
    # buscar_dados()
    buscar_dados_uf()