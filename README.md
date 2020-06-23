# Wirecard whitelabelling non UI validation

This project contains validations for whitelabelled extensions before they can be released on partner plugin.

# What it does
This is pytest based test suite. Each `test_*` class contains set of validation for that class.

# How to run
- Prepare the system and install pip dependencies
`pip install pycurl gitpython`
 - Export environment variables

    Example:
    ```
    EXTENSION=woocommerce-ee #extension name as in wirecard organisation
    GITHUB_WORKSPACE='/github/workspace' # location of the whitelabelled extension files
    REPO_SLUG='wirecard-cee/caps-woocommerce-ee'
    AUTH_TOKEN='token' # token that has access to private repositories
    ```
 - Run the scripts
 `python -m unittest test_Files.TestFiles`
 or  `python -m unittest test_GithubRelease.TestGithubRelease`
