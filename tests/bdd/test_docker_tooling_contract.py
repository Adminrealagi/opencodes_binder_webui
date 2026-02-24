from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[2]


class TestDockerToolingContract(unittest.TestCase):
    def test_requested_cloud_and_cli_tools_are_declared(self) -> None:
        dockerfiles = [
            ROOT / "docker" / "electerm-hoster.Dockerfile",
            ROOT / "docker" / "opencode-hoster.Dockerfile",
        ]
        required_markers = [
            "gh",
            "google-cloud-cli",
            "awscli",
            "docker.io",
            "azure-cli",
            "jq",
            "yq",
            "miller",
            "csvkit",
            "tabulate",
            "playwright",
            "robotframework",
            "selenium",
        ]

        for path in dockerfiles:
            text = path.read_text(encoding="utf-8")
            lowered = text.lower()
            for marker in required_markers:
                with self.subTest(file=str(path), marker=marker):
                    self.assertIn(marker, lowered)


if __name__ == "__main__":
    unittest.main()
