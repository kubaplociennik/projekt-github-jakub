# Projekt GitHub Jakub

Projekt zaliczeniowy dla kursu `NDA_ABU_INFinz_NW_HB(m)_L25/26`.

Aplikacja jest prostym serwisem Flask, ktory zwraca komunikat `Hello World`
w formacie JSON. Repozytorium pokazuje podstawowy workflow inzynierski:

- prace z historia Git,
- uruchamianie aplikacji Python/Flask,
- testowanie i lintowanie przez `Makefile`,
- budowanie obrazu Docker,
- automatyzacje CI/CD w CircleCI.

## Wymagania

- Python 3.11+
- Docker
- GNU Make

## Polecenia

```sh
make deps
make lint
make test
make run
make docker_build
make docker_push
```

Target `docker_push` wymaga ustawienia zmiennych `DOCKERHUB_USERNAME` i
`DOCKERHUB_IMAGE`.
