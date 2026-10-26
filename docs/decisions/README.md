# Decisions

Durable record of team decisions — the `[DECIDE]` items from the CONOPS and elsewhere. This is one of the two things we keep a lasting record of (the other is regulatory verifications in `../regulatory/`). See `../working-with-agents.md`.

## Why this exists
A low-contact team can't afford to re-discuss settled questions. Recording a decision once — with the reasoning — means it's closed asynchronously and stays closed. Without this, decisions live in chat and get lost, forcing another meeting.

## How to record a decision
Keep it short. One decision per entry. Either one file per decision (`YYYY-MM-DD-<topic>.md`) or append a row below — whichever the team prefers. Use **roles, not names** (public-repo rule).

Each entry captures:
- **Decision** — what was chosen.
- **Question** — the `[DECIDE]` item it closes.
- **Why** — one or two lines of rationale; alternatives rejected.
- **Date** — ISO `YYYY-MM-DD`.
- **Owner** — the role that owns it.
- **Depends on** — any `[VERIFY]` finding it relied on (if applicable).

After recording, go back to the source doc (e.g. the CONOPS) and replace the inline `[DECIDE: …]` tag with the decided text plus a link to the entry here.

## Log

| Date | Decision | Closes | Why | Owner |
|------|----------|--------|-----|-------|
| 2026-10-26 | Sensor baseline = Option B (AIS + radar + 360° EO/IR + basic environmental sensor) — [brief](2026-10-26-sensor-baseline.md) | CONOPS §3 sensor baseline | smallest suite covering all four missions; hydrophone/LiDAR as growth options | remote-ops lead |
| _(proposed)_ | CONOPS template/standard — [brief](2026-10-26-conops-template.md) | CONOPS document structure | awaiting team confirmation; proposed EMSA RBAT + IMO autonomy-degree hybrid | remote-ops lead |

## Open decisions (from the CONOPS, for reference)
These are still open — search the source docs for the authoritative inline tags. Listed here only as a pointer, grouped by what they wait on.

### Decide FIRST (gating — unblocks the rest)
- **CONOPS template/standard** — *PROPOSED, decide now* (brief: `2026-10-26-conops-template.md`). **Gating:** it sets the document structure all other CONOPS decisions are recorded against. Closing other decisions before this risks structural rework. Decide this before spending effort on the items below.

### Can decide now (once the template is confirmed)
- Lost-link policy (brief: `2026-10-26-lost-link-policy.md`)
- Geographic operating boundary
- Operating envelope (sea-state / visibility / ice thresholds)
- Surveillance → enforcement handoff boundary
- Support concept / deployment cadence
- Cyber-security concept baseline
- One-slide summary owner

### Blocked on the regulatory ceiling (`[VERIFY]` must land first)
- Operator model (Port of Göteborg as owner/operator)
- Operator-to-vessel ratio
- Which decisions must always require a human
- Target autonomy degree (IMO Degree 3 assumed, provisional)

### Decided
- ~~Sensor baseline~~ — **DECIDED 2026-10-26** (Option B), see log above
