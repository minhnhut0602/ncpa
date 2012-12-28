import logging
import ConfigParser

class NCPADaemon(object):
    '''
    Defines the general form that listener daemons must adhere
    to. Override all of these methods.
    '''
    
    def __init__(self, config_filename, handler, *args, **kwargs):
        '''
        Always inherit this method
        '''
        self.handler = handler
        self.config_filename = config_filename
        self.parse_config()
        self.setup_logging()
    
    def parse_config(self, *args, **kwargs):
        '''
        Set the parsed config to self.config
        '''
        print type(self.config_filename)
        import sys
        sys.exit()
        self.config = ConfigParser.ConfigParser()
        self.config.read(self.config_filename)
    
    def setup_logging(self, *arg, **kwargs):
        '''
        This should always setup the logger.
        '''
        print type(self.config)
        import sys
        sys.exit()
        log_config = dict(self.config.items('logging', 1))
        log_config['level'] = getattr(logging, log_config['log_level'], logging.INFO)
        del log_config['log_level']
        logging.basicConfig(**log_config)
        self.logger = logging.getLogger()
    
    def start(self, *args, **kwargs):
        '''
        This method should start the daemon or persistent
        process.
        '''
        raise Exception("Instantiation of abstract base class.")
    
    def stop(self, *args, **kwargs):
        '''
        This should kill the daemon and shut down everything
        tidily.
        '''
        raise Exception("Instantiation of abstract base class.")