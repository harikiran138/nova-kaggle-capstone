# Nova – Multi-Agent Autonomous System (Kaggle Edition)

## Overview
Nova is a lightweight, deterministic multi-agent system designed to run entirely within a Kaggle notebook environment. It demonstrates the core concepts of agentic workflows—routing, code generation, research, and self-correction—without relying on external LLM APIs or internet access.

## Agents
1.  **Supervisor**: The brain of the operation. It analyzes incoming tasks and routes them to the appropriate specialist agent.
2.  **Coder**: Specialized in generating Python code. For this demo, it uses deterministic templates to solve specific algorithmic tasks.
3.  **Researcher**: A retrieval agent that scans local documentation (`docs.txt`) to answer information-seeking queries.
4.  **Fixer**: An autonomous debugging agent that identifies and repairs syntax errors in existing code files.

## Architecture
The system follows a star topology where the Supervisor acts as the central hub.
- **Input**: `data/tasks.json` containing a list of tasks.
- **Process**: `Nova` pipeline iterates through tasks -> Supervisor routes -> Agent executes.
- **Output**: Execution results and an evaluation report (`results.csv`).

## How to Run
1.  Open the `notebooks/nova_capstone.ipynb` in Kaggle.
2.  Ensure the `src/` and `data/` folders are uploaded or created in the working directory.
3.  Run all cells.
4.  View the final `results.csv` for the performance report.

## Evaluation Metrics
The system is evaluated based on:
- **Success Rate**: Percentage of tasks correctly completed.
- **Correctness**: Verified by running generated code (for Coder), checking string matches (for Researcher), and re-running fixed files (for Fixer).
