import json
from src.CurlHelper import CurlHelper
from src.Constants import Constants
import git
import os


class GithubHelper:

    @staticmethod
    def get_github_release_info(release_link):
        """
        Retuns json object from gihub api from release
        :param release_link:
        :return: json object
        """
        release_json = json.loads(CurlHelper.get_curl_string(release_link))
        return release_json

    @staticmethod
    def release_notes_exist(release_link):
        release_json = GithubHelper.get_github_release_info(release_link)
        release_notes = release_json[Constants.GITHUB_RELEASE_BODY]
        return release_notes is None

    @staticmethod
    def release_notes_contain_codeword(release_link, codeword):
        """
        Retuns true of code word found in release notes
        :param release_link:
        :param codeword:
        :return: boolean
        """
        mention = False
        release_json = GithubHelper.get_github_release_info(release_link)
        release_notes = release_json[Constants.GITHUB_RELEASE_BODY]
        if codeword in release_notes:
            mention = True
        return mention

    @staticmethod
    def get_last_release_tag(repo_directory):
        """
        Returns latest tag
        :return: string
        """
        curr_dir = os.getcwd()
        os.chdir(repo_directory)
        repo = git.Repo(search_parent_directories=True)
        release_candidate_tag = str(repo.tags[-1])
        os.chdir(curr_dir)
        return release_candidate_tag

    @staticmethod
    def get_release_asset_size(release_link):
        """
        Returns size of release asset
        :param release_link:
        :return: string
        """
        release_json = GithubHelper.get_github_release_info(release_link)
        release_asset_size = release_json[Constants.GITHUB_ASSETS][0][Constants.GITHUB_ASSET_SIZE]
        return release_asset_size
