# Decision brief — Sensor baseline

**Status:** DECIDED · **Date:** 2026-10-26 · **Owner:** remote-ops lead
**Closes:** `[DECIDE]` sensor baseline (CONOPS §3, §8)
**Depends on:** none — this is decidable now (not blocked on the regulatory ceiling)

> This is a brief, not a settled decision. It frames options and a recommendation so the team can confirm asynchronously. To close: pick an option, fill in **Decision** below, add the row to the log in `README.md`, and replace the inline `[DECIDE]` tag in the CONOPS with the chosen baseline + a link here.

## Question
What sensing suite should the concept carry to support the four surveillance missions (criminal activity, infrastructure security, environmental monitoring, general safety) in a dense harbour environment?

## What the missions demand (from CONOPS §3)
- **Detect/track vessels and small craft** day and night, including non-cooperative targets.
- **Situational awareness in a dense AIS/radar environment** feeding the shore operator and VTS.
- **Environmental indicators** — spills, discharge, debris.
- **Intrusion/anomaly detection** near terminals and subsea assets.

## Options

### Option A — Minimal cooperative baseline
AIS receiver + navigation radar + single EO/IR camera.
- **Pro:** cheapest, simplest integration, lowest data/comms load, fastest to prototype.
- **Con:** weak on non-cooperative small-craft detection; limited environmental sensing; single camera = coverage gaps.
- **Fits:** a stripped concept demonstrator, not the stated mission set.

### Option B — Balanced surveillance baseline (recommended)
AIS receiver + navigation/solid-state radar + 360° EO/IR camera suite + basic environmental sensor (oil-sheen/turbidity or water-quality probe).
- **Pro:** covers all four missions at concept level; EO/IR + radar gives day/night non-cooperative detection; environmental sensor addresses mission 3; maps cleanly to sensor-fusion AI in CONOPS §6.
- **Con:** more integration and data load; environmental sensing is indicative, not laboratory-grade.
- **Fits:** the mission set as written — the defensible concept baseline.

### Option C — Extended baseline
Option B + acoustic/hydrophone array + LiDAR for close-range docking/intrusion.
- **Pro:** strongest intrusion and subsea-adjacent sensing; richest fusion demonstrator.
- **Con:** highest cost, data, and integration burden; hydrophone value in a noisy harbour is uncertain; risks over-scoping a concept study.
- **Fits:** if the team wants to showcase advanced fusion, accept the extra scope.

## Recommendation
**Option B.** It's the smallest suite that credibly covers all four stated missions and lines up with the AI sensor-fusion concept already in §6. Treat the hydrophone/LiDAR from Option C as **future growth options**, not the baseline, to avoid over-scoping a concept study.

## Decision
- **Chosen option:** Option B — balanced surveillance baseline (AIS + navigation/solid-state radar + 360° EO/IR camera suite + basic environmental sensor).
- **Rationale / any adjustments:** smallest suite that credibly covers all four missions and aligns with the AI sensor-fusion concept in §6. Hydrophone/LiDAR held as future growth options to avoid over-scoping the concept study.
- **Confirmed by (role):** remote-ops lead
- **Date:** 2026-10-26
