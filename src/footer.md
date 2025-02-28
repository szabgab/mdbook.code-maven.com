# Footer

In order to add a footer to every page you can use the [Embedify preprocessor](./embedify.md). You need to enable the footer and add the footer text - that can be using Markdown -
to the `book.toml` [configuration file](./configuration.md).


```toml
[preprocessor.embedify]
footer.enable = true
footer.message = "Copyright © 2025 • Created with ❤️  by [Gábor Szabó](https://szabgab.com/)"
```


