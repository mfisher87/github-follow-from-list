#!/usr/bin/env python
import os
import sys

from github import Github, Auth


def follower_write_token() -> str:
    token_envvar = "GITHUB_FOLLOWER_WRITE_TOKEN"
    try:
        return os.environ[token_envvar]
    except KeyError:
        raise RuntimeError(
            f"Environment variable {token_envvar} must be populated with a"
            " GitHub fine-grained personal access token with write access to"
            " 'Followers'." 
        )


def users_to_follow(filename: str) -> list[str]:
    with open(filename) as f:
        return f.read().splitlines()


def follow_user(username: str, *, client: Github) -> None:
    """Follow a user.

    Theoretically, this would require only one query:

        PUT /user/following/{username_to_follow}

    Is there a way to do this with one query with PyGitHub? ¯\_(ツ)_/¯
    """
    # TODO: Is this a query? Is it necessary?
    self = client.get_user()
    # TODO: This query was added because `add_to_following` requires a NamedUser to
    # be passed in. This was the only documented way I could see to initialize one; is
    # it possible to make one without a query?
    to_follow = client.get_user(username)
    self.add_to_following(to_follow)


def follow_users(users: list[str], *, client: Github) -> None:
    for username in users:
        try:
            follow_user(username, client=client)
            print(f"Followed {username}")
        except Exception as e:
            print(f"ERROR: Following {username} failed with: {e}")


def main() -> None:
    token = follower_write_token()
    to_follow = users_to_follow(sys.argv[1])

    client = Github(auth=Auth.Token(token))
    follow_users(to_follow, client=client)


if __name__ == "__main__":
    main()
