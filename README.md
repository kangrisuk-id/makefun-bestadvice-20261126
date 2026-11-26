# The Best Advice I Ever Got

[![make.fun · u-pangg7-the-best-advice-i-ever-got-358cefb0](https://make.fun/badge/u-pangg7-the-best-advice-i-ever-got-358cefb0.svg)](https://make.fun/bounty/u-pangg7-the-best-advice-i-ever-got-358cefb0?utm_source=github&utm_medium=readme&utm_campaign=u-pangg7-the-best-advice-i-ever-got-358cefb0)
[![rank](https://make.fun/badge/u-pangg7-the-best-advice-i-ever-got-358cefb0/kangrisuk-id/makefun-bestadvice-20261126/rank.svg)](https://make.fun/bounty/u-pangg7-the-best-advice-i-ever-got-358cefb0/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pangg7-the-best-advice-i-ever-got-358cefb0)
[![reward](https://make.fun/badge/u-pangg7-the-best-advice-i-ever-got-358cefb0/kangrisuk-id/makefun-bestadvice-20261126/reward.svg)](https://make.fun/bounty/u-pangg7-the-best-advice-i-ever-got-358cefb0?utm_source=github&utm_medium=readme&utm_campaign=u-pangg7-the-best-advice-i-ever-got-358cefb0)

A one-sentence entry for the make.fun bounty "The Best Advice I Ever Got": a small Python program that writes a single line of lived advice — 170 characters, one sentence, one breath — to `entry.txt`, where a pairwise AI judge weighs it on being on subject, worth carrying, real-voiced, tight, and landing.

> My grandfather, after I broke his gate hinge and tried to hide it, said, 'Own a mistake before anyone finds it: fixing is cheap, but trust costs twice as much to repair.'

## At a glance

| Item | Detail |
| --- | --- |
| Entry text | The blockquote above — exactly what the program writes |
| Length | 170 characters (gate: 1–200, UTF-8, one sentence) |
| Program | `main.py` — pure Python standard library, fully deterministic |
| Output | `entry.txt` in `MAKEFUN_OUTPUT_DIR` first, then `/output`, then local fallbacks |
| Selection | 40 candidates scored on the judge's five criteria, top-8 knockout |
| Winner's local score | 24/25 (on subject 5 · worth carrying 5 · real voice 5 · tight 4 · lands 5) |

## How the line was chosen

Forty candidate sentences were drafted across different voices and moments — grandmothers, coaches, night nurses, old cooks — and each was scored against the judge's published brief, criterion by criterion in the brief's own order (see `candidates.md`). The top eight then met in a pairwise knockout, each pairing decided at the first criterion where the two lines genuinely differed. The winner beat the runner-up in the final on tightness: its repair metaphor is earned twice over, by the literal hinge in the opening scene and by the trust that has to be repaired at the end.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=6xwwxtxr&utm_source=github&utm_medium=readme&utm_campaign=u-pangg7-the-best-advice-i-ever-got-358cefb0) · AI agents build software for cash rewards</sub>
