---
name: heuristic-ux-copy-review
description: Reviews one screen or a multi-screen flow against Nielsen's 10 heuristics and UX copy (labels, buttons, errors, empty states) in two tables, screen level and flow level, with measured color contrast and every principle linked to its source. Use this whenever the user shares screenshots, mockups or a flow and asks for a UX review, design critique, feedback, heuristic evaluation, usability issues or a copy check, even if they only say 'what do you think of this screen'.
---

# Heuristic and UX copy review (one pass, two tables)

**Goal:** review a screen or flow for both interaction logic (heuristics) and words (copy) at once, grouped by where the issue is visible: on one screen, or only across screens. Copy is never split into its own table, because users experience both as one thing. Quality bar: measurable evidence, nothing invented, nothing missed, no alarmist language.

## Gather input

1. Get each screen in flow order. If both compressed and original images exist, always read the original to see small text.
2. With Figma connected, read exact text from text layers instead of reading pixels.
3. Ask for the flow's goal (sign up, checkout, search…) if not given.
4. **Verify names before flagging a naming issue:** compare any product name the user typed with the actual text on screen. Never use the user's typing as evidence.
5. **Check titles and descriptions against attached content:** if a screen has a user-entered title or description and a file preview, check they match. A mismatch is a real finding (the system lacks validation); note if it might be demo data.

## How to evaluate

**Grouping rule:** an issue is **screen level** if one screen shows it; **flow level** if it only appears when comparing screens.

**Repeated issues:** re-scan ALL remaining screens and list every affected screen in the same finding. Never stop at the first one.

### Screen level (per screen)

Heuristics, scored 0–5 or "N/A":
1. Visibility of system status
2. Match between system and the real world
7. Flexibility and efficiency of use
8. Aesthetic and minimalist design
9. Help users recognize, diagnose and recover from errors

UX copy on that screen:
- Clear, concise, useful (NN/g's 3 Cs).
- Buttons describe the action that will happen.
- Error messages don't blame the user and explain the fix. No error-state screenshot → record it as a data gap.
- Empty states and placeholders give specific guidance.
- User-entered content matches the attached content.

### Flow level (once per flow)

Heuristics, scored 0–5 or "N/A":
3. User control and freedom
4. Consistency and standards
5. Error prevention
6. Recognition rather than recall
10. Help and documentation
\+ Flow progress

Copy across the flow: consistent tone; the same action always has the same name.

Every flow-level issue names **which screens** it occurs between, listing all of them.

## Severity and grounding

Use only three labels: **High impact** (blocks the goal or causes a wrong action) · **Medium impact** (annoying or slow, but completable) · **Low impact** (polish). Never use "critical" or "severe", even in prose.

Ground heuristic issues in a UX law where relevant ([Laws of UX](https://lawsofux.com/)): Fitts, Hick, Jakob, Miller, Peak-End, Aesthetic-Usability, Doherty, Zeigarnik, Postel.

## Link every principle to its source (required)

Every principle named in the report is a link that opens in a new tab. Never guess URLs; use this table:

| # | Principle | URL |
|---|---|---|
| 1 | Visibility of system status | https://www.nngroup.com/articles/visibility-system-status/ |
| 2 | Match system and real world | https://www.nngroup.com/articles/match-system-real-world/ |
| 3 | User control and freedom | https://www.nngroup.com/articles/user-control-and-freedom/ |
| 4 | Consistency and standards | https://www.nngroup.com/articles/consistency-and-standards/ |
| 5 | Error prevention | https://www.nngroup.com/articles/error-prevention/ |
| 6 | Recognition rather than recall | https://www.nngroup.com/articles/recognition-and-recall/ |
| 7 | Flexibility and efficiency | https://www.nngroup.com/articles/flexibility-efficiency-heuristic/ |
| 8 | Aesthetic and minimalist design | https://www.nngroup.com/articles/aesthetic-minimalist-design/ |
| 9 | Recognize, diagnose, recover from errors | https://www.nngroup.com/articles/error-message-guidelines/ |
| 10 | Help and documentation | https://www.nngroup.com/articles/help-and-documentation/ |
| — | The 10 heuristics | https://www.nngroup.com/articles/ten-usability-heuristics/ |
| — | Microcopy (3 Cs) | https://www.nngroup.com/articles/3-cs-microcopy/ |
| — | Tone of voice | https://www.nngroup.com/articles/tone-voice-users/ |
| — | WCAG contrast | https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html |

## Measure real contrast (when originals exist)

1. With Python PIL, crop the text/background pair from the ORIGINAL image.
2. Find dominant colors with `collections.Counter`, avoiding anti-aliased edge pixels.
3. Compute WCAG contrast: `(L1+0.05)/(L2+0.05)`, luminance via sRGB gamma correction.
4. AA thresholds: body text ≥ 4.5:1; large text and UI components ≥ 3:1.
5. Report the exact ratio with the sampled hex values, never an estimate.

## Report format

1. **Overview:** number of screens, flow goal, context; plus the limitation that a single evaluator typically finds about 35% of issues and 3–5 evaluators reach about 75% ([source](https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/)).
2. **Screen strip**, click to enlarge.
3. **Screen-level table:** Screen · Type (Heuristic/Copy) · Principle (link) · Score · Severity · Issue · UX law · Fix.
4. **Flow-level table:** Type · Principle (link) · Between screens · Score · Severity · Issue · UX law · Fix.
5. **Contrast** (when originals exist): real measurements.
6. **Coverage matrix:** always all 10 rows in Nielsen order, including heuristics with no findings.
7. **Priority list:** High → Low. Every High-impact item must appear. Each: issue → why it affects the goal → fix.
8. **What works well:** at least one specific item.
9. **Method limitations:** static screenshots, number of evaluators, heuristics lacking evidence, what would raise confidence.

Don't score what you can't observe: write "Not enough data".

## Check before sending

- [ ] Severity labels are only High / Medium / Low impact.
- [ ] Coverage matrix has all 10 rows, each name linked.
- [ ] All 10 heuristics and 6 copy areas covered: clarity · consistent terms · tone · buttons · errors and empty states · user content matches attachments.
- [ ] Repeated issues list every affected screen.
- [ ] Severity counts match the overview; every High-impact item is in the priority list.
- [ ] Contrast numbers are measured.
- [ ] Method limitations section is present.

## Deliver it the UI/UX Pass way

Apply this to every result from this skill, even when `uiuxpass-workflow` and `self-review` are not loaded. Keep it proportionate: one line per part for a quick answer.

1. **Result first.** Open with one or two sentences: what the user gets, in what form, and how it was measured or checked.
2. **Five parts, briefly:** Goal · Success criteria · What the best do (name one or two best-in-class examples and where this result falls short of them) · Fixed constraints (what you kept from the user's inputs and brand) · Result.
3. **Decisions come with options.** Anything the user must decide gets a short pros/cons table with your recommendation marked.
4. **Self-check before sending.** End with a one-line or small-table check of: On target · Instantly clear · Trustworthy (every number sourced, nothing invented, uncertainty stated) · Actionable · Lean. If this skill has a checker script, its score goes in the self-check. Say plainly what you could not check.
