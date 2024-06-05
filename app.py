import streamlit as st
import time
from qiskit import QuantumCircuit, Aer, execute


def create_quantum_circuit(num_qubits):
    qc = QuantumCircuit(num_qubits, num_qubits)
    qc.h(range(num_qubits))
    qc.measure(range(num_qubits), range(num_qubits))
    return qc


def run_quantum_circuit(qc):
    backend = Aer.get_backend("qasm_simulator")
    job = execute(qc, backend, shots=1)
    result = job.result()
    counts = result.get_counts()
    outcome = list(counts.keys())[0]
    return int(outcome, 2), outcome


def quantum_random_number_generator(max_number):
    num_qubits = max_number.bit_length()
    while True:
        qc = create_quantum_circuit(num_qubits)
        random_number, binary_outcome = run_quantum_circuit(qc)
        if 1 <= random_number <= max_number:
            return (
                random_number,
                binary_outcome,
            )


def display_steps(max_number, final_number, binary_outcome):
    num_qubits = max_number.bit_length()
    progress_bar = st.progress(0)

    st.write("Generating quantum states...")
    progress_bar.progress(20)
    time.sleep(1)

    st.write(f"Creating {num_qubits} qubits...")
    progress_bar.progress(40)
    time.sleep(1)

    st.write(f"Creating {num_qubits} classical bits...")
    progress_bar.progress(60)
    time.sleep(1)

    st.write("Putting qubits into superposition states using Hadamard gates...")
    progress_bar.progress(80)
    time.sleep(1)

    st.write("Measuring qubits...")
    progress_bar.progress(100)
    time.sleep(1)

    st.write(f"The final number generated is: {final_number} ({binary_outcome})")


st.title("Quantum Random Number Generator")
st.subheader("By Block-S Dev Team for Lunch")
max_number = st.number_input(
    "Enter the maximum number (n):", min_value=1, max_value=9999, value=4
)

if st.button("Generate Random Number"):
    random_number, binary_outcome = quantum_random_number_generator(max_number)
    display_steps(max_number, random_number, binary_outcome)


with st.expander("View Code"):
    code = """
def create_quantum_circuit(num_qubits):
    qc = QuantumCircuit(num_qubits, num_qubits)
    qc.h(range(num_qubits))
    qc.measure(range(num_qubits), range(num_qubits))
    return qc


def run_quantum_circuit(qc):
    backend = Aer.get_backend("qasm_simulator")
    job = execute(qc, backend, shots=1)
    result = job.result()
    counts = result.get_counts()
    outcome = list(counts.keys())[0]
    return int(outcome, 2), outcome


def quantum_random_number_generator(max_number):
    num_qubits = max_number.bit_length()
    while True:
        qc = create_quantum_circuit(num_qubits)
        random_number, binary_outcome = run_quantum_circuit(qc)
        if 1 <= random_number <= max_number:
            return (
                random_number,
                binary_outcome,
            )
    """
    st.code(code, language="python")
