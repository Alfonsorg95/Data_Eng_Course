import yaml


__config = None


def config(folder = ''):
    
    global __config
    if not __config:
        with open('{}config.yaml'.format(folder), mode = 'r') as f:
            __config = yaml.safe_load(f)
    
    return __config