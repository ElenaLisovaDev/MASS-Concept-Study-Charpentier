# CONOPS Proposal — Göteborg Harbour Surveillance USV

**Status:** Draft v0.1 — for team review. Regulatory statements are drafts to be verified (see §8).
**Scope:** Concept of Operations for a 24 m uncrewed surface vessel (USV) performing civil surveillance of Göteborg harbour.

> This document captures the CONOPS direction agreed in the first team discussion. It is a proposal, not a baseline. Items needing confirmation are marked **[VERIFY]** (regulatory/legal) or **[DECIDE]** (team decision).

---

## 1. Mission statement

Provide persistent, uncrewed surface surveillance of Göteborg harbour and its approaches to support port security, safety, and environmental monitoring — using a system that is **legal to operate today** under current applicable regulations, civil-use only.

### Key constraints (from team discussion)
- **Platform:** surface vessel, **not** a submarine. ~**24 m** length.
- **Legality:** must be operable **today** under current/appointed regulations — no dependence on future rulemaking. **[VERIFY]**
- **Use:** **civil only — no military** use or payloads.
- **Owner / operator:** Port of Göteborg (Göteborgs Hamn) as concept owner/operator. **[DECIDE]** (confirm operator model)

---

## 2. Operational context

- **Operating area:** Göteborg harbour, quays, and approach channels. Mixed traffic: commercial shipping, ferries, pilot/tug boats, small craft. High-value infrastructure (terminals, energy, bridges).
- **Environment:** coastal/harbour conditions, seasonal weather, ice possibility, day/night, variable visibility, dense AIS and radar environment.
- **Stakeholders:** port authority, Swedish Maritime Administration (Sjöfartsverket), Swedish Transport Agency (Transportstyrelsen), Coast Guard (Kustbevakningen), police, port tenants, vessel traffic service (VTS). **[VERIFY]** exact authority map.

---

## 3. Surveillance missions

The USV supports general port security and safety:

1. **Criminal activity** — detect/monitor unauthorised access, smuggling indicators, suspicious small-craft behaviour.
2. **Sabotage / security of critical infrastructure** — patrol near terminals, subsea assets, bridges; detect intrusion.
3. **Environmental monitoring** — spills, illegal discharge, water-quality indicators, debris.
4. **General safety** — man-overboard spotting support, hazard detection, situational awareness feed to VTS/port ops.

Primary sensing concept (to be refined by naval architecture / systems engineering): EO/IR cameras, radar, AIS receiver, acoustic/hydrophone (environmental), with data relayed to a shore control centre. **[DECIDE]** sensor baseline.

---

## 4. Autonomy concept — autonomous vs. remotely supervised

A central question for this project. We frame autonomy on a spectrum and propose a **default operating mode** plus fallbacks.

| Mode | Description | Proposed use |
|------|-------------|--------------|
| **Remotely operated** | Continuous human control from shore | Fallback / complex situations / manoeuvring in dense traffic |
| **Remotely supervised** (proposed default) | USV executes the mission autonomously; a shore operator monitors and can intervene; human stays "on the loop" | Routine patrol legs, station-keeping |
| **Fully autonomous** | No real-time human supervision | **Likely not permissible today** for collision-avoidance decisions in this traffic environment **[VERIFY]** |

**Proposed concept:** operate primarily **remotely supervised**, with a human operator on-the-loop able to take direct control, and an operator-to-USV ratio to be studied. Autonomy handles navigation, route-following, station-keeping, and sensor tasking; the human retains authority over collision-avoidance exceptions, interaction with other vessels, and any enforcement-adjacent action.

**[DECIDE]** target operator-to-vessel ratio and what decisions must always require a human.

---

## 5. CONOPS feasibility — how autonomous *could* it be under current regulation?

This is the feasibility core requested in the discussion. Conclusions here are **drafts to be confirmed by the regulatory analysis** (`../regulatory/`) and the regulatory agent.

Working hypotheses to test:
- **COLREGs** require proper lookout and collision-avoidance judgement; today these are interpreted around a human master/lookout. A fully unmanned, fully autonomous collision-avoidance decision in busy harbour traffic is likely **not** clearly permissible yet → supports a **remotely supervised** default. **[VERIFY]**
- **IMO MASS Code** is developing (non-mandatory → mandatory phase planned). Operating "legal today" likely means relying on **national/port permissions and existing conventions**, not the future mandatory MASS Code. **[VERIFY]**
- **Swedish national / port rules (Transportstyrelsen, port by-laws)** may allow a supervised trial/operation within defined harbour limits with specific approvals. **[VERIFY]**
- **Manning / certification, radio/comms licensing, and liability** must all be satisfiable with today's framework. **[VERIFY]**

**Feasibility output:** a mapping of "desired autonomy level" vs. "regulatory ceiling today," producing the maximum defensible autonomy for a legal-today operation. This mapping is a key deliverable and links directly to `../requirements/` (derived requirements) and `../regulatory/` (compliance matrix).

---

## 6. Use of AI — and its limitations (concept / design / operation)

How AI can support the USV, and where it is limited. This addresses the "any AI limitations in concept, design, or operation" question.

### Concept phase
- **Uses:** generating CONOPS options, scenario exploration, regulatory research assistance, requirement drafting (the agentic workflow itself).
- **Limitations:** AI output can be plausible but wrong; regulatory interpretation must be human/expert-validated; no authoritative legal judgement.

### Design phase
- **Uses:** parametric trade studies, design-space exploration, architecture/consistency checks, documentation drafting.
- **Limitations:** engineering validity must be verified; AI lacks certified physics/classification authority; results need traceability and review.

### Operation phase
- **Uses:** sensor data fusion, anomaly/threat detection, situational-awareness aids, route optimisation, alert prioritisation for the shore operator.
- **Limitations:** safety-critical decisions (collision avoidance, enforcement) need human authority; perception can fail in edge conditions (weather, occlusion, spoofing); explainability and accountability requirements; cyber-security of autonomy and comms links; regulatory acceptance of AI in safety functions is immature. **[VERIFY]**

**Guiding principle:** AI augments the engineer and operator; it does not hold final authority over safety-critical or legal decisions.

---

## 7. Communications & shore control (concept)

- Shore control centre with the on-the-loop operator(s).
- Resilient comms link (primary + fallback) with defined **lost-link behaviour** (e.g. safe station-keeping / return / hold). **[DECIDE]** lost-link policy.
- Cyber-security for command/control and sensor data.

---

## 8. Open items

### To verify (regulatory / legal — route to `../regulatory/` + regulatory agent)
- Exact "legal today" pathway for a supervised 24 m surveillance USV in Göteborg waters.
- COLREGs lookout/collision-avoidance interpretation for unmanned operation.
- Applicable national (Transportstyrelsen / Sjöfartsverket) and port-authority requirements and approvals.
- Manning, certification, radio licensing, insurance/liability.
- Permissibility of AI in safety-related functions.

### To decide (team)
- Operator model and operator-to-vessel ratio.
- Sensor baseline.
- Lost-link policy.
- What decisions must always require a human.

---

## 9. Next steps

1. Team review of this proposal; resolve **[DECIDE]** items.
2. Feed **[VERIFY]** items to the regulatory agent / `../regulatory/` to establish the regulatory ceiling.
3. Derive initial requirements into `../requirements/` from the agreed CONOPS.
4. Owner TBD — produce the one-slide summary suggestion for the harbour surveillance concept — store in `../../presentations/`.
