import os
import pytest
import csv
from solution import get_animals_by_letter


def test_get_animals_by_letter_creates_csv(tmp_path):
    old_cwd = os.getcwd()
    os.chdir(tmp_path)

    try:
        get_animals_by_letter()
        csv_path = tmp_path / 'beasts.csv'
        assert csv_path.exists(), "Файл beasts.csv не создан"

        with open(csv_path, encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = list(reader)
        assert len(rows) > 0, "Файл beasts.csv пустой"

        for letter, count in rows:
            assert letter.isalpha(), "Первая колонка должна быть буквой"
            assert count.isdigit(), "Вторая колонка должна быть числом"

    finally:
        os.chdir(old_cwd)
