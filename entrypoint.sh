#!/bin/sh -l


cp -r /script/*.json /script/src/*.json
TEST_TYPE=$1

if [ "${TEST_TYPE}" = "test_files_and_github" ]; then
  cd /script
  echo "Runninng file related tests"
  python -m unittest src.test_Files.TestFiles
  echo "Running Github release related tests"
  python -m unittest src.test_GithubRelease.TestGithubRelease
else
    echo "Other action that 'test_files_and_github' is not available"
fi