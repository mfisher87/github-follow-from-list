#!/usr/bin/env bash
#
# A simpler implementation with less dependencies.
set -uo pipefail

for user in $(cat $1); do
    curl -L \
      -X PUT \
      -H "Accept: application/vnd.github+json" \
      -H "Authorization: Bearer ${GITHUB_FOLLOWER_WRITE_TOKEN}" \
      -H "X-GitHub-Api-Version: 2022-11-28" \
      "https://api.github.com/user/following/${user}" \
      && echo "Followed: ${user}"
done
