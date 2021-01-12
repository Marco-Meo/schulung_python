import requests
import json

# Create Token:
# python manage.py drf_create_token admin


url = "http://localhost:8000/api/"
token = ""
headers = {"Authorization": "Token " + token}

headers = {"Authorization": "Token " + token}
url_faq = url + "faq/"

def faq_create():
    body = {
        "title": "API 1",
        "description": "Ein neuer Eintrag per API",
        "creator": 1
    }

    try:
        response = requests.post(url_faq, data=body, headers=headers,)
        return response
    except Exception as e:
        print(f"Fehler {e}")
        return None


def faq_update(body):
    body['title'] = " ".join(['Update', body.get('title')])
    del body['creation_date']
    print(body)
    url_faq_update = url_faq + str(body['id'])+"/"
    print(url_faq_update)
    try:
        response = requests.put(url_faq_update, data=body, headers=headers)
        return response
    except Exception as e:
        print(f"Fehler: {e}")
        return None


if __name__ == '__main__':
    result = faq_create()
    if result:
        print('Response code:', result.status_code)
        response_dict = json.loads(result.text)
        print("New ID: ", response_dict.get('id'))
        print("Title: ", response_dict.get('title'))


        update_result = faq_update(response_dict)
        print("Response code: ", update_result.status_code)
        print(update_result.text)