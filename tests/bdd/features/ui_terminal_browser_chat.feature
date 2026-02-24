Feature: Mocked paired hosters provide visible UI flows
  As an operator of the binder web app
  I want mocked pair planning and UI action descriptions
  So that terminal and browser workflows are testable without live infrastructure

  Scenario: Pair planning returns electerm and opencode hosters
    Given a mocked pair-plan response exists
    When the planner response is loaded
    Then it contains an electerm hoster and an opencode hoster
    And both hosters reference MCP widget usage guidance

  Scenario: High-level UI actions include desktop, terminal, browser, chat and opencode webui
    Given a mocked pair-plan response exists
    When the UI actions are inspected
    Then the actions include desktop panel presets
    And the actions include terminal widget interaction
    And the actions include browser widget interaction
    And the actions include chat access
    And the actions include opencode webui access
