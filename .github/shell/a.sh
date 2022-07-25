spinup_dir=grep -R --exclude_dir={'zx', 'ab'} /b
echo "::set-output name=matrix::(ls b | jq --raw-input --slurp)"
