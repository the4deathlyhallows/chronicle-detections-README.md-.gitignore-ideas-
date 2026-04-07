# ClickFix macOS Terminal / curl / base64 / osascript

## Objective
Detect ClickFix-style macOS execution chains where Terminal or iTerm launches shell activity involving `curl`, `echo`, `base64 -d`, pipe-to-shell execution, `sh -c`, or `osascript`.

## Why this matters
This pattern aligns with user-executed social engineering chains that abuse native interpreters and staged command execution.

## Data sources
- macOS EDR process execution
- UNIX process telemetry
- File monitoring where available

## Detection hypothesis
A suspicious parent-child chain or a command line should show one or more of these traits:
- Terminal or iTerm launches `bash`, `zsh`, `sh`, or `osascript`
- Command includes `curl` or `http`
- Command includes `base64 -d` or decode behavior
- Pipe-to-shell execution such as `| bash`, `| sh`, `bash -c`, `sh -c`
- AppleScript execution that triggers shell actions

## Initial logic
Focus on process command lines and parent-child relationships, then tighten around combinations instead of single noisy tokens.

## Blind spots / assumptions
- Requires command-line visibility
- May miss heavily obfuscated payloads
- Some admin or developer activity may partially resemble this

## Testing plan
- Simulate `curl | bash`
- Simulate `echo <base64> | base64 -d | sh`
- Simulate `osascript -e 'do shell script ...'`

## Known false positives
- Developer testing
- Admin scripts
- Security team lab validation

## Tuning notes
Prioritize combinations involving Terminal parent + network retrieval + decode / shell execution.
