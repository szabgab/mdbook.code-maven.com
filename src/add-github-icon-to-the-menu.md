# Add GitHub icon to the menu

On the top of this web site, on the right-hand side you can see two icons. One is a GitHub and the other is a pen.
The former will lead to the root of the repository of this book. The latter will open a link on GitHub where
the reader can edit the source of this page. If the user does not have the rights to edit the file in the default repository
then GitHub will create a fork as needed.

The following lines in the `book.toml` [configuration file](./configuration.md) control these icon and the addresses of the
GitHub repository.


```
[output.html]
git-repository-url = "https://github.com/szabgab/mdbook.code-maven.com"
git-repository-icon = "fa-github"
edit-url-template = "https://github.com/szabgab/mdbook.code-maven.com/edit/main/{path}"
```


