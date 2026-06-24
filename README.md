<div align="center" id="top">
<img src="assets/firebaseimage.png" alt=frcShow width=228px>
</div>

## 

<h4 align="center">Fetch and display a project's Firebase Remote Config data</h4>

<p align="center">
  <img alt="language" src="https://img.shields.io/github/languages/top/phor3nsic/frcshow">
  <img alt="last commit" src="https://img.shields.io/github/last-commit/phor3nsic/frcshow">
  <img alt="license" src="https://img.shields.io/github/license/phor3nsic/frcshow">
  <img alt="stars" src="https://img.shields.io/github/stars/phor3nsic/frcshow?style=social">
</p>

### About

`frcShow` is a simple command-line tool that fetches the **Firebase Remote Config**
of a project and prints it in a readable format. You provide a Firebase project ID
(or a search term, in which case it tries to resolve the project ID from the API's
error message) and a Google API key. It is useful for security research and assessing
what configuration data a Firebase project exposes.

### Install

- via pipx:

```sh
pipx install git+https://github.com/phor3nsic/frcshow
```
- via pip:

```sh
pip install git+https://github.com/phor3nsic/frcshow
```

### Usage

```sh
frcshow --project_id 923626523156 --key AIzaSyXXXXXXXXXXXXizywz_XXXXXXXXX7HlyTs
```

Note: if you have `GOOGLE_API_KEY` set in your environment, the `--key` argument is not required.

| Flag | Description | Default |
|------|-------------|---------|
| `-p`, `--project_id` | Firebase project ID or search term (e.g. `923626523156` or `weluproject`) | required |
| `-k`, `--key` | Google API key for Firebase Remote Config | `$GOOGLE_API_KEY` |
| `-h`, `--help` | Show help | — |

### Example

Try to get data of this project:

> 923626523156

```sh
frcshow --project_id 923626523156 --key YOURVALIDKEY
```

Or you can found by name:

```sh
frcshow --project_id weluproject --key YOURVALIDKEY
```

### Disclaimer

For authorized security testing and education only. You are responsible for how you use it.

### License

[MIT](LICENSE) © [phor3nsic](https://github.com/phor3nsic)