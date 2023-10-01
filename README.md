# Follow GitHub users from a list

Want to follow a lot of people, for example from a list of community members? Use this
tool.


## Using

> :warning: Just use the bash script.
>
> It's more efficient, doesn't require installing dependencies, etc.
>
> ```
> ./same_thing_but_in_bash.sh input.txt
> ```
>
> The Python script was for playing around. If you must use the Python script, read on.


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

- [x] Read list of usernames from a newline-delimited text file
- [x] Read fine-grained personal access token with "write" permissions to the "Followers"
  resource from `GITHUB_FOLLOWER_WRITE_TOKEN`.
- [x] Send a request to GitHub API to follow each user.


## Future

I don't have plans for the future.
