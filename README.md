---
license: cc-by-4.0
language:
- nl
- fr
pretty_name: Belgian legal lexicon Dutch-French (procedure)
task_categories:
- translation
tags:
- legal
- terminology
- belgium
- glossary
size_categories:
- n<1K
configs:
- config_name: default
  data_files:
  - split: train
    path: data/lexicon.jsonl
---

# Belgian legal lexicon, Dutch-French (procedure)

Thirty Dutch terms of Belgian court procedure with their French equivalent, each one tied to the article of law where both language versions use it.

Belgian statutes are published in Dutch and in French, so the law itself fixes the equivalent. For every term, this lexicon quotes the provision in both languages, gives the usual translation pitfall and adds one sample sentence in Dutch and in French.

Author: Philippe Lognoul, translator since 1992 ([bysaro.com](https://bysaro.com), [ORCID 0009-0000-3951-5667](https://orcid.org/0009-0000-3951-5667)).
Human-readable version: [bysaro.be/lexique](https://bysaro.be/lexique/) (French) and [bysaro.be/nl/lexicon](https://bysaro.be/nl/lexicon/) (Dutch).

## Files

| File | Content |
|---|---|
| `data/lexicon.csv` | One row per term, UTF-8 with byte order mark, opens in a spreadsheet |
| `data/lexicon.json` | Full entries, with the quoted provisions |
| `data/lexicon.jsonl` | Same entries, one per line |

## Fields

| Field | Meaning |
|---|---|
| `id` | Stable identifier of the term |
| `term_nl`, `term_fr` | Dutch term and French equivalent |
| `equivalence_fr`, `equivalence_nl` | Why this equivalent holds, in French and in Dutch |
| `pitfall_fr`, `pitfall_nl` | The usual translation error, in French and in Dutch |
| `example_nl`, `example_fr` | One sample sentence and its translation |
| `related` | Identifiers of neighbouring terms |
| `sources` | For each provision: instrument, article, quotation in Dutch and in French, link to the official text (JSON files) |
| `source_references`, `source_urls_nl`, `source_urls_fr` | The same references, flattened (CSV file) |
| `page_fr`, `page_nl` | Page of the term on bysaro.be |
| `first_published` | Date of first publication on bysaro.be |

## Sources

Fifty-nine references to official Belgian texts: the Judicial Code (Gerechtelijk Wetboek, Code judiciaire), Book XX of the Code of Economic Law (Wetboek van economisch recht, Code de droit économique) and one page of the Federal Public Service Employment. Legislation was read on Justel, the consolidated legislation database of the Belgian Federal Public Service Justice, on 3, 10 and 17 November 2026. Each entry links to the text it quotes. Legislation changes: check the current version before relying on a quotation.

## Scope and limits

Version 1.0 of 21 November 2026 holds 30 terms; the lexicon on bysaro.be grows every week and later versions will follow. The entries cover Belgian law only: Dutch legal terms used in the Netherlands often carry another meaning. The lexicon is a translation aid and gives no legal advice.

## Licence and citation

Lexicon entries: [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/). The quoted provisions come from the official texts linked in each entry.

Please cite: Philippe Lognoul, *Belgian legal lexicon, Dutch-French (procedure)*, version 1.0, 2026, https://bysaro.be/lexique/.

## Français

Trente termes néerlandais de la procédure belge et leur équivalent français. Chaque équivalence s’appuie sur l’article de loi où les deux versions linguistiques emploient le terme. Chaque entrée cite la disposition dans les deux langues, signale l’erreur de traduction courante et donne une phrase d’exemple en néerlandais et en français.

Les textes ont été lus sur Justel, la base de législation consolidée du SPF Justice, les 3, 10 et 17 novembre 2026. Le lexique porte sur le seul droit belge. Il aide à traduire et ne donne aucun conseil juridique. Réutilisation libre sous licence CC BY 4.0, avec mention de l’auteur.

## Nederlands

Dertig Nederlandse termen uit het Belgische procesrecht met hun Franse equivalent. Elke gelijkwaardigheid steunt op het wetsartikel waarin beide taalversies de term gebruiken. Elke ingang citeert de bepaling in beide talen, wijst op de gebruikelijke vertaalfout en geeft een voorbeeldzin in het Nederlands en in het Frans.

De teksten zijn geraadpleegd op Justel, de databank met geconsolideerde wetgeving van de FOD Justitie, op 3, 10 en 17 november 2026. Het lexicon behandelt alleen Belgisch recht. Het is een hulpmiddel bij het vertalen en geeft geen juridisch advies. Vrij hergebruik onder de licentie CC BY 4.0, met naamsvermelding.
