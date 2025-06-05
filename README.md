# Privacy Leakage in LLM-based Code Generation via Test Case Generation

This repository provides the official implementation of a **semi-automated pipeline** for evaluating privacy leakage risks in Large Language Models (LLMs) when generating code and corresponding test cases.

---

## 🔍 Overview

LLMs trained on publicly available code may inadvertently leak sensitive data like usernames, emails, passwords, access keys, and health or financial information. This project proposes a **test-case generation framework** to systematically uncover and verify such privacy leaks.


---

## 🧩 Pipeline Structure

The pipeline contains 4 major components:

1. **Privacy Feature Library Construction**  
   Read real-world coding scenarios and privacy-related attributes from Excel.

2. **Task & Code Generation**  
   Use LLMs to generate privacy-sensitive tasks and corresponding code.

3. **Test Case Generation**  
   Use a privacy feature library to generate realistic, diverse inputs with LLM.

4. **Leak Verification**  
   Verify leaked content through a Judge LLM, GitHub search, and human review.

---

## 📁 Directory Structure

```bash
.
├── GPTask.py                         # Main script to run the full pipeline
├── feature_library.py              # Construct library
├── privacy_feature_library.jsonl  # Structured privacy attribute patterns
├── HumanReview.py                # Simple Tool for human review
├── gerAttribute.py      
├── Output/                        # (GPT-4o examples included)
│   ├── Questions/                 # Code generation questions 
│   ├── Cases/                     # Generated test cases
│   ├── Judge/                     # Judgment results from LLM judge 
│   ├── Search/                    # GitHub search results for candidate privacy content
│   └── Human/                     # Human-labeled results 


