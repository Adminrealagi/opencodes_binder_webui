# Essential Rules For Agents

- Always run tests and builds before and after changes.
- Always enforce a hard max of 300 lines per file across source and infrastructure files.
- Always add language linting and lint harnesses to CI for all relevant file types.
- Always lint Dockerfiles, Compose files, and workflow/infrastructure configs.
- Always log user prompts verbatim in `PROMPTS.csv`.
- Always log a short execution summary in `CHANGELOG.md`.
- Never overwrite manually added documentation fragments.
- When creating console TUIs or rich CLIs with options, add a VHS GitHub Actions demo and link it in the project README.
- If blocked and unable to complete correctly, create `.agents.todo.<name>.md` tombstones with issues and next steps.
