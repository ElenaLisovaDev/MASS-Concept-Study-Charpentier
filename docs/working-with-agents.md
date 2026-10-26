# How we work with agents

A one-page working agreement for a small team with little meeting time. It covers **who reviews what, how much review each thing needs, and where decisions and verifications are recorded** — so most work happens asynchronously and we only meet at natural checkpoints.

This complements `CONTRIBUTING.md` (which says *where files go*). This file says *how work flows*.

---

## 1. Review by risk, not everything the same

Don't review all agent output with the same effort. Match the review to the risk.

| Risk tier | What it covers | Review needed |
|-----------|----------------|---------------|
| **Low** (reversible) | Draft text, scenario write-ups, summaries, formatting, structure | Agent produces it; author glances and commits. No sign-off. |
| **Moderate** | Requirements drafts, architecture notes, trade-study inputs | One reviewer (the owning role) reads before it's relied on. |
| **High** (regulated / safety / legal / irreversible) | Regulatory findings (`[VERIFY]`), safety-authority decisions, anything claiming "legal today" | Mandatory human sign-off by the owning role. Never relied on as raw agent output. |

The point: spend the team's scarce attention on the high-risk items. Let agents carry the reversible bulk.

## 2. One reviewer per artifact type

Review works async when it's clear *who* reviews *what* and *what "good" means* — not "whoever is free." Each artifact type has one owning role (see `project/Team-Responsibilities.md`):

| Artifact | Owning role | "Done when…" |
|----------|-------------|--------------|
| Regulatory compliance matrix / findings | regulatory lead | every claim has a citation and a verdict (permissible / not / conditional) |
| CONOPS | remote-ops lead | no open `[VERIFY]`/`[DECIDE]`, scenarios + roles present |
| Requirements | systems lead | each `REQ-MASS-xxx` traces to a regulation or CONOPS statement |
| Architecture / SysML | systems lead | consistent with requirements, traceable |

If an item has no clear owner, that's the signal to assign one — not to call a meeting.

## 3. Gate at checkpoints, not continuously

Work runs in parallel between checkpoints. We sync at the stage boundaries that already exist in `project/Project-Timeline.md` (e.g. sponsor workshop 2026-11-24, midpoint 2026-12-08). A stage is "approved to build on" at its checkpoint — we don't re-approve every edit in between.

Natural stage order (from `project/Agentic-Engineering-Approach.md`): Regulatory → Requirements → Architecture → Design → Visualization → UI. CONOPS develops in parallel with regulatory and feeds it.

## 4. Record only the two things that must be durable

Most work needs no tracking. Only two kinds of outcome must survive as a record, because they're high-risk and others depend on them:

- **Verifications** (`[VERIFY]`) → the reviewed answer lives in `docs/regulatory/` with a citation and a verdict. One line noting the agent run it came from (`Source: regulatory_agent run YYYY-MM-DD, reviewed by <role>`).
- **Decisions** (`[DECIDE]`) → recorded in `docs/decisions/` as a short entry: the question, the choice, one line of why, the date, the owning role. One file or one row per decision.

Everything else is just the artifact in its folder. No separate tracker to maintain.

## 5. The open-item convention (lightweight)

Open questions are marked inline in the doc where they live:

- `[VERIFY: <topic>]` — a fact to confirm (regulatory/legal). Closed via the regulatory agent → `docs/regulatory/`.
- `[DECIDE: <topic>]` — a team choice. Closed via a `docs/decisions/` entry.

To see what's open, search the repo for `[VERIFY` / `[DECIDE`. When an item closes, replace the inline tag with the decided text + a link to where the answer lives. The tag disappearing *is* the status update — no register to sync.

> If the team later finds search-the-repo isn't enough, upgrade to GitHub Issues with `verify`/`decide` labels (status comes free from the tool) rather than a hand-maintained table.

## 5a. Exact steps to close an item

Closing an item means propagating one outcome to a few places **in a single commit** so nothing drifts. These are the canonical procedures — any agent (IDE assistant or teammate) applies them when given an outcome. The human supplies the *judgement* (the choice/verdict); the agent does the *propagation*.

### Closing a `[DECIDE]`
Given an outcome like "sensor baseline = Option B, confirmed by remote-ops lead":
1. **Source doc** — find the inline `[DECIDE: <topic>]` tag and replace it with the decided text + a link to the decision record. (This is the step most easily forgotten; it's what removes the item from a repo search.)
2. **Decision record** (`docs/decisions/…`) — record the outcome: chosen option, one line of why, confirming role, ISO date. If a brief exists, flip its status to `DECIDED` and fill its Decision block; otherwise add a row to the log in `docs/decisions/README.md`.
3. **Log + open list** (`docs/decisions/README.md`) — add the log row and strike the item from the open-decisions list.
4. **Verify the close** — search the source doc for the old `[DECIDE: <topic>]`; it must return nothing. Then scan for *prose* mentions of the item (e.g. in a "next steps" list) and update any that are now stale — automated tag-matching won't catch those, so this needs a human/agent judgement pass.

### Closing a `[VERIFY]`
Given a reviewed regulatory finding:
1. **Source doc** — replace the inline `[VERIFY: <topic>]` tag with the confirmed statement + a link to the finding in `docs/regulatory/`.
2. **Finding** (`docs/regulatory/…`) — record the verdict (permissible / not / conditional), the citation, and a `Source: <agent> run YYYY-MM-DD, reviewed by <role>` line.
3. **Verify the close** — search the source doc for the old `[VERIFY: <topic>]`; it must return nothing. Check for dependent items: if this finding unblocks a `[DECIDE]` (e.g. an autonomy-level decision), note that the blocked item can now proceed.

### Rules for any agent doing this
- **One commit per close** — source doc + record + log move together, so the repo is never half-updated.
- **Never close on your own authority.** A `[DECIDE]` needs the team's choice; a `[VERIFY]` needs a human-reviewed finding. Agents propagate outcomes, they don't originate them.
- **Always do step "verify the close."** A stale tag left behind is the one failure mode this whole convention exists to prevent.
- **Roles, not names** in every record (public-repo rule).

## 6. The principle

Agents handle volume and drafting. Humans own direction, verification of high-risk claims, and decisions. Keep bookkeeping near zero — the scarce resource is human attention, so spend it on judgement, not status-keeping.
