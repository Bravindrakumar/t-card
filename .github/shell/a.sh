#!/bin/bash
spinup_dir=grep -r --exclude_dir={'zx', 'ab'} /b
echo "::set-output name=matrix::$(ls b/** | jq -R -s -c 'split("\n")[:-1]')"
