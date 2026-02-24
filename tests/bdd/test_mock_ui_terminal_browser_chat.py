import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[2]
MOCK_PATH = ROOT / "mocks" / "pair_plan_response.json"
FEATURE_PATH = ROOT / "tests" / "bdd" / "features" / "ui_terminal_browser_chat.feature"


class TestMockedPairPlanBDD(unittest.TestCase):
    def test_feature_uses_high_level_bdd_terms(self) -> None:
        text = FEATURE_PATH.read_text(encoding="utf-8")
        self.assertIn("Feature:", text)
        self.assertIn("Scenario:", text)
        self.assertIn("terminal", text.lower())
        self.assertIn("browser", text.lower())
        self.assertIn("chat", text.lower())
        self.assertIn("opencode webui", text.lower())

    def test_mock_pair_contains_expected_hoster_roles(self) -> None:
        payload = json.loads(MOCK_PATH.read_text(encoding="utf-8"))
        self.assertEqual(payload["status"], "ok")
        self.assertGreaterEqual(len(payload["pairs"]), 1)

        pair = payload["pairs"][0]
        self.assertIn("electerm_hoster", pair)
        self.assertIn("opencode_hoster", pair)

        electerm_ref = pair["electerm_hoster"]["mcp_reference"]
        opencode_ref = pair["opencode_hoster"]["mcp_reference"]
        self.assertIn("MCP-Widget-Usage-Guide", electerm_ref)
        self.assertIn("MCP-Widget-Usage-Guide", opencode_ref)

    def test_mock_ui_actions_cover_requested_flows(self) -> None:
        payload = json.loads(MOCK_PATH.read_text(encoding="utf-8"))
        actions = [a.lower() for a in payload["pairs"][0]["ui_actions"]]

        required_terms = [
            "desktop panel",
            "terminal widget",
            "browser widget",
            "chat",
            "opencode webui",
        ]
        flattened = " | ".join(actions)
        for term in required_terms:
            with self.subTest(term=term):
                self.assertIn(term, flattened)


if __name__ == "__main__":
    unittest.main()
