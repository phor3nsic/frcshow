<div align="center" id="top">
<img src="assets/firebaseimage.png" alt=frcShow width=228px>
</div>

## 

`frcShow` is a simple tool to show data of project in `Firebase Remote Config`

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

Note: If you have GOOGLE_API_KEY in enviroment, not need --key argument

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