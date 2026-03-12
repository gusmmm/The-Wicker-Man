---
id: baux-score
version: "0.0.1"
created_at: "2026-03-11"
updated_at: "2026-03-11"
title: "Baux Score"
description: "The original prognostic index for burn mortality based on age and TBSA."
aliases: ["Baux Index"]
links:
  "Wikipedia": "https://en.wikipedia.org/wiki/Baux_score"


# Standards Mapping
loinc_code: null
snomed_concept: "246111003" # prognostic score
omop_domain: "Measurement"

components:
  - name: "Age"
    coding: { system: "LOINC", code: "30525-0", display: "Age" }
    data_type: "int"
    unit: "years"
  - name: "TBSA"
    coding: { system: "LOINC", code: "3139-3", display: "Burn surface area - total body - measured" }
    data_type: "float"
    unit: "percent"

formula_latex: "$$Score = Age + TBSA$$"
calculation_logic: "age + tbsa"
reference_doi: ["10.1097/TA.0b013e31824052bb"]

interpretation_table:
  "160": "The point of futility (the Baux Score at which predicted mortality is 100%)"
  "109.6" : "The Baux50 (the Baux score at which predicted mortality is 50%)" 
---

# Baux Score
The Baux score is a, historically significant, 1961-developed tool predicting burn mortality by adding age and total body surface area (TBSA) burned. Due to improved survival rates, it was updated to the Revised Baux (rBaux) score, which adds 17 points if inhalation injury is present.
- Original Formula (1961): a score > 75 indicated an unfavourable prognosis.