<div align="center" id="top">
<img src="https://lh3.googleusercontent.com/gg/AIJ2gl_V8_3PVx8CuJOBw_ScHJ2P3YFBe6ZvN-vOt2phtXKdUAagmT-qcux8MC7EZkpmIUOX7tLCdsuxcZDJGIZx6-OK1eI5_fg713wcC6b3MtLCNEmZvVD4cUWbTqjPK0Q9mcReLaluIiNokW2XvgE4ZS0fctLumBI2vSYEx7_qagMw92hQOAYh=s1024-rj-mp2" alt=frcShow width=228px>
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