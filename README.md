# GitHub Actions — Testes multiplataforma

Exercício de Integração Contínua utilizando GitHub Actions.

## Objetivo

Executar o build e os testes de uma biblioteca Python em **Ubuntu, macOS e Windows**, nas versões **Python 3.12 e 3.13**.

## Funcionalidades

Biblioteca com operações de soma, subtração, multiplicação, divisão (com validação de divisão por zero) e potenciação (com validação de expoente inteiro).

## Testes locais

A partir da raiz do repositório:

```bash
python -m pip install .
python -m compileall -q src
python -m unittest discover -s tests -p "test_*.py" -v
```

O projeto possui 9 testes unitários.

## Integração contínua

O workflow está em `.github/workflows/ci.yml`. Ele executa automaticamente após cada push e em pull requests, além de permitir execução manual. Uma matriz combina três sistemas operacionais e duas versões de Python, produzindo **6 jobs** por execução.

Em cada job, o GitHub Actions realiza checkout do código, configura a versão de Python, instala o projeto, compila os módulos Python e executa os 9 testes.

A opção `fail-fast: false` permite visualizar os resultados das seis combinações mesmo que alguma falhe.

## Como verificar

No GitHub, abra a aba **Actions**, selecione **Testes multiplataforma** e confira os seis jobs. Cada um deve apresentar conclusão `success` e nove testes aprovados.
