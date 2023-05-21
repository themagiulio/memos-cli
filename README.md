# Memos CLI

*To use this cli, you must have a self-hosted [✍️memos](https://github.com/usememos/memos) server set up and running.*

## About

Memos CLI is a third-party client for [✍️memos](https://github.com/usememos/memos) and both projects aren't affiliated with each other.

## Installation

Install from pip:

```
$ pip install memos-cli 
```

## Usage

1. Sign in your account

    ```
    $ memos auth signin
    ````
2. List your memos

    ```
    $ memos list
    ```
3. Create a new memo

    ```
    $ memos new
    ```

Run `memos --help` to see all available commands.

## Configuration

All configs are stored in `$HOME/.memos.json`.

- `text-editor`: the text editor used to visualize and edit memos. If it is not specified `vi` will be used.

## License

This project is made available under the GNU General Public License v3.
