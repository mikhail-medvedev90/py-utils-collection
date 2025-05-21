import os
import requests
from bs4 import BeautifulSoup
import csv

from constants import BASE_URL, CATEGORY_URL


def get_animals_by_letter(output_path: str = None) -> None:
    """
    Собирает количество животных на Википедии по первой букве
    и сохраняет результат в CSV-файл (по умолчанию 'beasts.csv' рядом со скриптом).
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

    if output_path is None:
        output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'beasts.csv')

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            for letter, count in sorted(result.items()):
                writer.writerow([letter, count])
        print(f"Файл успешно сохранён: {output_path}")
    except Exception as e:
        print(f"Ошибка при сохранении файла: {e}")


if __name__ == '__main__':
    print("Рабочая директория:", os.getcwd())
    get_animals_by_letter()
