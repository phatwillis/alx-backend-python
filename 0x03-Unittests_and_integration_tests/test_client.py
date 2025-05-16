#!/usr/bin/env python3
"""testing client.py methods"""
import unittest
from unittest.mock import MagicMock, Mock, PropertyMock, patch

from parameterized import parameterized, parameterized_class
from requests import HTTPError

from client import *
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """GitHub org client class"""

    @parameterized.expand([("google",),
                           ("abc")])
    @patch('client.get_json')
    def test_org(self, org, mock_getjson: MagicMock) -> None:
        """test that the correct org is returned"""
        new_client = GithubOrgClient(org_name=org)
        self.assertEqual(new_client._org_name, org)
        mock_getjson.return_value = {"payload": True}
        mock_getjson()
        mock_getjson.assert_called_once()

    @patch.object(GithubOrgClient, '_public_repos_url',
                  new_callable=PropertyMock)
    def test_public_repos_url(self, mock_property: MagicMock) -> None:
        """mocking a @property"""
        mock_property.return_value = {"payload": True}
        self.assertEqual(mock_property.return_value, {"payload": True})

    @patch('client.get_json')
    def test_public_repos(self, mock_get: MagicMock) -> None:
        """test public repos function"""
        # using patch as a context manager
        with patch.object(GithubOrgClient, "_public_repos_url",
                          MagicMock(return_value="https://api.github.com/"
                                                 "orgs/google/"
                                                 "repos")) as mock_repos_url:
            repo_url = mock_repos_url
            # give the mock get request of the repos url a mock response
            mock_get.return_value = [
                {
                    "id": 123,
                    "name": "repo1",
                    "description": "description of repo1",
                    "owner": {
                        "login": "user1",
                        "id": 456
                    },
                    "html_url": "https://github.com/user1/repo1",
                    "stargazers_count": 10,
                    "language": "Python",
                    "created_at": "2022-04-22T11:11:11Z",
                    "updated_at": "2022-04-23T12:12:12Z"
                },
                {
                    "id": 234,
                    "name": "repo2",
                    "description": "description of repo2",
                    "owner": {
                        "login": "user2",
                        "id": 567
                    },
                    "html_url": "https://github.com/user2/repo2",
                    "stargazers_count": 20,
                    "language": "JavaScript",
                    "created_at": "2022-04-22T13:13:13Z",
                    "updated_at": "2022-04-23T14:14:14Z"
                }
            ]
            json_resp = mock_get(repo_url)

            self.assertEqual(json_resp, mock_get.return_value)
            mock_get.assert_called_once()

    @parameterized.expand([({"license": {"key": "my_license"}}, "my_license", True),
                           ({"license": {"key": "other_license"}}, "my_license", False)])
    def test_has_license(self, repo: Dict, license_key: str, result: bool):
        license_check = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(license_check, result)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration testing class
    Excerpted from Tolulope Fakunle"""

    @classmethod
    def setUpClass(cls) -> None:
        """Sets up class fixtures before running tests."""
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """Tests the `public_repos` method."""
        self.assertEqual(
            GithubOrgClient("google").public_repos(),
            self.expected_repos,
        )

    def test_public_repos_with_license(self) -> None:
        """Tests the `public_repos` method with a license."""
        self.assertEqual(
            GithubOrgClient("google").public_repos(license="apache-2.0"),
            self.apache2_repos,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """Removes the class fixtures after running all tests."""
        cls.get_patcher.stop()
