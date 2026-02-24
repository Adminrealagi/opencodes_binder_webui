# opencodes_binder_webui

This is a web app that is a binder of the dockers (Kubernetes machines) with GitHub repository / opencode open and access via https://github.com/electerm/electerm accessed through web widgets.

## Purpose of this system

"per request it creates a pairs of the machine hosting https://github.com/electerm/electerm with mcp and machine hosting opencode with mcp access to https://github.com/electerm/electerm/wiki/MCP-Widget-Usage-Guide , based on infrastructure scaffolding / considerations of architecutre from the model predictor of optimal architecutre of pair(s) of executors of electerm-hosters and opencode-hosters, which in this repository are just fully mocked as simple precanned json responses."

## Implementation artifacts

- Development plan: `docs/DEVPLAN.md`
- Container images: `docker/electerm-hoster.Dockerfile`, `docker/opencode-hoster.Dockerfile`
- Local composition: `docker-compose.yml`
- Mock architecture outputs: `mocks/pair_plan_response.json`
- Registry publishing workflow: `.github/workflows/docker-publish.yml`
- BDD-style mock tests: `tests/bdd/features/ui_terminal_browser_chat.feature`, `tests/bdd/test_mock_ui_terminal_browser_chat.py`




# Essential rules for agents (TO BE WRITTENT INTO AGENTS.md.d/*.md!)

 - always run tests and builds before and after changes
 - always add linter rules "no more than 300 lines of code per file" to any language linter, add language linter and its harness and its harness into ci for every source code file / config in the repository. lint docker compose, dockerfiles and etc whatever infrastructure files too!
 - write user prompts into log inside of repository (PROMPTS.csv, verbatum)
 - write short log of your actions into log file inside of repository (CHANGELOG.md, as short as changelog usually is)
 - never overwrite manually added documentation like this fragment
 - 