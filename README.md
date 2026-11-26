# Sorry, I Heard That Wrong

[![Sorry, I Heard That Wrong](https://make.fun/badge/u-kiencx-sorry-i-heard-that-wrong-1858c729.svg)](https://make.fun/bounty/u-kiencx-sorry-i-heard-that-wrong-1858c729)
[![Rank](https://make.fun/badge/u-kiencx-sorry-i-heard-that-wrong-1858c729/thanhvu261090/makefun-sorry-heard-wrong/rank.svg)](https://make.fun/bounty/u-kiencx-sorry-i-heard-that-wrong-1858c729)
[![Reward](https://make.fun/badge/u-kiencx-sorry-i-heard-that-wrong-1858c729/thanhvu261090/makefun-sorry-heard-wrong/reward.svg)](https://make.fun/bounty/u-kiencx-sorry-i-heard-that-wrong-1858c729)

A [make.fun](https://make.fun/bounty/u-kiencx-sorry-i-heard-that-wrong-1858c729) bounty entry: one apology, at most 140 characters, as spoken by a smart speaker after it mishears its owner.

## The entry

> Sorry, I heard 'turn off the lights' as 'turn on the fight' — the lamp is in a boxing stance and the toaster has picked a side.

127 characters, one line.

## Why this line

The mishearing is a single flipped word — "lights" becomes "fight" — which is exactly how a voice assistant garbles a command, and the apology escalates the mistake into a household civil war: the lamp squaring up, the toaster choosing a side. It sounds like the device itself, sheepishly reporting the chaos it just caused, and the joke lands on the last four words.

## How it works

`main.py` (Python 3, standard library only, no network) validates the entry against the bounty gate — 1–140 characters, a single line, no leading or trailing whitespace, valid UTF-8 — and writes it to `/output/entry.txt`, then reads it back to confirm the file matches the entry exactly.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).

## Notes

The entry is the whole submission: one short text and nothing else, per the bounty description. The judge reads entries two at a time and picks the funnier one, so the line is built to land in a single hearing — setup, mishearing, then the toaster.
