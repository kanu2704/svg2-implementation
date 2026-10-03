# PVSG, Option A: pipeline vs human labels

Videos: 0027_4571353789, 0028_4021064662, 0039_6951351121, 1122_3393449055

## Objects

| video | human things | things found | human stuff | stuff found | our tracks | extra tracks | named right | matched & described |
|---|---|---|---|---|---|---|---|---|
| 0027_4571353789 | 12 | 9 | 4 | 1 | 57 | 47 | 8 | 10 |
| 0028_4021064662 | 8 | 4 | 2 | 2 | 8 | 2 | 4 | 6 |
| 0039_6951351121 | 14 | 2 | 3 | 2 | 36 | 32 | 1 | 4 |
| 1122_3393449055 | 8 | 8 | 1 | 0 | 47 | 39 | 6 | 8 |

Human stuff named as a person: 2

## Naming errors

- 0027_4571353789: human `tree` → ours `bush` (`plant`)
- 0027_4571353789: human `table` → ours `tablecloth` (`cloth`)
- 0028_4021064662: human `ground` → ours `car` (`car`)
- 0028_4021064662: human `grass` → ours `child` (`child`)
- 0039_6951351121: human `sky` → ours `cloud` (`none`)
- 0039_6951351121: human `grass` → ours `person` (`adult`)
- 0039_6951351121: human `adult` → ours `football` (`ball`)
- 1122_3393449055: human `child` → ours `baby` (`baby`)
- 1122_3393449055: human `table` → ours `countertop` (`countertop`)

## Relations

| video | human relations | correct | wrong time | wrong predicate | reversed | pair not related | object missed | our relations | ours between found objects | of those also in PVSG (any time) | our predicates with no PVSG match |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0027_4571353789 | 17 | 1 | 1 | 1 | 0 | 4 | 10 | 10 | 7 | 2 | 6 |
| 0028_4021064662 | 18 | 0 | 0 | 4 | 0 | 8 | 6 | 11 | 9 | 0 | 2 |
| 0039_6951351121 | 13 | 0 | 0 | 0 | 0 | 1 | 12 | 10 | 0 | 0 | 4 |
| 1122_3393449055 | 11 | 2 | 1 | 5 | 0 | 3 | 0 | 12 | 9 | 3 | 5 |

![naming errors](naming_errors.png)
