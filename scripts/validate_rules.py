from pathlib import Path
import re
import sys

REQUIRED_META_KEYS = {
    "author",
    "description",
    "severity",
    "date",
    "platform",
    "logsource",
}


def extract_meta_block(text: str) -> str:
    match = re.search(r"meta:\s*(.*?)\n\s*events:", text, re.DOTALL)
    return match.group(1) if match else ""



def validate_rule(path: Path) -> list[str]:
    errors: list[str] = []
    content = path.read_text(encoding="utf-8")

    if "rule " not in content:
        errors.append("Missing rule declaration")

    if "events:" not in content:
        errors.append("Missing events block")

    if "condition:" not in content:
        errors.append("Missing condition block")

    meta_block = extract_meta_block(content)
    if not meta_block:
        errors.append("Missing or malformed meta block")
    else:
        found_keys = set(re.findall(r"^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=", meta_block, re.MULTILINE))
        missing = REQUIRED_META_KEYS - found_keys
        for key in sorted(missing):
            errors.append(f"Missing required meta key: {key}")

    return errors



def main() -> int:
    rules_dir = Path("rules")
    if not rules_dir.exists():
        print("rules/ directory not found")
        return 1

    failures = 0
    for rule_file in sorted(rules_dir.glob("*.yaral")):
        errors = validate_rule(rule_file)
        if errors:
            failures += 1
            print(f"[FAIL] {rule_file}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"[OK]   {rule_file}")

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
