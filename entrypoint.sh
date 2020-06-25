#!/bin/sh -l


cp -r /script/*.json /script/src/*.json
TEST_TYPE=$1

if [ "${TEST_TYPE}" = "test_files_and_github" ]; then
  cd /script
  python src/main.py
else
    echo "Other action that 'test_files_and_github' is not available"
fi