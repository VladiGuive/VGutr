class Server():
    """Server is one of the basic monitor resources."""
    def __init__(self,
                 name: str = '',
                 notify: bool = True,
                 integration: str = '',
                 scan_interval: int = 60,
                 prefix: str = '',
                 mem_threshold_alert: int = 90,
                 cpu_threshold_alert: int = 90,
                 disk_threshold_alert: int = 90,
                 use_password_authentication: bool = True,
                 host: str = '',
                 port: int = 22,
                 user: str = '',
                 password: str = '',
                 pkey: str = ''):
        self.name = name
        self.notify = notify
        self.integration = integration
        self.scan_interval = scan_interval
        self.prefix = prefix
        self.mem_threshold_alert = mem_threshold_alert
        self.cpu_threshold_alert = cpu_threshold_alert
        self.disk_threshold_alert = disk_threshold_alert
        self.use_password_authentication = use_password_authentication
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.pkey = pkey
