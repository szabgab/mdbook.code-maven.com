# Generating pdf file

I found the [mdbook-pdf](https://crates.io/crates/mdbook-pdf)

Installed it using `cargo install mdbook-pdf`.
Added the following line to `book.toml`

```
[output.pdf]
```

Then found out that it needs the `print.html` file which will not be created as we set the output.html.print to false.

Once I enabled the creation of the `print.html` file the pdf file was also generated.

TBD: How to create the pdf file without the prining icon? (I don't mind if the `print.html` is generated, but I don't want the icon.

TBD: pdf with pandoc?


