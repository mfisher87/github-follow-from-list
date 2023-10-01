# Follow GitHub users from a list

Want to follow a lot of people, for example from a list of community members? Use this
tool.


## Using

### Installing

Run from source:

* Clone this repo
* Install dependencies: `conda env create`


### Running

* Set `GITHUB_FOLLOWER_WRITE_TOKEN` envvar. Please use a GitHub fine-grained personal
  access token with _only_ write permission to "Followers" with a short expiration time.

* Create a newline-delimited text-file, e.g. `input.txt`, containing the GitHub
  usernames you want to follow. For example:

  ```
  mfisher87
  mattf-nsidc
  ```

* Run the program:

  ```
  python main.py input.txt
  ```


## Minimum Viable Product

* Read list of usernames from a newline-delimited text file
* Read fine-grained personal access token with "write" permissions to the "Followers"
  resource from `GITHUB_FOLLOWER_WRITE_TOKEN`.
* Send a request to GitHub API to follow each user.


## Future

I don't have plans for the future.
