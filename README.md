# Mini CI/CD - kalkulator Python

## Funkcje
- Dodawanie dwóch liczb
- Mnożenie dwóch liczb

## Uruchomienie lokalne
python app.py

## Testy
pip install -r requirements.txt
python -m pytest -v

## Docker
docker build -t mini-cicd:local .
docker run --rm mini-cicd:local

## CI
GitHub Actions automatycznie uruchamia testy
i buduje obraz Docker po push oraz przy Pull Request.
