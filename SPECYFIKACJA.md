# Specyfikacja środowiska laboratoryjnego

## Przeznaczenie

Jedno, wspólne środowisko Docker do całego cyklu 7 laboratoriów z przedmiotu
**Podstawy kryptografii kwantowej**. Założenie: podczas semestru studenci nie
powinni wykonywać dodatkowych `pip install` wewnątrz notebooków.

## Warstwa bazowa

- Python 3.12
- Debian Bookworm Slim
- JupyterLab 4.x
- kernel: `Python 3.12 (Qiskit)`
- port JupyterLab domyślnie: `127.0.0.1:8888`
- notebooki i dane przechowywane poza kontenerem przez bind mount

## Wersje bazowe (stan na 30.09.2026)

- Qiskit 2.5.2
- Qiskit Aer 0.17.2
- qiskit-ibm-runtime 0.50.0
- qiskit-algorithms 0.4.0
- cryptography 50.0.1

Wersje kluczowych bibliotek są przypięte w `requirements.txt`, aby współpracownicy budowali możliwie identyczne środowisko.

## Pakiety Python

| Pakiet | Rola w kursie |
|---|---|
| `qiskit` | obwody, bramki, Statevector, transpilacja, podstawowy model programowania kwantowego |
| `qiskit-aer` | lokalna symulacja, pomiary wielokrotne, modele szumu i ćwiczenia z korekcji błędów |
| `qiskit-ibm-runtime` | uruchamianie obwodów na IBM Quantum Platform |
| `qiskit-algorithms` | opcjonalna warstwa wysokopoziomowa, m.in. Grover; pakiet społecznościowy, nie jest już oficjalnie wspierany przez IBM |
| `numpy` | wektory, macierze, amplitudy i obliczenia numeryczne |
| `scipy` | dodatkowe obliczenia numeryczne wykorzystywane przez stos naukowy |
| `pandas` | zestawienia wyników i analiza danych; przydatne m.in. przy Shorze i eksperymentach statystycznych |
| `sympy` | arytmetyka symboliczna, liczby pierwsze, NWD i pomocnicza matematyka dla RSA/Shora |
| `matplotlib` | histogramy i wykresy |
| `pylatexenc` | obsługa renderowania obwodów Qiskit w notebookach |
| `cryptography` | przykłady kryptografii klasycznej i współczesnych mechanizmów postkwantowych |
| `jupyterlab`, `ipykernel`, `ipywidgets` | środowisko pracy notebookowej |

## Pokrycie 7 laboratoriów

| Laboratorium | Główne składniki środowiska |
|---|---|
| 1. Podstawy Qiskit i bramki | Qiskit, NumPy, Aer, Matplotlib, IBM Runtime |
| 2. BB84 | Qiskit, Aer, NumPy |
| 3. Splątanie i E91 | Qiskit, Aer, NumPy, Matplotlib |
| 4. Shor | Qiskit, IBM Runtime, NumPy, pandas, SymPy |
| 5. Grover | Qiskit, Qiskit Algorithms, Aer / IBM Runtime |
| 6. Korekcja błędów | Qiskit, Qiskit Aer i `qiskit_aer.noise` |
| 7. RSA / PQC | SymPy, cryptography, Qiskit jako kontekst ataku kwantowego |

## Celowo niewłączone biblioteki

Środowisko nie zawiera osobnych frameworków Cirq, PennyLane, Stim ani `qiskit-qec`.
Zakres kursu można zrealizować w jednym stosie Qiskit, co ogranicza liczbę zależności,
czas budowania oraz ryzyko konfliktów wersji.

## Bezpieczeństwo

- JupyterLab jest publikowany tylko na `127.0.0.1` hosta.
- Token IBM Quantum nie powinien znajdować się w notebooku ani repozytorium.
- `.env` jest ignorowany przez Git.
- domyślny `JUPYTER_TOKEN` z `.env.example` należy zmienić w środowiskach innych niż lokalne laboratorium.

## Uwagi eksploatacyjne

Pierwsze zbudowanie obrazu wymaga dostępu do Internetu, ponieważ `pip` pobiera
pakiety z repozytoriów. Po zbudowaniu obrazu część laboratoriów może działać offline.
Dostęp do rzeczywistego QPU IBM zawsze wymaga połączenia z Internetem i aktywnego
konta/uprawnień po stronie IBM Quantum Platform.

Jeżeli potrzebne będzie wdrożenie całkowicie offline, należy przygotować osobno
wyeksportowany obraz Dockera (`docker save`) albo lokalny katalog wheel-i Python.


## Uwaga o qiskit-algorithms

Pakiet `qiskit-algorithms` 0.4.0 jest dołączony jako wygodna, opcjonalna warstwa do demonstracji algorytmów takich jak Grover. Projekt nie jest już oficjalnie wspierany przez IBM, dlatego zasadnicze ćwiczenia powinny pozostać możliwe do wykonania bez uzależniania całego kursu od tego pakietu.
