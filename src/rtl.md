# Right to left languages (Hebrew, Arabic, Farsi)

Most languages are written from left to right (LTR), but if you are in the lucky situation that your language is written from Right to Left (RTL), don't worry. mdBook can work for you.

By setting the `language` or by setting the text-direction` fields in the `book` section the book will be rendered from right o left.


```
[book]
text-direction = "rtl"
language = "he"
```

If you'd like to see and example you can take a look at the [Hebrew Code Maven](https://he.code-maven.com/) or the [Persian translation](https://google.github.io/comprehensive-rust/fa/) of the [Comprehensive Rust](https://google.github.io/comprehensive-rust/)  book.


If you have a book that is written Left-to-right, but you would like to have a sort section written Right-to-Left, then you can wrap that section in the following:

```html
<div dir="rtl">

</div>
```

As you can see here:

---
<div dir="rtl">

שלום עולם!
</div>

---

On the other hand, if you have book that is primarily written in a Right-to-Left language and you'd like to insert some text that flows from left to right, eg. some code-snippet,
then you can wrap it in:

```html
<div dir="ltr">

</div>
```


