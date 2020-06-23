# Wirecard whitelabelling non UI validation action

This action automates validations for whitelabelled extensions before they can be released on partner plugin.

# What it does
This is pytest based test suite. Each `test_*` class contains set of validation for that class.
- With parameter `action` =  `test_files_and_github`
    - Perform "file" based checks
    - Perform check of release on private repository 
- With parameter `test_emails_after_ui_tests`
   - TBD

# How to setup
- Add action into your workflow as in the example
    - Important notes:
        - Set environment variables
            - `EXTENSION_NAME` - name of extension as per wirecard/{extension-name}
            - `REPO_SLUG`
            - `TOKEN` - token with access to private repository releases information

    Example:
 ```
name: Run non UI whitelabeled extension checks

on: push

jobs:
  run-non-whitelabelling-tests:
    runs-on: ubuntu-latest
    name: Run non UI whitelabeled extension checks
    steps:
     - name: Checkout ${{ github.event.repository.name }}
       uses: wirecard/checkout@v2.0.0
       with:
         ref: ${{ github.head_ref }}
     - name: Get tags
       run: git fetch --prune --unshallow
     - name: Run non UI whitelabelled extension checks
       uses: wirecard/whitelabelling-non-ui-validation-action@master
       with:
         action: test_files_and_github
       env:
         EXTENSION: 'woocommerce-ee'
         REPO_SLUG: ${{ github.repository }}
         TOKEN: ${{ secrets.SHOP_SYSTEM_BOT }}
```
- Running locally
```

docker build . -t white
docker run -it \
-v /path-to-private-repository:/github/workspace \
-e EXTENSION=extension-name \
-e GITHUB_WORKSPACE='/github/workspace' \
-e REPO_SLUG='repo/slug' \
-e TOKEN='auth-token' \
white test_files_and_github
```

