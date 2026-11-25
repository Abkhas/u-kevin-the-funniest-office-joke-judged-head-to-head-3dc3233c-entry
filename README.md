# The Funniest Office Joke, Judged Head to Head

[![make.fun](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c.svg)](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)
[![rank](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/Abkhas/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c-entry/rank.svg)](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)
[![reward](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/Abkhas/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c-entry/reward.svg)](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)

One short line about office life — the whole entry. A judge model reads
entries two at a time against a published brief and keeps the funnier one.

The entry: a single joke about office life, setup and turn, punchline last.
`main.py` writes the line to `/output/entry.txt`.

## The line

> Someone keeps stealing my lunch from the shared fridge, so I labelled it 'Dave's' — nobody has touched it in three weeks, including Dave.

## How it runs

`main.py` writes the joke to `/output/entry.txt`. Before writing, it enforces
the sealed 1–200 character gate, raising a `ValueError` if the line falls
outside it. The line is 137 characters.
