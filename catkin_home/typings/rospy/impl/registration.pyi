"""
This type stub file was generated by pyright.
"""

"""Internal use: handles maintaining registrations with master via internal listener APIs"""
_topic_manager = None
def set_topic_manager(tm):
    ...

def get_topic_manager():
    ...

_service_manager = None
def set_service_manager(sm):
    ...

def get_service_manager():
    ...

class Registration(object):
    """Registration types"""
    PUB = ...
    SUB = ...
    SRV = ...


class RegistrationListener(object):
    """Listener API for subscribing to changes in Publisher/Subscriber/Service declarations"""
    def reg_added(self, resolved_name, data_type_or_uri, reg_type):
        """
        New pub/sub/service declared.
        @param resolved_name: resolved topic/service name
        @param data_type_or_uri: topic type or service uri
        @type  data_type_or_uri: str
        @param reg_type: Valid values are L{Registration.PUB}, L{Registration.SUB}, L{Registration.SRV}
        @type  reg_type: str
        """
        ...
    
    def reg_removed(self, resolved_name, data_type_or_uri, reg_type):
        """
        New pub/sub/service removed.
        @param resolved_name: topic/service name
        @type  resolved_name: str
        @param data_type_or_uri: topic type or service uri
        @type  data_type_or_uri: str
        @param reg_type: Valid values are L{Registration.PUB}, L{Registration.SUB}, L{Registration.SRV}
        @type  reg_type: str
        """
        ...
    


class RegistrationListeners(object):
    def __init__(self) -> None:
        """
        ctor.
        """
        ...
    
    def add_listener(self, l):
        """
        Subscribe to notifications of pub/sub/service registration
        changes. This is an internal API used to notify higher level
        routines when to communicate with the master.
        @param l: listener to subscribe
        @type  l: TopicListener
        """
        ...
    
    def notify_removed(self, resolved_name, data_type_or_uri, reg_type):
        """
        @param resolved_name: resolved_topic/service name
        @type  resolved_name: str
        @param data_type_or_uri: topic type or service uri
        @type  data_type_or_uri: str
        @param reg_type: Valid values are L{Registration.PUB}, L{Registration.SUB}, L{Registration.SRV}
        @type  reg_type: str
        """
        ...
    
    def notify_added(self, resolved_name, data_type, reg_type):
        """
        @param resolved_name: topic/service name
        @type  resolved_name: str
        @param data_type: topic/service type
        @type  data_type: str
        @param reg_type: Valid values are L{Registration.PUB}, L{Registration.SUB}, L{Registration.SRV}
        @type  reg_type: str
        """
        ...
    
    def clear(self):
        """
        Remove all registration listeners
        """
        ...
    


_registration_listeners = RegistrationListeners()
def get_registration_listeners():
    ...

class RegManager(RegistrationListener):
    """
    Registration manager used by Node implemenation.
    Communicates with ROS Master to maintain topic registration
    information. Also responds to publisher updates to create topic
    connections
    """
    def __init__(self, handler) -> None:
        """
        ctor.
        @param handler: node API handler
        """
        ...
    
    def start(self, uri, master_uri):
        """
        Start the RegManager. This should be passed in as an argument to a thread
        starter as the RegManager is designed to spin in its own thread
        @param uri: URI of local node
        @type  uri: str
        @param master_uri: Master URI
        @type  master_uri: str
        """
        ...
    
    def is_registered(self):
        """
        Check if Node has been registered yet.
        @return: True if registration has occurred with master
        @rtype: bool
        """
        ...
    
    def run(self):
        """
        Main RegManager thread loop.
        Periodically checks the update
        queue and generates topic connections
        """
        ...
    
    def cleanup(self, reason):
        """
        Cleans up registrations with master and releases topic and service resources
        @param reason: human-reasonable debug string
        @type  reason: str
        """
        ...
    
    def reg_removed(self, resolved_name, data_type_or_uri, reg_type):
        """
        RegistrationListener callback
        @param resolved_name: resolved name of topic or service
        @type  resolved_name: str
        @param data_type_or_uri: either the data type (for topic regs) or the service URI (for service regs).
        @type  data_type_or_uri: str
        @param reg_type: Valid values are L{Registration.PUB}, L{Registration.SUB}, L{Registration.SRV}
        @type  reg_type: str
        """
        ...
    
    def reg_added(self, resolved_name, data_type_or_uri, reg_type):
        """
        RegistrationListener callback
        @param resolved_name: resolved name of topic or service
        @type  resolved_name: str
        @param data_type_or_uri: either the data type (for topic regs) or the service URI (for service regs).
        @type  data_type_or_uri: str
        @param reg_type: Valid values are L{Registration.PUB}, L{Registration.SUB}, L{Registration.SRV}
        @type  reg_type: str
        """
        ...
    
    def publisher_update(self, resolved_name, uris):
        """
        Inform psmanager of latest publisher list for a topic.  This
        will cause L{RegManager} to create a topic connection for all new
        publishers (in a separate thread).
        @param resolved_name: resolved topic name
        @type  resolved_name: str
        @param uris: list of all publishers uris for topic
        @type  uris: [str]
        """
        ...
    


