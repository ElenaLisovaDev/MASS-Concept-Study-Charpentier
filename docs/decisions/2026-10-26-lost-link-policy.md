# Decision brief — Lost-link policy

**Status:** PROPOSED (awaiting team confirmation) · **Date:** 2026-10-26 · **Owner:** remote-ops lead
**Closes:** `[DECIDE]` lost-link policy (CONOPS §7, §8)
**Depends on:** none to *draft* — but the final safe-behaviour choice should be sanity-checked against the §5 "legal today" / COLREGs finding once it lands.

> This is a brief, not a settled decision. It frames options and a recommendation so the team can confirm asynchronously. To close: pick an option, fill in **Decision** below, add the row to the log in `README.md`, and replace the inline `[DECIDE]` tag in the CONOPS with the chosen policy + a link here.

## Question
When the command/control link to the shore operator is lost, what should the USV do? The policy must keep the vessel safe and predictable to other traffic in a busy harbour, without a human in direct control.

## Constraints (from CONOPS §4, §7)
- Default mode is **remotely supervised** — a human is normally on-the-loop.
- Harbour is dense mixed traffic; behaviour must be **predictable and COLREGs-consistent**.
- There is a comms concept with **primary + fallback** links, so "lost link" means both are down.
- Collision-avoidance authority normally sits with the human → lost link removes that authority.

## Options

### Option A — Immediate station-keeping / hold
On link loss, hold position (or safest local hold) and signal lost-link status.
- **Pro:** simplest, most predictable; vessel becomes a known stationary obstacle.
- **Con:** holding in a fairway or traffic lane can itself be a hazard; not always the safest spot.

### Option B — Move to nearest pre-defined safe zone, then hold (recommended)
On link loss: reduce speed, navigate autonomously to the nearest **pre-planned safe holding area** (clear of fairways/berths), hold, signal status, and attempt link re-establishment.
- **Pro:** gets the vessel out of traffic to a known-safe spot; predictable because safe zones are pre-agreed with the port/VTS; degrades gracefully.
- **Con:** requires a short autonomous transit with no human on-the-loop — must be bounded (low speed, defined corridor) and is the part to sanity-check against the COLREGs/"legal today" finding.

### Option C — Autonomous return-to-base
On link loss, autonomously navigate all the way back to the launch/recovery point.
- **Pro:** fully recovers the asset without human control.
- **Con:** longest unsupervised autonomous transit through traffic — highest regulatory and collision risk; least likely to be permissible "today."

## Recommendation
**Option B**, with a tiered fallback: attempt reconnect immediately; if still lost, transit at low speed to the nearest pre-defined safe zone and hold; escalate to the operator/VTS. Keep the autonomous leg **short, slow, and corridor-bounded**. This balances "don't be a hazard in the fairway" (rules out pure A in bad spots) against "don't make a long unsupervised transit" (rules out C).

## Flag for the verify track
The permissibility of *any* autonomous manoeuvring without a human on-the-loop ties directly to the COLREGs / "legal today" `[VERIFY]` items (CONOPS §5). Record this decision now as **provisional**, and confirm the autonomous-transit extent against the regulatory finding when it lands.

## Decision
_To be completed by the team:_
- **Chosen option:**
- **Rationale / any adjustments:**
- **Confirmed by (role):**
- **Date:**
