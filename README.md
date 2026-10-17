# Podstawy kryptografii kwantowej — środowisko Docker

Gotowe środowisko do realizacji całego cyklu 7 laboratoriów z Qiskit.
JupyterLab działa w kontenerze Docker, a notebooki i dane pozostają na hoście.

## Wymagania po stronie komputera

- Docker Engine + Docker Compose **lub** Docker Desktop,
- dostęp do Internetu podczas pierwszego budowania obrazu,
- przeglądarka internetowa,
- dostęp do IBM Quantum Platform tylko w laboratoriach korzystających z QPU.

> Archiwum nie zawiera binarnych paczek Python ani gotowego obrazu Dockera.
> Zależności są pobierane automatycznie podczas `docker compose build`.

## Szybki start

1. Rozpakuj archiwum.
2. Przejdź do katalogu projektu.
3. Utwórz plik `.env` na podstawie przykładu:

### Linux / macOS

```bash
cp .env.example .env
```

### Windows PowerShell

```powershell
Copy-Item .env.example .env
```

Na Linuksie sprawdź UID/GID:

```bash
id -u
id -g
```

Jeżeli są inne niż `1000`, popraw `UID` i `GID` w `.env`.

4. Zbuduj i uruchom środowisko:

```bash
docker compose up -d --build
```

5. Otwórz:

```text
http://127.0.0.1:8888
```

6. Podaj token ustawiony jako `JUPYTER_TOKEN` w `.env`.
7. Otwórz `notebooks/00_test_srodowiska.ipynb` i wykonaj wszystkie komórki.

## Zatrzymanie

```bash
docker compose down
```

Notebooki i dane pozostają w katalogach `notebooks/` i `data/`.

## Aktualizacja / przebudowanie

Po zmianie `requirements.txt`:

```bash
docker compose build --no-cache
docker compose up -d
```

## IBM Quantum Platform

Token najlepiej przekazać przez `.env`:

```text
IBM_QUANTUM_TOKEN=...
IBM_QUANTUM_INSTANCE=...
```

Nie umieszczaj prawdziwego tokenu w notebookach ani w repozytorium.

Przykładowe utworzenie połączenia:

```python
import os
from qiskit_ibm_runtime import QiskitRuntimeService

kwargs = {
    "channel": "ibm_quantum_platform",
    "token": os.environ["IBM_QUANTUM_TOKEN"],
}

instance = os.getenv("IBM_QUANTUM_INSTANCE")
if instance:
    kwargs["instance"] = instance

service = QiskitRuntimeService(**kwargs)
```

## Test z terminala

Po uruchomieniu kontenera można wykonać:

```bash
docker compose exec quantum-lab python /workspace/scripts/check_environment.py
```

## Zakres laboratoriów

Katalog `notebooks/` zawiera przygotowane miejsca na 7 tematów:

1. podstawy Qiskit i bramki,
2. BB84,
3. splątanie i E91,
4. algorytm Shora,
5. algorytm Grovera,
6. korekcja błędów kwantowych,
7. RSA / kryptografia postkwantowa.

Szczegóły pakietów i ich przeznaczenia znajdują się w `SPECYFIKACJA.md`.
