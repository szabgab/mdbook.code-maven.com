# Syntax highlighting

The syntax-highlighting uses [highlight.js](https://highlightjs.org/)

It support a limited set of languages.

In order to have your code highlightted properly mark the code snippet with the name of the language. In the following snippet we marked it as `rust`

    ```rust
    let name = "Rust";
    ```

It will look like this:

```rust
let name = "Rust";
```


If the language you need is not in the [list of supported languages](https://rust-lang.github.io/mdBook/format/theme/syntax-highlighting.html#supported-languages) you can download and use a version of highlightjs that supports that language.

* Go to https://highlightjs.org/
* Check the languages for which you'd like to have support in your book.
* Click on download
* Wait for some 10 seconds till the download starts and satve the `highlight.zip` file
* `unizp` it in some empty folder.
* Move the `highlight.min.js` file to `src/highlight.js` in your book.
* Make sure you mark your code snippets with the proper language.

