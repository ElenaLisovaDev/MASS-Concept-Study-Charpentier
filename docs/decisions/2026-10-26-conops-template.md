# Decision brief — Which CONOPS template/standard to follow

**Status:** PROPOSED (awaiting team confirmation) · **Date:** 2026-10-26 · **Owner:** remote-ops lead
**Closes:** `[DECIDE]` CONOPS template/standard (CONOPS §0 — document structure)
**Depends on:** none — decidable now; it shapes how the CONOPS is structured going forward.

> This is a brief, not a settled decision. It frames options and a recommendation so the team can confirm asynchronously. To close, follow `../working-with-agents.md` §5a (replace the inline `[DECIDE]` tag + fill the Decision block + log it).

## Question
What document structure should the CONOPS follow? A generic systems-engineering CONOPS outline, or a maritime/MASS-specific one? This matters because the structure drives what we're obliged to cover and how the CONOPS traces into regulatory analysis and requirements.

## Options

### Option 1 — Generic SE CONOPS standard (NASA outline / ANSI-AIAA G-043B / ISO-IEC-IEEE 29148)
Structure around the classic SE sections: background, assumptions, scope, actors, modes, environment, scenarios (nominal/off-nominal), impacts, risks.
- **Pro:** comprehensive, well-known, strong on scenarios and traceability; ISO/IEC/IEEE 29148 is the formal requirements-engineering anchor.
- **Con:** domain-neutral (NASA is aerospace); doesn't natively reflect MASS concepts like autonomy degrees or shore operational roles; the formal standards are paywalled.

### Option 2 — EMSA RBAT CONOPS structure (recommended)
Follow the maritime, EU-authored MASS CONOPS pattern used in EMSA's Risk-Based Assessment Tool work, aligned to IMO's framework:
1. Overall description
2. Mission description
3. Main characteristics
4. Description of autonomous systems
5. Operational roles
...with the §4 autonomy concept mapped onto **IMO's four degrees of autonomy**, and generic-but-valuable additions retained (operating environment, nominal/off-nominal scenarios, risks).
- **Pro:** maritime and MASS-specific; authored by the EU maritime safety regulator (EMSA); aligns directly with IMO MASS Code and EU MASS trial guidelines — exactly the frameworks our `[VERIFY]` items reference; public.
- **Con:** lighter on explicit requirements-traceability scaffolding than 29148, so we add scenario labelling ourselves.

### Option 3 — Hybrid (EMSA backbone + 29148 traceability habits)
Use the EMSA 5-part maritime structure as the spine, but borrow the generic standard's rigor where EMSA is thin: labelled operational scenarios, assumptions & constraints, operating envelope, and risks — so requirements can trace to scenario IDs.
- **Pro:** maritime-correct *and* traceable; best fit for a project whose core mandate is regulation→requirement traceability.
- **Con:** slightly more to maintain than pure EMSA.

## Recommendation
**Option 3 (hybrid): EMSA RBAT structure as the backbone, with IMO four-degree autonomy mapping, plus 29148-style scenario labelling, assumptions, operating envelope, and risks.** This keeps the CONOPS maritime-authentic and regulator-aligned (EMSA/IMO/EU) while preserving the traceability the project depends on.

## Sources
- EMSA RBAT CONOPS concepts (short-sea cargo / passenger ferries / Ro-Pax) — structure: overall description, mission, main characteristics, autonomous systems, operational roles. https://www.emsa.europa.eu/mass.html
- IMO four degrees of MASS autonomy (MSC 100). https://www.imo.org/en/mediacentre/meetingsummaries/pages/msc-100th-session.aspx
- IMO MASS Code (adopted). https://www.imo.org/en/mediacentre/pressbriefings/pages/imo-adopts-mass-code.aspx
- EU Operational Guidelines on MASS trials. https://transport.ec.europa.eu/transport-modes/maritime/maritime-autonomous-ships-and-shipping_en
- Generic SE reference (structure only): NASA ConOps annotated outline; ISO/IEC/IEEE 29148.

*Content rephrased from the sources for compliance with licensing restrictions.*

## Decision
_To be completed by the team:_
- **Chosen option:**
- **Rationale / any adjustments:**
- **Confirmed by (role):**
- **Date:**
