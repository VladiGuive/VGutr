from monitors.endpoints import Endpoint 
from monitors.servers import Server 
from pathlib import Path
import tomllib

def load_toml() -> list:
    monitors: list = []
    integrations: list = []
    
    for path in Path('.').rglob('*.toml'):
        with open (path, 'rb') as f:
            m, i = parse_toml(tomllib.load(f))
        monitors.extend(m)
        integrations.extend(i)
    return [monitors, integrations]

def parse_toml(data: dict) -> list:
    monitors: list = []
    integrations: list = []

    if 'active' not in data or not data['active']:
        return [[],[]]
    if 'monitor' in data:
        monitors.extend(parse_monitors(data['monitor']))
    #if 'integration' in data:
    #    objects.append(parse_integrations(data['integration']))
    return [monitors, integrations]


def parse_monitors(data: dict) -> list:
    monitors: list = []
    conf: dict = {}
    for key, value in data.items():
        if type(value) is not dict:
            conf[key] = value
        if key == 'endpoints':
            monitors.extend(parse_endpoints(value, conf))
        if key == 'servers':
            monitors.extend(parse_servers(value, conf))
    return monitors

def parse_endpoints(data: dict, conf: dict) -> list:
    config: dict = conf.copy()
    endpoints: list = []
    for key, value in data.items():
        if type(value) is not dict:
            config[key] = value
        else:
            endpoint_data: dict = config.copy()
            endpoint_data.update(value)
            if 'name' not in endpoint_data:
                endpoints.append(Endpoint(name = key, **endpoint_data))
            else:
                endpoints.append(Endpoint(**endpoint_data))
            endpoint_data.clear()
    return endpoints

def parse_servers(data: dict, conf: dict) -> list:
    config: dict = conf.copy()
    servers: list = []
    for key, value in data.items():
        if type(value) is not dict:
            config[key] = value
        else:
            server_data: dict = config.copy()
            server_data.update(value)
            if 'name' not in server_data:
                servers.append(Server(name = key, **server_data))
            else:
                servers.append(Server(**server_data))
            server_data.clear()
    return servers
