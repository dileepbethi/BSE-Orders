# Order Value Extractor V2

## Objective

Extract the commercial order value from corporate announcements with high accuracy.

---

## Inputs

Raw OCR text

---

## Output

Examples

18,53,66,820

157.97 Lakhs

495.80 Crore

USD 51.98 million

---

## Challenges

- OCR merged text
- Broken lines
- Tables
- Currency formats
- Hidden values
- MW values that are NOT money

---

## Pipeline

Normalize Text

↓

Find Context

↓

Extract Candidate Values

↓

Validate Candidate

↓

Return Best Match