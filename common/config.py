import json
from pathlib import Path


def read_config(key=None):
    with open(get_config_path(), 'r', encoding='utf8') as f_obj:
        content = f_obj.read()
        if content != '':
            config = json.loads(content)
        else:
            config = {}
    if key is None:
        return config
    return config.get(key, None)



def write_config(key, value):
    config = read_config()
    config[key] = value
    with open(get_config_path(), 'w', encoding='utf8') as f_obj:
        f_obj.write(json.dumps(config))


def get_config_path():
    home = Path.home()
    config_path = Path.joinpath(home, '.memos.json')
    config_path.touch(exist_ok=True)
    return config_path
