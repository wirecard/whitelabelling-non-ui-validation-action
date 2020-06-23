from unittest import TestCase
from src.GithubHelper import GithubHelper
from src.Constants import Constants
from src.FileActionHelper import FileActionHelper
import os


class TestGithubRelease(TestCase):

    def setUp(self) -> None:
        self.extension = os.getenv("EXTENSION")
        self.repo_slug = os.getenv("REPO_SLUG")
        self.workspace = os.getenv("GITHUB_WORKSPACE")
        self.github_release_info_link = "{}/{}/releases/tags/{}".format(Constants.GITHUB_API_LINK, self.repo_slug,
                                                                        GithubHelper.get_last_release_tag(self.workspace))
        self.data_list = FileActionHelper.get_extension_file_data(self.extension)

    def test_release_notes_contain_codeword(self):
        self.assertFalse(GithubHelper.release_notes_contain_codeword(self.github_release_info_link,
                                                                     Constants.WIRECARD))

    def test_release_asset_size_smaller_than_value(self):
        self.assertGreater(int(self.data_list[Constants.MAX_RELEASE_ASSET_SIZE]),
                           int(GithubHelper.get_release_asset_size(self.github_release_info_link)))
