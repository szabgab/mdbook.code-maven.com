# Print and remove the print icon


By default there is a printer icon on the menu. Clicking it will create a virtual file called `print.html` and will open the printer menu of your browser. Because it uses this vritual page called `print.html`
mdBook reserved that page. Meaning you cannot have a file called `print.md` in your book.

In some cases you might want to disable the print functionality. You can remove the printer icon from the menu by adding the following lines to `book.toml`:

```toml
[output.html.print]
enable = false
```

