# Chronicle Detection Engineering Repo

This repository is a simple Detection-as-Code starter kit for Chronicle / Google SecOps detections.

## Goals
- Store YARA-L detections in Git
- Keep detection ideas documented
- Validate detections before merge
- Package rules in CI
- Create a clean portfolio project that shows detection engineering maturity

## Layout
- `ideas/` = rationale, test notes, false positives, blind spots
- `rules/` = YARA-L detections
- `scripts/` = validation and helper tooling
- `.github/workflows/` = CI automation

## Suggested workflow
1. Open an issue for a new detection idea
2. Create or update a markdown file in `ideas/`
3. Add or tune the rule in `rules/`
4. Run local validation
5. Push branch and open pull request
6. Let GitHub Actions validate and package the content
7. Merge after review

## Local usage
```bash
python3 scripts/validate_rules.py
python3 scripts/package_rules.py
