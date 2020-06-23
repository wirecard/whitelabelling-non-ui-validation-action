class Constants:

    SHOP_EXTENSION_DATA_FILE_PATH = 'shopsystems-extensions-data.json'

    IMAGES_FOLDER_NAME = "images_folder_name"
    README_FILE = "readme_file"
    LICENSE_FILE = "license_file"
    CHANGELOG_FILE = "changelog_file"
    MAX_RELEASE_ASSET_SIZE = "max_release_asset_size"

    WIRECARD = "wirecard"

    GITHUB_DOMAIN = "github.com"
    WIRECARD_GITHUB_LINK = "{}/{}".format(GITHUB_DOMAIN, WIRECARD)
    GITHUB_API_LINK = "https://api.{}/repos".format(GITHUB_DOMAIN)
    GITHUB_ASSETS = "assets"
    GITHUB_ASSET_SIZE = "size"
    GITHUB_RELEASE_BODY = "body"

    BLACKLIST_FOLDERS = [".git", "vendor", ".github"]
    BLACKLIST_FILES = [".travis.yml"]
