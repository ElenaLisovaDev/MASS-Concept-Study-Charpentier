# CONOPS Proposal — Göteborg Harbour Surveillance USV

**Status:** Draft v0.2 — for team review. Regulatory statements are drafts to be verified (see §13).
**Owner:** remote-ops lead · **Date:** 2026-10-26
**Scope:** Concept of Operations for a 24 m uncrewed surface vessel (USV) performing civil surveillance of Göteborg harbour.

> This document captures the CONOPS direction agreed in the first team discussion. It is a proposal, not a baseline. Items needing confirmation are marked **[VERIFY]** (regulatory/legal — closed via the regulatory agent → `../regulatory/`) or **[DECIDE]** (team choice — recorded in `../decisions/`). See `../working-with-agents.md` for how these close.

> **Concept-viability gate:** the whole concept depends on the §6 **"legal today"** finding. Until that closes, treat the autonomy-degree target in §5 as **provisional** and don't commit downstream effort that assumes a specific autonomy ceiling.

### Document structure
This CONOPS follows the **EMSA RBAT maritime MASS CONOPS** structure (overall description → mission → main characteristics → autonomous systems → operational roles), extended with operating environment, labelled operational scenarios, and risks for requirement traceability, and with the autonomy concept mapped to **IMO's four degrees of autonomy**. The choice of template is itself a team decision — **[DECIDE: CONOPS template/standard]** (brief: `../decisions/2026-10-26-conops-template.md`; proposed: EMSA + IMO hybrid).

> **Gating decision — decide first.** This template choice sets the structure every other CONOPS decision is recorded against. Confirm it before closing the other `[DECIDE]` items, otherwise those may need structural rework. This is a *sequencing* gate (decide-first-to-avoid-churn), distinct from the §6 regulatory gate (which blocks the *content* of the autonomy decisions).

### Revision history
| Version | Date | Change |
|---------|------|--------|
| v0.1 | 2026-10-26 | Initial team-discussion proposal. |
| v0.2 | 2026-10-26 | Restructured onto EMSA RBAT maritime CONOPS template + IMO autonomy degrees; added operating environment, operational scenarios, roles, risks, assumptions, glossary; carried sensor-baseline decision; added CONOPS-template decision. |

---

## 1. Overall description

Provide persistent, uncrewed surface surveillance of Göteborg harbour and its approaches to support port security, safety, and environmental monitoring — using a system that is **legal to operate today** under current applicable regulations, civil-use only.

The concept is a **24 m uncrewed surface vessel (USV)** — a Maritime Autonomous Surface Ship (MASS) in IMO terms — operated primarily under shore supervision, feeding a situational-awareness picture to a shore control centre and to the port's vessel traffic service (VTS).

### 1.1 Assumptions and constraints
- **Platform:** surface vessel, **not** a submarine. ~**24 m** length.
- **Legality:** must be operable **today** under current/appointed regulations — no dependence on future rulemaking. **[VERIFY]**
- **Use:** **civil only — no military** use or payloads.
- **Operator model:** Port of Göteborg (Göteborgs Hamn) assumed as concept owner/operator. **[DECIDE]** (confirm operator model)
- **Assumed available infrastructure:** shore control facility, resilient shore–ship comms, AIS/VTS coverage in the operating area. **[VERIFY]** / **[DECIDE]** as these firm up.
- **Regulatory baseline is evolving:** the IMO MASS Code has now been adopted (goal-based framework for remotely controlled/autonomous ships); "legal today" must be re-checked against the adopted Code **and** national/port permissions, not assumed to rely only on future rulemaking. **[VERIFY]**

### 1.2 Scope (in / out)
- **In scope:** the USV platform concept, its sensing/autonomy/comms concept, shore-operator workflows, the operating envelope within defined harbour limits, and the autonomy-vs-regulation feasibility mapping.
- **Out of scope (concept phase):** detailed hull/structural design (naval architecture workstream), enforcement/interdiction action (handed off to authorities — see §5), military payloads, operation outside defined harbour limits.

---

## 2. Mission description

The USV supports general port security and safety across four mission areas:

1. **Criminal activity** — detect/monitor unauthorised access, smuggling indicators, suspicious small-craft behaviour.
2. **Sabotage / security of critical infrastructure** — patrol near terminals, subsea assets, bridges; detect intrusion.
3. **Environmental monitoring** — spills, illegal discharge, water-quality indicators, debris.
4. **General safety** — man-overboard spotting support, hazard detection, situational-awareness feed to VTS/port ops.

The USV **observes and reports**; it does not interdict. Where a mission detects an actionable event (e.g. suspected criminal activity), the concept is to **hand off to the responsible authority** (Coast Guard / police / VTS) — the boundary between surveillance and enforcement is defined in §5. **[DECIDE]** confirm the surveillance/enforcement handoff boundary.

---

## 3. Main characteristics

- **Type / size:** ~24 m uncrewed surface vessel, civil surveillance configuration.
- **Operating area:** Göteborg harbour, quays, and approach channels, within defined harbour limits. **[DECIDE]** exact geographic boundary.
- **Endurance / patrol profile:** persistent patrol with station-keeping legs. **[DECIDE]** target endurance, speed range, patrol cadence.
- **Sensor baseline (decided 2026-10-26 — [see decision](../decisions/2026-10-26-sensor-baseline.md)):** AIS receiver + navigation/solid-state radar + 360° EO/IR camera suite + a basic environmental sensor (oil-sheen/turbidity or water-quality probe). Acoustic/hydrophone and LiDAR are future growth options, not the baseline. To be refined by naval architecture / systems engineering; data relayed to a shore control centre.
- **Launch / recovery & support:** home berth for launch, recovery, recharge/refuel, and maintenance. **[DECIDE]** support concept and deployment cadence.

---

## 4. Description of autonomous systems

The autonomy concept is framed against **IMO's four degrees of autonomy** so it maps cleanly onto the regulatory framework.

| IMO degree | Description | Relation to this concept |
|------------|-------------|---------------------------|
| **Degree 1** | Automated processes / decision support; seafarers on board | Not this concept (uncrewed). |
| **Degree 2** | Remotely controlled, seafarers on board | Not this concept (uncrewed). |
| **Degree 3** | Remotely controlled, **no** seafarers on board | **Closest fit** — shore operator in control/on-the-loop, no crew aboard. |
| **Degree 4** | Fully autonomous; system decides and acts by itself | **Likely not permissible today** for collision-avoidance in this traffic. **[VERIFY]** |

**Operating modes (within the Degree-3 concept):**

| Mode | Description | Use |
|------|-------------|-----|
| **Remotely operated** | Continuous human control from shore | Fallback / complex situations / dense-traffic manoeuvring |
| **Remotely supervised** (proposed default) | USV executes the mission autonomously; shore operator monitors and can intervene; human "on the loop" | Routine patrol legs, station-keeping |
| **Autonomous task execution** | Navigation, route-following, station-keeping, sensor tasking without real-time input | Bounded, low-risk legs; human retains override |

**Proposed concept:** operate primarily **remotely supervised** (IMO Degree 3), with a human operator on-the-loop able to take direct control. Autonomy handles navigation, route-following, station-keeping, and sensor tasking; the human retains authority over collision-avoidance exceptions, interaction with other vessels, and any enforcement-adjacent action. **[DECIDE]** target operator-to-vessel ratio and what decisions must always require a human.

### 4.1 Use of AI — and its limitations
**Concept phase** — *Uses:* CONOPS option generation, scenario exploration, regulatory research assistance, requirement drafting. *Limitations:* AI output can be plausible but wrong; regulatory interpretation must be human/expert-validated.
**Design phase** — *Uses:* parametric trade studies, design-space exploration, consistency checks, documentation drafting. *Limitations:* engineering validity must be verified; AI lacks certified physics/classification authority; results need traceability and review.
**Operation phase** — *Uses:* sensor data fusion, anomaly/threat detection, situational-awareness aids, route optimisation, alert prioritisation. *Limitations:* safety-critical decisions (collision avoidance, enforcement) need human authority; perception can fail in edge conditions (weather, occlusion, spoofing); explainability/accountability requirements; cyber-security of autonomy and comms links; regulatory acceptance of AI in safety functions is immature. **[VERIFY]**

**Guiding principle:** AI augments the engineer and operator; it does not hold final authority over safety-critical or legal decisions.

### 4.2 Communications & shore control
- Shore control centre with the on-the-loop operator(s).
- Resilient comms link (primary + fallback) with defined **lost-link behaviour** (e.g. safe station-keeping / return / hold). **[DECIDE]** lost-link policy (brief: `../decisions/2026-10-26-lost-link-policy.md`).
- Cyber-security for command/control and sensor data — treated as a first-class concern given a remotely-commanded autonomous asset (threats: command spoofing, sensor spoofing/jamming, data interception). **[DECIDE]** cyber-security concept baseline.

---

## 5. Operational roles

| Role | Responsibility | Authority boundary |
|------|----------------|--------------------|
| **Shore operator (on-the-loop)** | Monitor the USV, take direct control when needed, authorise collision-avoidance exceptions | Holds final authority over safety-critical manoeuvres and any enforcement-adjacent action |
| **Port operations / VTS** | Receive situational-awareness feed; coordinate with harbour traffic | Owns harbour traffic picture; USV is a contributor, not a controller |
| **Responsible authorities (Coast Guard / police)** | Receive handoff of actionable events; conduct any enforcement/interdiction | Enforcement authority — the USV never acts here |
| **Maintenance / support** | Launch/recovery, recharge/refuel, upkeep | Platform availability |

**Surveillance → enforcement handoff:** the USV detects and reports; when an event warrants action, the shore operator escalates to the responsible authority. The USV performs no interdiction. **[DECIDE]** confirm this boundary and the escalation path (ties to §2).

**Operator-to-vessel ratio:** to be studied; blocked on the autonomy/regulatory finding (§6). **[DECIDE]**

---

## 6. Feasibility — how autonomous *could* it be under current regulation?

This is the feasibility core. Conclusions here are **drafts to be confirmed by the regulatory analysis** (`../regulatory/`) and the regulatory agent.

Working hypotheses to test:
- **COLREGs** require proper lookout and collision-avoidance judgement; today interpreted around a human master/lookout. A fully autonomous (Degree 4) collision-avoidance decision in busy harbour traffic is likely **not** clearly permissible yet → supports a **remotely supervised Degree-3** default. **[VERIFY]**
- **IMO MASS Code** — now **adopted** as a goal-based framework; determine what it requires for a Degree-3 surveillance USV and whether "legal today" relies on the adopted Code, interim guidance, and/or national/port permissions. **[VERIFY]**
- **EU MASS trial guidelines** — the EU has operational guidelines for MASS trials; assess whether a supervised harbour operation fits a trial/operational pathway. **[VERIFY]**
- **Swedish national / port rules (Transportstyrelsen, Sjöfartsverket, port by-laws)** may allow a supervised operation within defined harbour limits with specific approvals; confirm the exact authority map. **[VERIFY]**
- **Manning / certification, radio/comms licensing, insurance/liability** must all be satisfiable with today's framework. **[VERIFY]**

**Feasibility output:** a mapping of "desired autonomy degree" vs. "regulatory ceiling today," producing the maximum defensible autonomy for a legal-today operation. This mapping is a key deliverable and links directly to `../requirements/` (derived requirements) and `../regulatory/` (compliance matrix).

---

## 7. Operating environment

| Condition | Expectation | USV must… |
|-----------|-------------|-----------|
| Sea state / wind | Harbour/coastal, seasonal | **[DECIDE]** operate / tolerate-degraded / survive thresholds |
| Visibility | Day/night, fog, variable | Operate (sensor-dependent); degrade gracefully |
| Ice | Seasonal possibility | **[DECIDE]** operate, tolerate, or scope out |
| Traffic density | Dense: commercial shipping, ferries, pilot/tug, small craft | Operate; maintain COLREGs-consistent behaviour |
| EM environment | Dense AIS/radar; spoofing/jamming risk | Operate; detect degraded sensing |

The operating envelope (speed range, sea-state limits, geographic boundary) is to be set with naval architecture and systems engineering. **[DECIDE]** operating envelope.

---

## 8. Operational scenarios

Scenarios are labelled for requirement traceability. Nominal = `SCN-N-xx`; off-nominal = `SCN-OFF-xx`. These are drafts to be expanded with the team.

### Nominal
- **[SCN-N-01] Routine patrol leg** — USV follows a pre-planned patrol route under remote supervision; streams EO/IR + radar + AIS fusion to the shore operator and VTS; operator monitors multiple legs.
- **[SCN-N-02] Station-keeping watch** — USV holds position near a terminal/critical asset, running intrusion/anomaly detection; alerts prioritised to the operator.
- **[SCN-N-03] Environmental sweep** — USV surveys for spills/discharge/debris; environmental sensor flags an indicator; logged and reported.

### Off-nominal
- **[SCN-OFF-01] Lost comms link** — both primary and fallback links drop; USV executes the agreed lost-link policy (safe hold / move-to-safe-zone / return). **[DECIDE]** lost-link policy.
- **[SCN-OFF-02] Collision risk in dense traffic** — autonomy detects a close-quarters situation it cannot resolve within authority; escalates to the on-the-loop operator who takes control. Exercises the human-authority boundary (§4, §5).
- **[SCN-OFF-03] Detected intrusion / suspected criminal activity** — USV detects an actionable event; operator escalates to the responsible authority; USV continues to observe/report, does not interdict (§2, §5).
- **[SCN-OFF-04] Sensor degradation / spoofing** — perception degraded by weather/occlusion or AIS/GNSS spoofing; USV flags reduced confidence; operator decides on fallback.
- **[SCN-OFF-05] Man-overboard assist** — USV supports a MOB situation by providing EO/IR spotting and relaying position to rescue assets.

---

## 9. Risks & issues

| # | Risk / issue | Note |
|---|--------------|------|
| R1 | "Legal today" may not support Degree-3 uncrewed operation as hoped | **Concept-gating** — resolve first (§6). |
| R2 | Regulatory acceptance of AI in safety functions is immature | Affects autonomy scope (§4.1). |
| R3 | Cyber-security of command/control and sensor links | First-class concern (§4.2). |
| R4 | Comms resilience / lost-link behaviour in dense traffic | Drives §4.2 and SCN-OFF-01. |
| R5 | Liability/insurance for uncrewed operation | Part of the regulatory ceiling (§6). |
| R6 | Over-scoping the concept study (sensors, autonomy) | Keep baselines minimal; growth options noted. |

---

## 10. Environmental & organizational impacts

- **Environmental:** net-positive intent (spill/discharge detection); consider the USV's own footprint (power source, antifouling, noise). **[DECIDE]** power/propulsion concept and its environmental profile.
- **Organizational:** requires trained shore operators and a support function; changes port-ops workflows; defines a VTS interface and an authority-handoff path.

---

## 11. External interfaces

- **Shore control centre** — command/control + sensor data (comms link).
- **VTS / port operations** — situational-awareness feed.
- **Responsible authorities** — event handoff/escalation path.
- **AIS / navigation infrastructure** — cooperative traffic data in.

Interface definitions to be developed with systems engineering (SysML). **[DECIDE]** interface baseline.

---

## 12. Referenced documents & frameworks
- IMO MASS Code (adopted) and IMO four degrees of autonomy (MSC 100).
- EU Operational Guidelines on MASS trials (European Commission / EMSA).
- EMSA RBAT CONOPS concepts (structure reference).
- COLREGs, SOLAS, and applicable EU/Swedish national + port rules — see `../regulatory/`.
- Project definition: `../../project/`. Agent/collaboration conventions: `../working-with-agents.md`.

*External regulatory statements in this document are drafts for the regulatory track to verify; content summarised/rephrased from public sources for compliance.*

---

## 13. Open items

Open items are **tagged inline** in the sections above — this section is not a second copy to keep in sync. To see what's open, search this doc (and the repo) for `[VERIFY` and `[DECIDE`.

- **[VERIFY]** items (regulatory / legal) close via the regulatory agent → reviewed into `../regulatory/`, each with a citation and a verdict (permissible / not / conditional).
- **[DECIDE]** items (team choices) close via a short entry in `../decisions/`.

When an item closes, replace its inline tag with the decided text plus a link to where the answer lives. See `../working-with-agents.md` for the full convention.

---

## 14. Next steps

Each step names an owning **role** (not a person — public-repo rule). Steps run in parallel except where a dependency is noted.

1. **remote-ops lead — FIRST (gating):** confirm the CONOPS template decision (`../decisions/2026-10-26-conops-template.md`). This sets the structure the rest are recorded against, so close it before the others to avoid rework.
2. **remote-ops lead** — then resolve the unblocked **[DECIDE]** items that don't depend on the regulatory ceiling (lost-link policy, geographic boundary, operating envelope, surveillance/enforcement handoff, support concept, cyber baseline); record each in `../decisions/`. (Sensor baseline decided 2026-10-26.)
3. **regulatory lead** — in parallel, feed **[VERIFY]** items to the regulatory agent / `../regulatory/` to establish the regulatory ceiling (this unblocks the autonomy-degree and operator-ratio decisions in §4–§6).
4. **systems lead** — once CONOPS and the regulatory ceiling stabilise, derive initial requirements into `../requirements/`, tracing to the `SCN-*` scenarios.
5. **[DECIDE: one-slide summary owner]** — decide which role produces the one-slide concept summary for `../../presentations/`; record the decision in `../decisions/`.

---

## 15. Glossary
- **MASS** — Maritime Autonomous Surface Ship (IMO term).
- **USV** — Uncrewed Surface Vessel (the platform type in this concept).
- **COLREGs** — International Regulations for Preventing Collisions at Sea.
- **VTS** — Vessel Traffic Service.
- **EMSA** — European Maritime Safety Agency.
- **RBAT** — Risk-Based Assessment Tool (EMSA MASS method).
- **On-the-loop** — human monitors an autonomous system and can intervene, but is not in continuous control.
