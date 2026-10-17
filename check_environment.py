import importlib
import os
import sys

PACKAGES = [
    ("qiskit", "qiskit"),
    ("qiskit_aer", "qiskit-aer"),
    ("qiskit_ibm_runtime", "qiskit-ibm-runtime"),
    ("qiskit_algorithms", "qiskit-algorithms"),
    ("numpy", "numpy"),
    ("scipy", "scipy"),
    ("pandas", "pandas"),
    ("sympy", "sympy"),
    ("matplotlib", "matplotlib"),
    ("cryptography", "cryptography"),
    ("jupyterlab", "jupyterlab"),
]

print("Python:", sys.version.split()[0])
failed = []

for module_name, label in PACKAGES:
    try:
        module = importlib.import_module(module_name)
        version = getattr(module, "__version__", "OK")
        print(f"{label}: {version}")
    except Exception as exc:
        failed.append((label, str(exc)))
        print(f"{label}: BLAD - {exc}")

print("IBM_QUANTUM_TOKEN:", "ustawiony" if os.getenv("IBM_QUANTUM_TOKEN") else "nieustawiony")
print("IBM_QUANTUM_INSTANCE:", "ustawiony" if os.getenv("IBM_QUANTUM_INSTANCE") else "nieustawiony")

if failed:
    print("\nNie wszystkie testy importu przeszly poprawnie.")
    for name, error in failed:
        print(f"- {name}: {error}")
    raise SystemExit(1)

# Minimalny test Qiskit + Aer
from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator

qc = QuantumCircuit(1)
qc.h(0)
state = Statevector.from_instruction(qc)
probs = state.probabilities_dict()
assert abs(probs.get("0", 0) - 0.5) < 1e-9
assert abs(probs.get("1", 0) - 0.5) < 1e-9

measured = qc.copy()
measured.measure_all()
sim = AerSimulator()
compiled = transpile(measured, sim)
counts = sim.run(compiled, shots=128).result().get_counts()
assert sum(counts.values()) == 128

print("\nQiskit Statevector: OK")
print("Qiskit Aer: OK")
print("Srodowisko gotowe do pracy.")
