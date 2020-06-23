from src.FileActionHelper import FileActionHelper
from src.Constants import Constants
from unittest import TestCase
import os


class TestFiles(TestCase):

    def setUp(self) -> None:
        self.extension = os.getenv("EXTENSION")
        self.workspace = os.getenv("GITHUB_WORKSPACE")
        self.data_list = FileActionHelper.get_extension_file_data(self.extension)

    def test_readme_file(self):
        self.assertFalse(FileActionHelper.file_contains_code_word(
            FileActionHelper.get_file_path(self.data_list[Constants.README_FILE], self.workspace), Constants.WIRECARD))

    def test_license_file(self):
        self.assertFalse(FileActionHelper.file_contains_code_word(
            FileActionHelper.get_file_path(self.data_list[Constants.LICENSE_FILE], self.workspace), Constants.WIRECARD))

    def test_changelog_file(self):
        self.assertFalse(FileActionHelper.file_contains_code_word(
            FileActionHelper.get_file_path(self.data_list[Constants.CHANGELOG_FILE], self.workspace), Constants.WIRECARD))

    def test_picture_file_names(self):
        folder_path = FileActionHelper.get_folder_path(self.data_list[Constants.IMAGES_FOLDER_NAME], self.workspace)
        self.assertFalse(FileActionHelper.files_in_folder_contain_code_word(folder_path, Constants.WIRECARD))

    def test_github_links(self):
        self.assertFalse(FileActionHelper.files_contain_codeword(self.workspace, Constants.WIRECARD_GITHUB_LINK))
