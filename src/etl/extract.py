import requests
import json

end_point = 'https://parallelum.com.br/fipe/api/v1/carros/marcas'

def extract(end_point):
    
    try:
        response = requests.get(end_point)
        data = json.loads(response.text)
        
        return data
    except Exception as e:
        print(e)


if __name__ == "__main__":
    text = extract(end_point)
    print(text)