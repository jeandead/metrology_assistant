# Install on Gemini CLI

```bash
# After running `bash scripts/build.sh --platform gemini-cli`:
cp -R dist/gemini-cli/. /path/to/your/vault/
```

Then in your vault:

- `GEMINI.md` is the operating manual Gemini reads at session start.
- `.gemini/commands/*.md` are the command bodies the AI follows.
- `.gemini/scripts/` holds the Python helpers (`uv run -m scripts.research.<name>`).
