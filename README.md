# Simulação de Pipeline DevOps com Python

## Objetivo
Demonstrar o uso de GitHub Actions para automação de testes em Python.

## Estrutura do projeto
- `app.py`: Função de soma simples
- `test_app.py`: Testes automatizados com pytest
- `.github/workflows/python-tests.yml`: Pipeline CI com GitHub Actions

## Como funciona
A cada push ou pull request:
1. O código é verificado;
2. As dependências são instaladas;
3. Os testes são executados automaticamente.

## Requisitos
- Python 3.10+
- pytest
