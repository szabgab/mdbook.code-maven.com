# Alerts

This preprocessor adds [GitHub Flavored Markdown's Alerts](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#alerts)
(similar to [Obsidian's Callouts](https://help.obsidian.md/callouts)) to the syntax.

Source code of the [mdbook-alerts](https://github.com/lambdalisue/rs-mdbook-alerts) preprocessor.

## Install

Download from [releases](https://github.com/lambdalisue/rs-mdbook-alerts/releases) or install manuall by running `cargo install mdbook-alerts`

## Configuration

Add the following to `book.toml`:

```
[preprocessor.alerts]
```

## Usage

Include lines similar to these:

```
 > [!NOTE]
 > Useful information that users should know, even when skimming content.

 > [!TIP]
 > Helpful advice for doing things better or more easily.

 > [!IMPORTANT]
 > Key information users need to know to achieve their goal.

 > [!WARNING]
 > Urgent info that needs immediate user attention to avoid problems.

 > [!CAUTION]
 > Advises about risks or negative outcomes of certain actions.
```

## Result

You will see this in your book:

> [!NOTE]
> Useful information that users should know, even when skimming content.

> [!TIP]
> Helpful advice for doing things better or more easily.

> [!IMPORTANT]
> Key information users need to know to achieve their goal.

> [!WARNING]
> Urgent info that needs immediate user attention to avoid problems.

> [!CAUTION]
> Advises about risks or negative outcomes of certain actions.

