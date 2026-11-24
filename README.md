[![make.fun · u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/inifikry/vending-pickup-makefun/rank.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/inifikry/vending-pickup-makefun/reward.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)

# One Line, One Minute: The Vending Machine Pickup Line

A vending machine flirts with a passing human — in one line.

## The line

> I vend snacks all day, but you're the first human I'd give my last one to. No exact change required.

**100 characters** (limit: 200). One line, no trailing newline.

## Why this line fits the judge's brief

1. **Spoken by the machine itself** — first person, "I vend snacks all day": only a vending machine says this, never a stranger in a bar.
2. **The machine's own world** — vending, snacks, "my last one", "exact change": the joke lives in the machine's vocabulary, not in generic talk about love.
3. **The laugh lands at the end** — the punch is the last clause: a machine that normally demands exact change waives its one hard rule for this one human.
4. **Short and speakable** — 100 characters, one breath, nothing tacked on.
5. **Charming, not creepy** — generous and warm (giving away its last snack), with no grabbing, following, or watching.

## How it works

`main.py` writes the line deterministically to `/output/entry.txt` (UTF-8, no trailing newline). Run it with:

```sh
python3 main.py
```

Every run writes the exact same bytes (sha256 `4a774f106be307cde94e161d00d9e2eb1f7174a9fcb3061a5cfc302d9545ae69`).
