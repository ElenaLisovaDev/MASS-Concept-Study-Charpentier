# MASS-Concept-Study-Charpentier

Working repository for the 2026–2027 **Maritime Autonomous Surface System (MASS) Concept Study** at Charpentier Shipyard: a concept-level **Uncrewed Surface Vessel (USV)** developed with a Model-Based Systems Engineering (MBSE) approach, supported by AI agentic-engineering workflows.

The full project definition (vision, challenge, workflow, team responsibilities, timeline) is mirrored in [`project/`](project/) so the whole team works from one place. Start with [`project/Readme.md`](project/Readme.md).

## Repository structure

| Path | Contents |
|------|----------|
| `project/` | Project definition: overview, agentic approach, team responsibilities, timeline |
| `regulatory_agent/` | Regulatory Agent (crewai) — regulation review → compliance matrix. See its README |
| `docs/regulatory/` | Compliance matrix, gap analysis |
| `docs/requirements/` | Requirements repository and traceability |
| `docs/conops/` | Concept of operations (operator workflows, remote supervision) |
| `docs/architecture/` | System/functional/logical architecture, SysML exports |
| `docs/verification/` | Verification strategy and matrix |
| `models/sysml/` | SysML models (SysON) |
| `models/cad/` | FreeCAD models, assemblies, trade studies |
| `visualization/` | Blender renders, animations, visual assets |
| `ui/` | Lovable UI / digital-twin dashboard prototypes |
| `presentations/` | Check-in and final-demo decks |
| `reports/` | Technical reports and formal deliverables |

Each folder has a short README describing what goes in it. **Before adding files, read [`CONTRIBUTING.md`](CONTRIBUTING.md)** — it defines where everything is stored, naming conventions, LFS rules, and how to handle agent output.

### Large files (Git LFS)

Binary deliverables (CAD, Blender, images, Office docs, PDF, video) are tracked with **Git LFS** — see `.gitattributes`. Each teammate must run `git lfs install` once per machine (Git LFS ships with Git for Windows). After that, LFS files are handled transparently on clone/pull/push. Note: GitHub's free LFS quota is limited (1 GB storage, 1 GB/month bandwidth) — keep an eye on usage and avoid committing throwaway renders.

## Requirements

- **Python 3.11** (recommended; see `.python-version`). 3.11 is chosen because `requirements.txt` includes `cryptography`, which can be painful to build from source on newer Python.
- `pip`
- A Google AI / Gemini API key

## Setup

### macOS / Linux
```bash
cd regulatory_agent
bash setup.sh
```

### Windows (PowerShell)
```powershell
cd regulatory_agent
.\setup.ps1
```
If PowerShell blocks script execution, run this once in the session:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Both scripts create a `.venv` (if missing), activate it, install `certifi`, point the SSL bundle paths at it (needed behind the corporate proxy), and install `requirements.txt`.

## Configure your API key

1. Copy the example file:
   - macOS/Linux: `cp .env.example .env`
   - Windows: `Copy-Item .env.example .env`
2. Open `.env` and set `GEMINI_API_KEY=...` with your key.
3. Make sure the key is available in your environment when running. crewai/litellm loads `.env` automatically in most setups; if yours doesn't, export it in your shell (`export GEMINI_API_KEY=...`) or add `python-dotenv` with a `load_dotenv()` call to `run_regulatory_agent_crew.py`.

`.env` is gitignored — never commit it.

## Run

```bash
cd regulatory_agent
python run_regulatory_agent_crew.py
```

The agent fetches context from GitHub, analyses the regulations, and writes the result to `regulatory_agent/requirements/compliance_matrix.md`.

> Note: the script fetches its context files from a separate GitHub repo (`draronnax83-cmd/MASS-Concept-Study-Charpentier`). Make sure those files (`Agentic-Engineering-Approach.md`, `Readme.md`, `Team-Responsibilities.md`) exist there before running.

## Working together

We're a small team and work mostly directly on `main`. A few habits keep it smooth:

- **Pull before you start, and again before you push.**
- **Don't push code that doesn't run.** If a change is big or half-done, make a short-lived branch (`git switch -c my-thing`), finish it, merge it back to `main`.
- **Never force-push to `main`** (`git push --force`) — it can erase someone else's commits.
- Keep commits small and messages clear.
- Branch naming: `feat/...`, `fix/...`, or `<initials>/<topic>`.

## Secrets & hygiene

- Never commit API keys, passwords, or local config. `.env` is gitignored; only `.env.example` is committed.
- The `.gitignore` excludes virtual envs (`.venv`), `__pycache__`, OS files, and `.env`.

## Repo settings (for the repo owner)

One-time setup to keep the team safe:

1. **Add collaborators** — Settings → Collaborators → add each teammate with **Write** access.
2. **Protect `main` from force-push** — Settings → Branches → add a rule for `main` → enable "Do not allow force pushes" and "Do not allow deletations". (No PR requirement — we agreed on direct-to-main for a small team.)
3. **Visibility** — the repo is currently public. Confirm that's intended given the content; if anything is sensitive, switch to private (Settings → General → Danger Zone).
4. **Check history for leaked secrets** — scan past commits for API keys before widening access. If a key was ever committed, rotate it and scrub the history.
