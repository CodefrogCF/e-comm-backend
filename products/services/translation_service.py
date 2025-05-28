
import requests

DEEPL_API_KEY = '9d21df08-1f38-4627-84a9-41600b4f0ee5:fx'

def translate_text(text, target_lang='DE'):
    response = requests.post(
        'https://api-free.deepl.com/v2/translate',
        data={
            'auth_key': DEEPL_API_KEY,
            'text': text,
            'target_lang': target_lang
        }
    )
    response.raise_for_status()
    return response.json()['translations'][0]['text']