# Engineering Log

## Sprint 1 - PDF Text Extraction

### Goal

Extract text from PDF resumes.

### Design Decisions

- Used PyPDF for text extraction.
- Separated document extraction from AI processing.

### Challenges

- Python import issue due to package structure.

### Resolution

- Converted app into a Python package.
- Executed using `python -m app.main`.

### Learning

- Learned Python package imports and separation of concerns.

---

## Sprint 2 - Resume Parser Node

Sprint: 2

Task: Education Model

Completed

Created the first Pydantic domain model.
Chose optional scalar fields.
Adopted None as the representation for missing values.

Learning

Domain models should represent data, not UI-friendly text.

---
