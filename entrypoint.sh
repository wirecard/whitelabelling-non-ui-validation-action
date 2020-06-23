#!/bin/sh -l

cp scripts/*.json /scripts/src
export PYTHONPATH=/scripts/
export PYTHONUNBUFFERED=1
TEST_TYPE=$1

if [ "${TEST_TYPE}" = "test_files_and_github" ]; then
  echo "Running tests"
  cd ${GITHUB_WORKSPACE}/scripts
  python -m unittest src.test_Files.TestFiles
  python -m unittest src.test_GithubRelease.TestGithubRelease
else
    echo "Other action that 'test_files_and_github' is not available"
fi