# TODO

## Improvement ideas for mdBook

* Index Hebrew text  as well https://github.com/rust-lang/mdBook/issues/2393
* Remove .html extension
* syntax highlighting: generate the highlight.js when building the book?
* Check which files are not in use?
* Avoid including the same page twice.
* Allow searching for special symbols. e.g. What does `?` mean in Ruby or Rust?
* `mdbook test` reports lots of errors when run on this book. Shouldn't it skip everything as there is no rust code here?
* Verify that every page has a title - the first line starting with a single `#`
* Allow the inclusion of front matter in yaml or toml format
* Eliminate the need to duplicate the page title in the md file of the page and the summary.
* Warn if the same file is included twice via SUMMARY.md - right now it is just accepted.
* Check that all the (internal) links work.
* Reread the .gitignore file if it changed while `serve` is running. (e.g. if I add `*.swp` later) (same with `watch`, I guess)
* What happens if SUMMARY.md is missing?
* Should we check the case of SUMMARY.md (so people on Windows won't be surprised if Summary.md works on their computer but not on Linux?


## Topics to be covered


* [Git Maven in Hebrew](https://git-he.code-maven.com/)

* [Awesome mdbook](https://github.com/softprops/awesome-mdbook)

* [Awesome Rust mdBooks](https://github.com/smhmayboudi/awesome-rust-mdbooks)

* [Rust ebooks](https://rust-ebooks.code-maven.com/)


* Redirect to some other page or to an external site?

* Generating epub files
* [epub](https://crates.io/crates/mdbook-epub)



pandoc on Ubuntu:

```
sudo apt install pandoc
```

https://crates.io/keywords/mdbook


* How to make it easier for book readers to find the hidden keys?
    * Pressing the right and left arrows move the book to the next and the previous pages. (and it works the other way around in RTL books)
    * Pressing `s` open the search window.

* Lines starting with `##` in the summary file are ignored, Maybe they can be designated as comments? Or can we have other comments? e.g. `<!-- -->`?

* What is controlled by the `language` configuration option? Besides the direction (RTL, LTR?) and how come we can use any text there including "xyz" ?

* Update the code highlighting in the mdbook, and add detailed explanation to https://rust-lang.github.io/mdBook/format/theme/syntax-highlighting.html
on how to add a replacement highlighting.js file.


### Error

given the following SUMMARY.md

```
# Summary

- [next](Home](./index)

```

I get this error

```
$ mdbook build
2025-03-02 15:11:15 [WARN] (mdbook::book::summary): Expected a start of a link, actually got Some(Text(Borrowed("[")))
2025-03-02 15:11:15 [ERROR] (mdbook::utils): Error: Summary parsing failed for file="/home/gabor/work/exercises.code-mave.com/src/SUMMARY.md"
2025-03-02 15:11:15 [ERROR] (mdbook::utils): 	Caused By: There was an error parsing the numbered chapters
2025-03-02 15:11:15 [ERROR] (mdbook::utils): 	Caused By: There was an error parsing the numbered chapters
2025-03-02 15:11:15 [ERROR] (mdbook::utils): 	Caused By: failed to parse SUMMARY.md line 3, column 3: The link items for nested chapters must only contain a hyperlink
```

I the Rust `Some(Text(Borrowed` there looks bad

command line test


* What happens if there are two separeators in the SUMMARY one after the other?

```
# One
# Two
- [Page](./page.md)
```

* Include the time the book was generated. Either in the footer or on one of the pages.
* Include a front-image.
* Document what extensions can be the files referred to in the SUMMARY.md ?  `.md` works, but if we leave out the extension that also works. If the extension is `html` then I think it is not processed etc.

* We can use `{{#include file/path }}` to include file from pathes outside of the book, but currently `serve` does not `watch` changes to those files.
    Watch files from outside the tree.
