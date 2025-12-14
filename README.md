# gitgrade-analyzer
# GitGrade Repository Analyzer

## Overview
This project analyzes a public GitHub repository and generates a score, summary, and personalized improvement roadmap. The goal is to simulate how a recruiter or mentor evaluates a developer’s GitHub project.

## Input
- Public GitHub Repository URL

## Output
- Score (out of 100)
- Short quality summary
- Actionable improvement roadmap

## How It Works
The system uses rule-based evaluation to assess:
- Repository accessibility
- Documentation presence
- Project structure
- Test coverage
- Commit consistency

Based on these checks, it generates an honest evaluation and improvement steps.

## How to Run
```bash
python analyzer.py
