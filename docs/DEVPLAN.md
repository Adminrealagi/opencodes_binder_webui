# Dev Plan: Containerized Kali Electerm + OpenCode Pair Executors

## Goal

Create a predictable mocked system where each request can form a pair of executors:

1. Electerm hoster machine (with MCP integration references).
2. OpenCode hoster machine (with MCP access workflow references).

Both are represented as containerized Kali-based images, with CI publishing to registries and BDD-style mocked tests that describe visible UI activity in terminals and browsers.

## Scope

- Sane clickable visible desktop activity and panel widget presets in Kali containers.
- RPA/robotization framework tooling installed in images.
- Common cloud and CLI tooling installed in images:
  - `gh`, `az`, `gcloud`, `aws`, `docker`, `jq`, `yq`, tabular tools.
- GitHub Actions Docker workflow for image build and push to registries.
- Mock-first BDD tests using high-level UI steps for terminal/browser/chat/OpenCode WebUI flows.

## Architecture (Mocked in this repository)

- Pair planner returns pre-canned JSON for executor pair selection.
- No real Kubernetes scheduling is executed from this repo.
- UI and chat actions are validated as behavioral contracts against mocked responses.

## Container Strategy

### Image 1: electerm-hoster

- Base: `kalilinux/kali-rolling`.
- Includes desktop + remote UI stack for visible interactions:
  - `xfce4`, `xfce4-goodies`, `x11vnc`, `xvfb`, `novnc`, `websockify`, `dbus-x11`.
- Includes browser and terminal tooling:
  - `firefox-esr`, `tmux`, `xterm`, `curl`, `git`.
- Includes RPA and automation tooling:
  - Python + `playwright`, `selenium`, `robotframework`.

### Image 2: opencode-hoster

- Base: `kalilinux/kali-rolling`.
- Includes desktop + remote UI stack:
  - `xfce4`, `xfce4-goodies`, `x11vnc`, `xvfb`, `novnc`, `websockify`, `dbus-x11`.
- Includes cloud/ops and query tooling:
  - `gh`, `awscli`, `jq`, `yq`, `python3`, `pip`.
- Includes extensible placeholders for:
  - `az` and `gcloud` bootstrap hooks via scripts.

## Desktop Widget/Panel Presets

- Keep a deterministic XFCE panel preset profile mounted into the container.
- Presets should include launchers for:
  - Terminal
  - Firefox
  - Electerm host UI
  - OpenCode WebUI
  - Chat widget page
- For CI and local reproducibility, presets are generated and applied from scripts instead of manual UI edits.

## RPA Framework Plan

- Browser/UI:
  - Playwright (primary)
  - Selenium (secondary compatibility)
  - Robot Framework keyword orchestration
- Terminal flow automation:
  - tmux script orchestration
  - deterministic command logs for assertions

## GitHub Actions Registry Publishing

- Workflow: `.github/workflows/docker-publish.yml`
- Build strategy:
  - matrix build for both images (`electerm-hoster`, `opencode-hoster`)
  - tags: `sha`, `latest`
- Default registry target in this repository:
  - GHCR (`ghcr.io/<owner>/opencodes-binder-webui/<image-name>`)

## BDD Mock Testing Plan

- Feature contracts stored as Gherkin-like `.feature` files.
- Python mock test suite validates:
  - pair planner responses
  - required high-level steps and UI terms
  - endpoint/action coverage for terminal + browser + chat + OpenCode WebUI

## Delivery Checklist

- [x] Dev plan document
- [x] Dockerfiles for both hosters
- [x] Docker publish GitHub Actions workflow
- [x] Mock JSON response contract
- [x] BDD-style mocked tests for high-level UI actions
