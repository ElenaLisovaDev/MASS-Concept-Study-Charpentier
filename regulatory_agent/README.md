# Regulatory Agent

The **Regulatory Agent** — one of the five agentic roles defined for this project (see `../project/Agentic-Engineering-Approach.md`).

## What it does
A [crewai](https://github.com/crewAIInc/crewAI) program (`run_regulatory_agent_crew.py`) that uses a Gemini LLM as a "Senior Maritime Regulatory Compliance Specialist". It reviews maritime regulations (IMO MASS Code, COLREGs, SOLAS, EU, NATO), extracts requirements, and writes them to `requirements/compliance_matrix.md`.

Its place in the workflow is **Regulatory Analysis → Requirements Derivation**: it produces the first-cut compliance matrix that feeds `../docs/regulatory/` and `../docs/requirements/`.

## How to run
1. Set up the environment: `bash setup.sh` (macOS/Linux) or `.\setup.ps1` (Windows).
2. Copy `../.env.example` to `../.env` and set `GEMINI_API_KEY`.
3. Run: `python run_regulatory_agent_crew.py`

Output is written to `requirements/compliance_matrix.md` (overwritten on each run).

## Inputs
Currently the agent fetches context files (approach, readme, team responsibilities) from `https://github.com/draronnax83-cmd/MASS-Concept-Study-Charpentier`. Those files are now mirrored locally in `../project/` — a future improvement is to read the local copies instead, removing the network dependency and giving a single source of truth.

## Known issues / TODOs
- **Scenario mismatch:** the agent prompt currently describes a "24 m civilian submarine in Göteborg harbour", but this study is an **Uncrewed Surface Vessel (USV)**. Update the role/goal/task text in `run_regulatory_agent_crew.py` to the USV scenario before trusting the output.
- All AI-generated output must be reviewed by an engineer before use.
