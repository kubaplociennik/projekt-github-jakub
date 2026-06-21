# Sprawozdanie zaliczeniowe NDA_ABU_INFinz_NW_HB(m)_L25/26

**Jakub Płóciennik**

Nr albumu: 102182

Profil GH: [https://github.com/kubaplociennik](https://github.com/kubaplociennik)

Repo GH: [https://github.com/kubaplociennik/projekt-github-jakub](https://github.com/kubaplociennik/projekt-github-jakub)

Docker image: keiok/projekt-github-jakub:latest

Niniejsze sprawozdanie dokumentuje wykonanie cwiczen obejmujacych Git,
GitHub, Makefile, lint, testy, Docker, DockerHub oraz CircleCI.

## Opis repo

Repozytorium zawiera prosta aplikacje Flask zwracajaca komunikat Hello World
w formacie JSON. Dane studenta i kursu sa zapisane w pliku
`data/profile.json`, ktory ma poprawna, zagniezdzona strukture JSON. Aplikacja
jest testowana przy pomocy modulu `unittest`, a jakosc kodu sprawdzana przez
`flake8`.

`Makefile` udostepnia targety `deps`, `lint`, `test`, `run`, `docker_build`
oraz `docker_push`. Target `deps` tworzy lokalne srodowisko Python i instaluje
zaleznosci. Target `lint` uruchamia `flake8`, target `test` uruchamia testy
jednostkowe, target `run` startuje lokalny serwer Flask, a targety
`docker_build` i `docker_push` buduja oraz publikuja obraz Docker.

Konfiguracja CircleCI znajduje sie w `.circleci/config.yml`. Workflow
`build-and-test` wykonuje kolejno `make deps`, `make lint`, `make test`,
`make docker_build` oraz `make docker_push`. Obraz Docker jest nazwany
`keiok/projekt-github-jakub:latest` i jest widoczny na DockerHub po wykonaniu
pipeline.

## Screenshot GitHub

![github_commits.png](Sprawozdanie%20zaliczeniowe%20NDA_ABU_INFinz_NW_HB(m)_/github_commits.png)

## Screenshot CircleCI

![circleci_workflow.png](Sprawozdanie%20zaliczeniowe%20NDA_ABU_INFinz_NW_HB(m)_/circleci_workflow.png)

## Screenshot DockerHub

![dockerhub_image.png](Sprawozdanie%20zaliczeniowe%20NDA_ABU_INFinz_NW_HB(m)_/dockerhub_image.png)