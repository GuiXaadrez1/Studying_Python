from deep_translator import GoogleTranslator
import requests
from bs4 import BeautifulSoup

# Obtendo o conteúdo do site
url = "https://www.geeksforgeeks.org/opencv-python-tutorial"
response = requests.get(url)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    # Usando BeautifulSoup para extrair o conteúdo de texto da página
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()

    # Traduzindo o texto de inglês para português
    translated_text = GoogleTranslator(source='en', target='pt').translate(text)

    # Exibindo o texto traduzido
    print(translated_text)

else:
    print(f"Erro ao acessar o site: {response.status_code}")
