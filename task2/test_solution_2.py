import csv
import pytest
from solution_2 import get_animals_by_letter


def test_get_animals_by_letter_creates_csv(tmp_path):
    output_csv = tmp_path / 'beasts.csv'
    get_animals_by_letter(output_path=str(output_csv))

    assert output_csv.exists(), "Файл beasts.csv не создан"

    with open(output_csv, encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)

    assert len(rows) > 0, "Файл beasts.csv пустой"

    for letter, count in rows:
        assert letter.isalpha(), "Первая колонка должна быть буквой"
        assert count.isdigit(), "Вторая колонка должна быть числом"