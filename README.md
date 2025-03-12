# MCnet/MCviz GSoC 2025 Evaluation Assignment

## Project Overview
This repository contains my submission for the MCnet/MCviz evaluation exercise. The assignment includes conceptual questions and practical tasks related to Monte Carlo event visualization in particle physics.

---

## Task 1: Conceptual Questions & Answers

### 1. What are the HepMC and LHE formats used for in particle physics simulations? Briefly describe their structure and key differences.

#### **HepMC (HEP Monte Carlo) Format**
- Used to store Monte Carlo (MC) event data in **high-energy physics (HEP)** simulations.
- Represents **generated events** with particles, vertices, and kinematic properties.
- **Structure:** Graph-based format (particles as nodes, interactions as edges).
- **Usage:** Typically used in **later stages** of event generation, especially for detector simulations.

#### **LHE (Les Houches Event) Format**
- Used to store **parton-level events** from MC generators like Pythia, MadGraph, and Herwig.
- **Structure:** XML-based format, where each event contains a list of particles with their kinematic properties.
- **Usage:** Primarily used for **parton-level event generation**, before showering and hadronization.

**Key Differences:**  
| Feature        | HepMC | LHE |
|---------------|-------|-----|
| **Format**    | Graph-based | XML-based |
| **Event Stage** | Full event (including detector effects) | Parton-level only |
| **Usage**     | Detector simulations | Parton-level event storage |

---

### 2. What are the benefits of visualizing Monte Carlo events in particle physics? Name two potential use cases.

#### **Benefits:**
- Helps in **understanding event kinematics** and particle interactions.
- Useful for **debugging simulations** and verifying detector performance.
- Assists in **educational and outreach** efforts by making data accessible.

#### **Use Cases:**
1. **Particle Collision Analysis** – Visualizing jet formation, decay chains, and missing energy for physics studies.
2. **Detector Simulation Validation** – Comparing MC-generated events with experimental data to refine detector response models.

---

### 3. What is the purpose of jet clustering in particle physics? Name one common jet clustering algorithm.

#### **Purpose of Jet Clustering:**
- High-energy collisions produce quarks and gluons, which hadronize into **jets**.
- Jet clustering algorithms **group final-state particles into jets** to study their properties.
- Important for identifying **quark/gluon origins**, reconstructing **heavy particles (e.g., top quarks, Higgs boson)**.

#### **Common Jet Clustering Algorithm:**
- **kT Algorithm** – A sequential clustering method where particles are merged based on their relative transverse momentum.
- Other examples: **Cambridge/Aachen**, **Anti-kT (widely used in LHC analyses)**.

---

### 4. Explain how JSON or a similar structured format could be useful when transmitting event data from a server to a web visualization tool.

#### **Why JSON?**
- **Lightweight & Readable:** Easy to parse and transmit over HTTP.
- **Structured Data:** Stores particle properties (ID, momentum, energy) in a hierarchical format.
- **Interoperability:** Can be directly used in JavaScript (e.g., D3.js, Plotly) for visualization.

#### **Example JSON Event Data Structure:**
```json
{
  "event_id": 1,
  "particles": [
    {"id": 6, "px": 100.0, "py": 50.0, "pz": 200.0, "energy": 250.0},
    {"id": -6, "px": -100.0, "py": -50.0, "pz": -200.0, "energy": 250.0}
  ]
}
```
- The **front-end JavaScript** can fetch this JSON and visualize the event as a node-edge diagram or scatter plot.

---

## Task 2: Practical Tasks

### **Task 2a & Task 2b: Jupyter Notebook Implementation**
- **Goal:** Parse an LHE file, extract statistics, and visualize events.
- **Implementation:** The tasks have been implemented in a Jupyter Notebook.
- **Notebook File:** [`task_2a_2b.ipynb`](task_2a_2b.ipynb)

### **Task 2c: Basic Web Rendering**
- **Goal:** Build a Flask-based web server to serve event data.
- **Steps:**
  - Read a JSON file representing an event from the LHE data.
  - Serve the JSON via an API endpoint (`/event`).
  - Use JavaScript (D3.js, Three.js, or Plotly) to visualize the event in a web browser.

---

## Setup & Installation
- Task2a and Task2b solution can be found in task2a_2b.ipynb file in repo


Bonus task recording below :-



https://github.com/user-attachments/assets/671df86c-bf8e-4622-ae6d-7c044fa222e2


- To run the Task2c, you will need Python and the following libraries:
```sh
pip install flask flask-cors
```

### **Run Task 2c:**
 Flask Web Server
```sh
python server.py
```
Then open `http://127.0.0.1:5000/event` in your browser.

Demo output is shown in below recording :)



https://github.com/user-attachments/assets/4ade7895-84a7-4d1d-bf38-db8fd96364c7



Frontend code is wrriten in index_2c.html and can be accessed through it :)

---


