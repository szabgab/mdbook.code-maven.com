# Embedding YouTube videos


We can use the [Embedify](./embedify.md) preprocessor to embed YouTube videos.

We need to install Emebdify, add the following line to the `book.toml` file

```toml
[preprocessor.embedify]
```

and then we can embed youtube videos in the pages by adding a line where you'd include the ID of the YouTube video.

<!-- embed ignore begin -->
```
{% embed youtube id="YOUTUBE-ID" %}
```
<!-- embed ignore end -->


See and example here:

{% embed youtube id="x3vF9YiWBMQ" %}
