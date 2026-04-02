# dcx

`dcx` is a minimalistic Selenium-based browser automation wrapper for running small web workflows from a simple JSON file.

The project is designed for practical automation work: open a page, interact with elements, type values, click buttons, pause execution, and keep the workflow readable without requiring a large Python codebase. It can be installed from PyPI and started via `python -m dcx`, with Firefox as the default browser and optional Chrome or remote WebDriver modes available. 

## Features

- simple JSON-based workflow format
- command-line interface
- local Firefox support by default
- optional local Chrome support
- optional remote Firefox and remote Edge execution
- interactive halt / breakpoint support
- temporary log directory with optional retention
- environment variable expansion inside workflow values
- sample workflow generation via `--gen`

## Installation

Install from PyPI:

```bash
pip install dcx
```

You can then start it with:

```bash
python -m dcx --help
```

## What a Workflow Looks Like

A workflow is defined in a file named `play.js` in your working directory.

Despite the filename, `play.js` is **JSON**, not JavaScript. The root element is an array, and each entry is a single step. Each step is itself an array:

- 1st column: XPath selector or `null`
- 2nd column: command name
- 3rd, 4th, ... column: optional command parameters

Minimal structure:

```json
[
  [],
  [],
  []
]
```

Minimal runnable example:

```json
[
  [null, "get", "https://127.0.0.1:8080/"],
  [null, "halt"]
]
```

The repository also includes a sample workflow that opens Google, waits, clicks, types into the search box, submits the query, and then halts. 

## Quick Start

Create a new empty directory for your workflow:

```bash
mkdir EXAMPLE_WORKFLOW
cd EXAMPLE_WORKFLOW
```

Generate a starter workflow:

```bash
python -m dcx --gen
```

Run it with Firefox:

```bash
python -m dcx
```

Or with Chrome:

```bash
python -m dcx --local-chrome
```

If you prefer a shorter launcher command, the documentation recommends creating a small wrapper script in your `PATH` that forwards to `python -m dcx "$@"`.

## Example Workflow

```json
[
  [null, "get", "https://example.com"],
  ["//input[@name='q']", "type", "hello world"],
  ["//form", "submit"],
  [null, "halt"]
]
```

## Common Commands

The bundled cheatsheet currently documents commands such as:

- `get` — open a URL
- `path` — open a path on the current host
- `click` — click an element
- `type` — send keys to an element
- `setvalue` — set a value through JavaScript
- `clear` — clear an input
- `sleep` — wait for a number of seconds
- `halt` — pause execution interactively
- `bash` — run a shell command
- `bash0` — run a shell command and force a zero-style result handling
- `setenv` — define environment variables during runtime
- `attribute_setenv` — copy an element attribute into an environment variable
- `sam` — speak text via macOS Samantha voice

For the full command reference, see `cheatsheet.html` or `cheatsheet.txt` in the repository.

## Browser Modes

`dcx` supports multiple execution modes:

### Local Firefox

This is the default mode:

```bash
python -m dcx
```

### Local Chrome

```bash
python -m dcx --local-chrome
```

### Remote Firefox

```bash
python -m dcx --remote-firefox
```

### Remote Edge

```bash
python -m dcx --remote-edge --no-img
```

The repository also includes helper scripts in `src/` for these modes.

## Logging

During execution, `dcx` creates a `log` directory with browser-mode-specific runtime data. According to the documentation, this directory is removed automatically by default.

To keep logs for inspection, use:

```bash
python -m dcx --log
```

## Environment Variables

`dcx` pre-fills at least these variables for expansion:

- `$PWD`
- `$HOME`

The generated workflow hint also notes that you can extend the environment through a `play.env` file.

## Helpful Options

Based on the current code and helper scripts, useful options include:

- `--gen` — generate a starter `play.js`
- `--local-chrome` — use local Chrome
- `--remote-firefox` — use remote Firefox
- `--remote-edge` — use remote Edge
- `--log` — keep the log directory
- `--headless` — run headless
- `--no-dev` — disable Firefox devtools startup behaviour
- `--pre-bash` — run a shell command before automation starts
- `--unzip-profile` — restore a browser profile from an archive

## Repository Structure

```text
manual/            documentation sources
src/
├── dcx/           Python package
├── play.js        sample workflow
├── run.sh         local default launcher
├── run_chrome.sh  local Chrome launcher
├── run_remote_edge.sh
└── run_remote_firefox.sh
cheatsheet.html    generated command reference
cheatsheet.txt     plain text command reference
BUILD.txt          short release/build notes
VERSION            package version
```

## Example Helper Scripts

The repository contains small launcher scripts such as:

```bash
#!/bin/bash
vp -m dcx "$@"
```

and browser-specific variants like:

```bash
#!/bin/bash
vp -m dcx "$@" --local-chrome
```

This makes it easy to create your own local shortcuts around the CLI.

## Who This Is For

`dcx` is a good fit when you want:

- lightweight browser automation without building a full Selenium test suite
- repeatable “playbook” style workflows
- quick XPath-driven interactions
- simple test or scraping helpers
- browser automation that can be handed to less code-heavy users

## Documentation

Additional documentation is already included in the repository:

- `manual/`
- `cheatsheet.html`
- `cheatsheet.txt`

These files describe installation, workflow structure, and the available command set.

## License

The PyPI package metadata currently lists the project as MIT licensed. If you want the GitHub repository to communicate that clearly as well, adding a `LICENSE` file to the repository would be a good idea.

Donation welcome at https://www.paypal.com/donate/?hosted_button_id=4EZE2QKKG29JE
