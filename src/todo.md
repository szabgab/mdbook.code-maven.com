# TODO

## Generating pdf files

## Add github icon to the menu

```
[output.html]
git-repository-url = "https://github.com/szabgab/git-he.code-maven.com"
git-repository-icon = "fa-github"
edit-url-template = "https://github.com/szabgab/git-he.code-maven.com/edit/main/{path}"
```


* [Git Maven in Hebrew](https://git-he.code-maven.com/)

* [Awesome mdbook](https://github.com/softprops/awesome-mdbook)

* [Awesome Rust mdBooks](https://github.com/smhmayboudi/awesome-rust-mdbooks)

* [Rust ebooks](https://rust-ebooks.code-maven.com/)

* Customize 404 pages

* Redirect to some other page or to an external site?


* [epub](https://crates.io/crates/mdbook-epub)
* [pdf](https://crates.io/crates/mdbook-pdf)

https://crates.io/keywords/mdbook

* Verify that every page has a title - the first line starting with a single `#`

* Eliminate the need to duplicate the page title in the md file of the page and the summary.

* Check that all the (internal) links work.

* Allow searching for special symbols. e.g. What does `?` mean in Ruby or Rust?

* How to make it easier for book readers to find the hidden keys?
    * Pressing the right and left arrows move the book to the next and the previous pages. (and it works the other way around in RTL books)
    * Pressing `s` open the search window.

* Reread the .gitignore file if it changed while `serve` is running. (e.g. if I add `*.swp` later) (same with `watch`, I guess)


`mdbook test` reports lots of errors when run on this book. Shouldn't it skip everything as there is no rust code here?

Lines starting with `##` in the summary file are ignored, Maybe they can be designated as comments? Or can we have other comments? e.g. `<!-- -->`?

* What is controlled by the `language` configuration option? Besides the direction (RTL, LTR?) and how come we can use any text there including "xyz" ?


* Update the code highlighting in the mdbook, and add detailed explanation to https://rust-lang.github.io/mdBook/format/theme/syntax-highlighting.html
on how to add a replacement highlighting.js file.

