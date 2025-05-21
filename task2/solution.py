import os
import requests
from bs4 import BeautifulSoup
import csv

BASE_URL = 'https://ru.wikipedia.org'
CATEGORY_URL = f'{BASE_URL}/wiki/Категория:Животные_по_алфавиту'
OUTPUT_CSV = os.path.join(os.path.dirname(__file__), 'beasts.csv')

def get_animals_by_letter():
    """
    Собирает статистику животных по первой букве названия со страниц Википедии
    и сохраняет результат в CSV-файл 'beasts.csv' рядом с этим скриптом.
    """
    result = {}
    url = CATEGORY_URL
    while url:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        for li in soup.select('.mw-category-group ul li'):
            text = li.text.strip()
            if not text:
                continue
            letter = text[0].upper()
            result[letter] = result.get(letter, 0) + 1
        next_page = soup.select_one('a:-soup-contains("Следующая страница")')
        if next_page:
            url = BASE_URL + next_page['href']
        else:
            break
    with open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for letter, count in sorted(result.items()):
            writer.writerow([letter, count])

if __name__ == '__main__':
    print("Сохраняем файл в:", OUTPUT_CSV)
    get_animals_by_letter()
    print("Файл сохранён.")