---
name: self-review
description: One review standard for every deliverable (interfaces, reports, decks, docs, reviews): five universal questions, a side-by-side check against best-in-class work, type-specific checks, three review layers (automated, self, blind) and a script that checks the delivery format. Use this before handing any design, product or writing result to the user, and whenever the user asks 'is this good enough' or to check work before sending.
---

# Self-review

**Target outcome:** every deliverable is reviewed with the same standard. One glance at the review table tells the user how good the output is, what is missing and who checked it.

Apply by default: whenever you hand over a result, attach the review without being asked.

## 1. Five universal questions

Play the real recipient and look once. Name the role (executive, product manager, end user of the interface…). Score as the toughest of those roles.

| # | Question | Passes when |
|---|---|---|
| 1 | **On target:** does it answer what the recipient actually needs? | Matches the agreed goal and success criteria; nothing extra, nothing out of scope. |
| 2 | **Instantly clear:** is it understood in one pass? | The first sentence is the result or the decision needed; plain language; every number states its meaning and why it matters. |
| 3 | **Trustworthy:** would you stake a decision on these numbers? | Every number has a source or was computed from the original file; gaps say "Not measured"; illustrative numbers are labelled. |
| 4 | **Actionable:** can the recipient act right away? | Each point has the full chain: where the problem is → why → what to do → expected gain → evidence. Never ends by handing work back ("needs further monitoring"). No two places contradict each other. |
| 5 | **Lean and consistent:** anything extra, anything off-standard? | No filler; the same kind of information always uses the same format; matches every rule the user has locked. |

**Levels:** Pass / Partial / Fail / Not checked. "Not checked" never counts as a pass. Every row needs evidence: a measurement, screenshot, location or exact quote.

**Side-by-side with the best:** pick 1–2 best-in-class examples of the same kind (docs: Stripe, Linear; decks: McKinsey, Apple; interfaces: Notion, Linear; reports: The Economist, Our World in Data). Compare point by point: sharpness of content, layout and detail, typography, data, how it feels to use. Where it clearly loses, fix it before sending or say so. Never claim "world-class" without doing this comparison.

## 2. Type-specific checks

| Type | Also check |
|---|---|
| Interface design | 3 criteria: right for the workflow · fits the whole product · experience on par with leading products. The `interface-polish` checker shows no critical failures, and every major one is fixed or explained. |
| Web pages, data reports | The `interface-polish` checker; every number matches its source. |
| Decks, brochures | No text overflow, readable type size, one clear idea per screen. |
| Docs, articles | `product-writing`; questions 2 and 4 matter most. |
| Reviews, audits | Section 6 of `second-pass-workflow`. |
| Applications with an official rubric | Use that rubric exactly, with a projected score table: "As is" vs "After fixing high-priority items". |

## 3. Three review layers

1. **Automated** (every build): run the type's checker; for messages, files and recommendations, run the format checker in section 6. Checkers only count, never fix. Numbers in the review come from the checker, not typed by hand.
2. **Self-review** (every deliverable): score the five questions as the toughest recipient, challenge your own work, never defend it.
3. **Blind review** (large deliverables only, after the user has confirmed the content and the checker passes): spawn a fresh sub-agent that has not seen the process, with option names hidden. Brief: "You are [recipient role], used to [best-in-class example]. Look at this once and say plainly where it matches or falls short of the example. For each of the five questions [paste section 1] and the type checks [paste section 2], mark Pass / Partial / Fail with Location · Evidence · Fix. No generic praise." If sub-agents aren't available, open a new conversation and paste this brief.

## 4. How to present the review

- Put it in part 5, "Result with a self-review table".
- Rows: the five questions (question 1 split per success criterion) · a **Side-by-side with best-in-class** row (which example, where it matches or loses) · type-specific checks. Columns: Question · Level · Evidence · What's missing.
- Add one summary sentence (e.g. "4 Pass, 1 Partial: Trustworthy, two numbers lack a source"), which checkers ran, whether a blind review ran, and what's left.
- Avoid robotic shorthand like "4/7 items".
- Large deliverables also get: what works (max 3) · improvements (priority, current state, impact, recommendation) · the 1–3 hardest questions the recipient will ask · a one-line takeaway.

## 5. Principles

- The user's locked rules always beat this checklist. Breaking one is a Fail on question 5.
- Separate verified numbers from assumptions.
- Small tasks (a lookup, a one-word fix) only need a one-line review.
- A mistake the user had to point out twice becomes an automated check.

## 6. Format checker

Write the draft to a file and run it before sending:

`python3 -I scripts/check_format.py draft.md` (lookups and confirmations: add `--short`)

It checks: all five parts (short form: Goal · Result · Self-review); a review table; a side-by-side row; a pros/cons table when a decision is requested; no "4/7 items" shorthand; no "guaranteed" or "100%" unless something is marked "not checked".

To add a check for a mistake of your own: open `scripts/check_format.py` and add one line to the `checks` list.
