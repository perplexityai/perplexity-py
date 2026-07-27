import unittest

from commitlint import valid_subject


class CommitlintTest(unittest.TestCase):
    def test_conventional_commits(self) -> None:
        self.assertTrue(valid_subject("feat: add search"))
        self.assertTrue(valid_subject("fix(client)!: drop legacy mode"))
        self.assertTrue(valid_subject("Merge pull request #1"))

    def test_invalid_commits(self) -> None:
        self.assertFalse(valid_subject("add search"))
        self.assertFalse(valid_subject("feat add search"))


if __name__ == "__main__":
    unittest.main()
