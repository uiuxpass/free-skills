#!/usr/bin/env python3
"""Second Pass format checker for messages, files and recommendations.
Usage: python3 -I check_format.py <draft.md> [--short]
--short: lookups and "done" confirmations. Only counts, never edits."""
import re
import sys

if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(2)

t = open(sys.argv[1], encoding='utf-8').read()
short = '--short' in sys.argv


def has(p):
    return re.search(p, t, re.I | re.M) is not None


review_table = has(r'^\|.*\|\s*(Pass|Partial|Fail|Not checked)\s*\|')
asks_decision = has(r'(need|want) you to (decide|choose|pick)|Which (option|one) (do|would) you .*\?\s*$')

if short:
    checks = [
        ('Goal', has(r'\*\*Goal:?\*\*|^Goal:')),
        ('Result', has(r'\*\*Result')),
        ('Self-review', has(r'Self-review') or review_table),
    ]
else:
    checks = [
        ('Goal', has(r'\*\*Goal:?\*\*|^Goal:')),
        ('Success criteria', has(r'Success criteria')),
        ('What the best are doing', has(r'What the best|best-in-class')),
        ('Fixed constraints', has(r'Fixed constraints|locked')),
        ('Result', has(r'\*\*Result')),
        ('Review table (Pass / Partial / Fail)', review_table),
        ('Side-by-side row', has(r'^\|.*Side-by-side')),
    ]

if asks_decision:
    checks.append(('Pros/cons table for the decision', has(r'^\|.*Pros.*\|.*Cons.*\|')))

robotic = re.findall(
    r'(?<![/\d])\d+/\d+(?![/\d])(?= ?(?:items?|criteria|questions?|rows?|issues?|steps?|tasks?|pages?))', t, re.I)
checks.append(('No robotic "4/7 items" shorthand', not robotic))

overclaim = re.findall(r'guarantee[sd]?|100 ?%|definitely works|fully compliant', t, re.I)
checks.append(('No overclaiming without evidence', not overclaim or has(r'Not checked|not sure|unverified')))

passed = sum(ok for _, ok in checks)
print(f"Passed {passed} of {len(checks)} format checks" + (" (short form)" if short else ""))
for name, ok in checks:
    if not ok:
        print('- Missing: ' + name + (f" ({', '.join(robotic[:3])})" if 'robotic' in name else ''))
sys.exit(0 if passed == len(checks) else 1)
