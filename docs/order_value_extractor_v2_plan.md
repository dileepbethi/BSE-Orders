# Order Value Extractor V2

## Goal

Extract the correct commercial order value from BSE/NSE corporate announcement PDFs.

---

## Supported Cases

- Rs. 125 Crore
- ₹ 125 Crore
- INR 125 Crore
- USD 51.98 million
- EUR
- GBP
- Plain Rupee Values
- Lakhs
- Crores
- Cr

---

## OCR Problems

- Rs.
  (in INR);
  18,53,66,820

- 2.157.97 Lakhs

- Broken table text

---

## Priority

1. Broad consideration
2. Size of Order
3. Gross Order Value
4. Contract Value
5. Order Value
6. Worth
7. Value of
8. Aggregating to

---

## Ignore

- Paid-up capital
- Share capital
- EPS
- Revenue
- Profit
- Net worth

---

## Pipeline

Normalize

↓

Context Search

↓

Priority Extraction

↓

Fallback Extraction

↓

Cleaning

↓

Validation

↓

Return