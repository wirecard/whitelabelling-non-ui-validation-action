from src.Constants import Constants
import os
import json


class FileActionHelper:

    @staticmethod
    def get_file_path(file_name, start_path) -> str:
        """
        Returns filename path
        :return: string
        """
        file_path = None
        for root, dirs, files in os.walk(start_path):
            dirs[:] = [d for d in dirs if d not in Constants.BLACKLIST_FOLDERS]
            if file_name in files:
                file_path = os.path.abspath(os.path.join(root, file_name))
        return file_path

    @staticmethod
    def get_extension_file_data(extension):
        """
        Returns a json object
        :return: json
        """
        with open(FileActionHelper.get_file_path(Constants.SHOP_EXTENSION_DATA_FILE_PATH, os.getcwd()), 'r') \
                as data_json:
            json_content = json.loads(data_json.read())
            data_list = json_content[extension]
        return data_list

    @staticmethod
    def get_folder_path(folder_name, start_path):
        """
        Returns a path for provided folder
        :return: string
        """
        folder_path = None
        for root, dirs, files in os.walk(start_path):
            if folder_name in dirs:
                folder_path = os.path.abspath(os.path.join(root, folder_name))
        return folder_path

    @staticmethod
    def file_contains_code_word(file_path, code_word):
        """
        Returns true if code word found in file
        :return: boolean
        """
        mention = False
        with open(file_path, 'r') as text_file:
            try:
                text_lines = text_file.readlines()
                for line in text_lines:
                    if FileActionHelper.is_code_word_in_line(code_word, line):
                        print("Line '{}' contains {}\n".format(line, code_word))
                        mention = True
            except UnicodeDecodeError:
                pass
        return mention

    @staticmethod
    def files_in_folder_contain_code_word(folder_path, code_word):
        """
        Returns true if code word found in any file name in provided folder
        :return: boolean
        """
        mention = False
        for file in os.listdir(folder_path):
            if code_word in file:
                print("Found file {}\n".format(file))
                mention = True
        return mention

    @staticmethod
    def files_contain_codeword(folder_path, code_word):
        """
        Returns true if code word found in any file contents
        :return: boolean
        """
        mention = False
        for root, dirs, files in os.walk(folder_path):
            dirs[:] = [d for d in dirs if d not in Constants.BLACKLIST_FOLDERS]
            files[:] = [d for d in files if d not in Constants.BLACKLIST_FILES]
            for file in files:
                file_mention = FileActionHelper.file_contains_code_word(os.path.abspath(os.path.join(root, file)),
                                                                        code_word)
                if file_mention:
                    print("Found {} in {} \n".format(code_word, file))
                mention = mention or file_mention
        return mention

    @staticmethod
    def is_code_word_in_line(code_word, line):
        """
        Returns true if code word is in line
        :param code_word:
        :param line:
        :return: boolean
        """
        return code_word in line \
               or code_word.upper() in line \
               or code_word.lower() in line \
               or code_word.title() in line
