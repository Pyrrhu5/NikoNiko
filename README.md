# NikoNiko

Bot to register "daily mood" on Iluca's NikoNiko, randomly pick a mood an post it.

## Installation

Only tested on Linux.

**Python**

Python version 3.6 or above

```bash
python3 --version
```

**Clone the repository**

Git is required
```bash
git --version
```

Clone it
```bash
git clone https://aymericdeschard@bitbucket.org/aymericdeschard/nikoniko.git
```

**Virtual env**

Optional, but `Run.sh` assumes you have setup a virtual env as such:

```bash
python3 -m venv venv
```

**Dependencies**

Activate the virtual env first:
```bash
source ./venv/bin/activate
```

Install dependencies:

```bash
pip3 install -r requirements.txt
```

**Executable**

Allows execution of entry point (not needed for Windows)
```bash
chmod +x NikoNiko.py
```
or, if using the virtual env
```bash
chmod +x Run.sh
```

**Crontab**

Post it at 17:30 from Monday to Friday

```
30 17 * * 1-5 <install path>/nikoniko/Run.sh >> <where you want the logs>/nikoniko.log
```

## Update

```bash
git pull
```


## License
Unmodified [MIT license](https://opensource.org/licenses/MIT)

See `License.md`
