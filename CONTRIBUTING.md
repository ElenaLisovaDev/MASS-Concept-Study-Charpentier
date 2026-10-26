# Contributing & file-storage rules

This repo is the single shared workspace for the MASS Concept Study (USV). To keep five people across companies from stepping on each other, follow these rules for **where things go**, **how to name them**, and **how to handle agent output**.

If you're unsure where something belongs, check the table below or ask in the team channel before committing.

---

## 1. Where things go

Store by **deliverable type**, not by who made it or when. Each folder has its own README describing its contents.

| What you have | Where it goes |
|---------------|---------------|
| Project definition (approach, timeline, responsibilities) | `project/` — reference only, don't edit except to sync from source |
| Agent code (crewai scripts, setup, requirements) | `regulatory_agent/` (and future `*_agent/` folders) |
| Regulatory compliance matrix, gap analysis | `docs/regulatory/` |
| Requirements repository, traceability tables | `docs/requirements/` |
| CONOPS, operational scenarios, use cases | `docs/conops/` |
| Architecture descriptions, SysML exports (as docs) | `docs/architecture/` |
| Verification plan, verification matrix, test results | `docs/verification/` |
| SysML model files (from SysON) | `models/sysml/` |
| FreeCAD files, STEP/IGES/STL exports, trade studies | `models/cad/` |
| Blender files, renders, animations, visual assets | `visualization/` |
| Lovable/UI mockups, prototype exports, dashboards | `ui/` |
| Slide decks (check-ins, final demo) | `presentations/` |
| Technical reports, formal deliverables | `reports/` |

### General placement rules
- **One home per artifact.** Don't duplicate the same file into two folders. If two areas need it, keep the source in its type folder and reference it from the other.
- **Documents (`docs/...`) hold the reviewed, human-owned artifacts.** Models go in `models/`, not in `docs/`.
- **Don't create new top-level folders** without agreeing with the team first — it fragments the structure.
- **No personal scratch folders** in the repo (e.g. `my-notes/`, `tmp-<initials>/`). Use your own machine for scratch work; commit only shareable deliverables.
- **Don't commit generated environments or secrets** — `.venv/`, `__pycache__/`, `.env`, and `.kiro/` are already gitignored. Never commit API keys.

---

## 2. Naming conventions

Keep names predictable so files sort and search well.

- Lowercase, words separated by hyphens: `hull-trade-study.md`, not `Hull Trade Study (final) v2.docx`.
- No spaces or special characters in filenames (spaces break some tooling and LFS workflows).
- Dates as ISO `YYYY-MM-DD` when a date matters: `2026-11-24-sponsor-workshop.pptx`.
- Avoid `final`, `final2`, `latest` in names — git history is the version record. If you must mark a baseline, use a clear tag like `-baseline` or a git tag.
- Requirement IDs follow the agent's convention: `REQ-MASS-001`, `REQ-MASS-002`, …

---

## 3. Large / binary files (Git LFS)

Binary deliverables are tracked with **Git LFS** (see `.gitattributes`): CAD, Blender, images, Office docs, PDF, video.

- **One-time per machine:** run `git lfs install` (Git LFS ships with Git for Windows).
- After that, LFS files are handled automatically on clone/pull/push.
- **Watch the quota.** GitHub's free LFS allowance is small (≈1 GB storage, 1 GB/month bandwidth for the whole repo). So:
  - Don't commit throwaway renders or intermediate exports — commit the ones that matter.
  - Prefer compressed formats (e.g. `.glb` over raw, reasonable render resolution).
  - For very large source files (multi-hundred-MB Blender scenes), consider keeping the heavy source on a shared drive and committing a smaller export + a link.

---

## 4. Running agents — where output goes

Several of us will run AI agents (regulatory, systems engineering, design, UI/UX, documentation). To keep agent output traceable and reviewable:

### Two-stage flow: raw output → reviewed deliverable

Agent output goes through two defined stages. These are two different locations with two different meanings — not a scratch folder, and not a duplicate.

**Stage 1 — Raw output (lives with the agent).**
The agent writes its unreviewed draft into its own folder, in a fixed location (e.g. the regulatory agent writes `regulatory_agent/requirements/compliance_matrix.md`; new agents use `<name>_agent/output/`). This is a *reproducible artifact*: re-running the agent regenerates it. It is **not** a deliverable, and other team members should not build on it directly. Committing it is optional — commit it only if you want the raw run to be reproducible/visible; otherwise it can stay local.

**Stage 2 — Reviewed deliverable (lives in `docs/` or `models/`).**
A human reviews the raw draft, edits/corrects it using engineering judgement, and saves the reviewed result into the matching deliverable folder (e.g. `docs/regulatory/compliance-matrix.md`). **This copy is the single source of truth** — it's what the rest of the team references and what goes into reports.

**Why two places instead of editing in `docs/` directly:**
- The raw copy stays pristine so you can always see what the agent actually produced and re-run it.
- The `docs/` copy carries human edits and is safe to depend on.
- If you edited inside the agent folder, the next agent run would overwrite your work.

**Avoiding drift (important):**
- Once promoted to `docs/`, **edit only the `docs/` copy**. Don't keep polishing the raw copy — it's a snapshot of a run, not a living document.
- In the `docs/` file, note which agent run it came from (e.g. a line like `Source: regulatory_agent run on 2026-11-05, reviewed by <initials>`). This keeps traceability without re-syncing files.
- When you re-run the agent later, treat the new raw output as a *new draft* to diff against the current `docs/` version — review the changes, then update `docs/`. Never blind-overwrite the reviewed deliverable with fresh raw output.

**Never treat raw agent output as a deliverable.** All AI-generated content must be validated by engineering judgement before it's relied on (project rule, see `project/Agentic-Engineering-Approach.md`).

### Recommended per-agent layout
When you add a new agent, mirror the regulatory agent's pattern:
```
<name>_agent/
  run_<name>_agent_crew.py   # agent code
  requirements.txt            # its Python deps
  setup.sh / setup.ps1        # environment setup
  README.md                   # what it does, how to run, where output lands
  output/ (or requirements/)  # raw agent output (reproducible, pre-review)
```
Then the reviewed result is promoted to the relevant `docs/` or `models/` folder.

### Agent configuration & secrets
- Each person uses their **own** `.env` with their **own** API key. Copy `.env.example` → `.env` and fill it in. `.env` is gitignored — never commit it or paste a key into chat, code, or a committed file.
- If an agent needs project context, point it at the local `project/` files (single source of truth) rather than external URLs where practical.
- Pin the Python version (`.python-version` = 3.11) so everyone's agent runs the same way.

### Don't commit large agent runtime artifacts
- Model caches, downloaded datasets, and `.venv/` must not be committed (already gitignored). Only commit the agent **code**, its **config example**, and the **output you intend to share**.

---

## 5. Git workflow (recap)

We work directly on `main` (small team). Keep it smooth:

- **Pull before you start, and again before you push.**
- Stage specific files (`git add path/to/file`), not `git add .`.
- Don't push code that doesn't run; use a short-lived branch for big/half-done work.
- Never force-push to `main`.
- Small commits, clear messages.

---

## 6. Quick decision guide

- "I generated this with an agent." → raw copy stays with the agent; reviewed copy goes to `docs/` or `models/`.
- "It's a CAD/Blender/image/PDF/Office file." → it's LFS-tracked; just commit it in its type folder.
- "It's a slide deck." → `presentations/`.
- "It's the formal report." → `reports/`.
- "I'm not sure." → ask the team before creating a new folder or duplicating a file.
