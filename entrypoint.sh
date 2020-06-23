#!/bin/sh -l

cp -r /usr/bin/src/ $GITHUB_WORKSPACE/
cp -r /usr/bin/*.json $GITHUB_WORKSPACE/src
export PYTHONPATH=$GITHUB_WORKSPACE/
export PYTHONUNBUFFERED=1
TEST_TYPE=$1

if [ "${TEST_TYPE}" = "test_files_and_github" ]; then
  echo "Running tests"
  echo $GITHUB_WORKSPACE
  ls -la $GITHUB_WORKSPACE
  cd /github/workspace
  python -m unittest src.test_Files.TestFiles
  python -m unittest src.test_GithubRelease.TestGithubRelease
else
    echo "Other action that 'test_files_and_github' is not available"
fi