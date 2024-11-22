class Endpoint():
    """Endpoint is one of the basic monitor resources."""
    def __init__(self,
                 name: str = '',
                 notify: bool = True,
                 integration: str = '',
                 scan_interval: int = 60,
                 prefix: str = '',
                 force_https: bool = False,
                 auth: list = [],
                 url: str = ''):
        self.name = name
        self.notify = notify
        self.integration = integration
        self.scan_interval = scan_interval
        self.prefix = prefix
        self.force_https = force_https
        self.auth = auth
        self.url = url
