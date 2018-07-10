# mex-ws-bot

BitMEX Websocket Bot using [Python Adapter for BitMEX Realtime Data](https://github.com/BitMEX/api-connectors/tree/master/official-ws/python)

## venv

See: https://docs.python.org/ja/3/library/venv.html

```sh
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install -U pip
$ pip -V
pip 10.0.1 from camp.hena/mex-ws-bot/.local/lib/python3.6/site-packages/pip (python 3.6)
```

## install packages

```sh
pip install -r requirements.txt
```

## setup config

Copy and edit `config/config.ini`

```sh
cp -p config/config_default.ini config/config.ini
```

## run

```sh
python main.py
```