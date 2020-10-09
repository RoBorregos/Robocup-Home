"""
This type stub file was generated by pyright.
"""

import sys
import logging
from rospy.service import _Service
from rospy.impl.tcpros_base import TCPROSTransportProtocol

"""Internal use: Service-specific extensions for TCPROS support"""
if sys.hexversion > 50331648:
    def isstring(s):
        ...
    
else:
    def isstring(s):
        ...
    
logger = logging.getLogger('rospy.service')
def wait_for_service(service, timeout=...):
    """
    Blocks until service is available. Use this in
    initialization code if your program depends on a
    service already running.
    @param service: name of service
    @type  service: str
    @param timeout: timeout time in seconds or Duration, None for no
    timeout. NOTE: timeout=0 is invalid as wait_for_service actually
    contacts the service, so non-blocking behavior is not
    possible. For timeout=0 uses cases, just call the service without
    waiting.
    @type  timeout: double|rospy.Duration
    @note  roscpp waitForService() has timeout specified in millisecs.
    @raise ROSException: if specified timeout is exceeded
    @raise ROSInterruptException: if shutdown interrupts wait
    """
    ...

def convert_return_to_response(response, response_class):
    """
    Convert return value of function to response instance. The
    rules/precedence for this are:

    1. If the return type is the same as the response type, no conversion
    is done.

    2. If the return type is a dictionary, it is used as a keyword-style
    initialization for a new response instance.

    3. If the return type is *not* a list type, it is passed in as a single arg
    to a new response instance.

    4. If the return type is a list/tuple type, it is used as a args-style
    initialization for a new response instance.
    """
    ...

def service_connection_handler(sock, client_addr, header):
    """
    Process incoming service connection. For use with
    TCPROSServer. Reads in service name from handshake and creates the
    appropriate service handler for the connection.
    @param sock: socket connection
    @type  sock: socket
    @param client_addr: client address
    @type  client_addr: (str, int)
    @param header: key/value pairs from handshake header
    @type  header: dict
    @return: error string or None 
    @rtype: str
    """
    ...

class TCPService(TCPROSTransportProtocol):
    """
    Protocol implementation for Services over TCPROS
    """
    def __init__(self, resolved_name, service_class, buff_size=...) -> None:
        """
        ctor.
        @param resolved_name: name of service
        @type  resolved_name: str
        @param service_class: Service data type class
        @type  service_class: Service
        @param buff_size int: size of buffer (bytes) to use for reading incoming requests.
        @type  buff_size: int
        """
        ...
    
    def get_header_fields(self):
        """
        Protocol API
        @return: header fields
        @rtype: dict
        """
        ...
    


class TCPROSServiceClient(TCPROSTransportProtocol):
    """Protocol Implementation for Service clients over TCPROS"""
    def __init__(self, resolved_name, service_class, headers=..., buff_size=...) -> None:
        """
        ctor.
        @param resolved_name: resolved service name 
        @type  resolved_name: str
        @param service_class: Service data type class
        @type  service_class: Service
        @param headers: identifier for Service session
        @type  headers: dict
        @param buff_size: size of buffer (bytes) for reading responses from Service. 
        @type  buff_size: int
        """
        ...
    
    def get_header_fields(self):
        """
        TCPROSTransportProtocol API        
        """
        ...
    
    def read_messages(self, b, msg_queue, sock):
        """
        In service implementation, reads in OK byte that preceeds each
        response. The OK byte allows for the passing of error messages
        instead of a response message
        @param b: buffer
        @type  b: StringIO
        @param msg_queue: Message queue to append to
        @type  msg_queue: [Message]
        @param sock: socket to read from
        @type  sock: socket.socket
        """
        ...
    


class ServiceProxy(_Service):
    """
    Create a handle to a ROS service for invoking calls.

    Usage::
      add_two_ints = ServiceProxy('add_two_ints', AddTwoInts)
      resp = add_two_ints(1, 2)
    """
    def __init__(self, name, service_class, persistent=..., headers=...) -> None:
        """
        ctor.
        @param name: name of service to call
        @type  name: str
        @param service_class: auto-generated service class
        @type  service_class: Service class
        @param persistent: (optional) if True, proxy maintains a persistent
        connection to service. While this results in better call
        performance, persistent connections are discouraged as they are
        less resistent to network issues and service restarts.
        @type  persistent: bool
        @param headers: (optional) arbitrary headers 
        @type  headers: dict
        """
        ...
    
    def wait_for_service(self, timeout=...):
        ...
    
    def __call__(self, *args, **kwds):
        """
        Callable-style version of the service API. This accepts either a request message instance,
        or you can call directly with arguments to create a new request instance. e.g.::
        
          add_two_ints(AddTwoIntsRequest(1, 2))
          add_two_ints(1, 2)
          add_two_ints(a=1, b=2)          
        
        @param args: arguments to remote service
        @param kwds: message keyword arguments
        @raise ROSSerializationException: If unable to serialize
        message. This is usually a type error with one of the fields.
        """
        ...
    
    def call(self, *args, **kwds):
        """
        Call the service. This accepts either a request message instance,
        or you can call directly with arguments to create a new request instance. e.g.::
        
          add_two_ints(AddTwoIntsRequest(1, 2))
          add_two_ints(1, 2)
          add_two_ints(a=1, b=2)          
        
        @raise TypeError: if request is not of the valid type (Message)
        @raise ServiceException: if communication with remote service fails
        @raise ROSInterruptException: if node shutdown (e.g. ctrl-C) interrupts service call
        @raise ROSSerializationException: If unable to serialize
        message. This is usually a type error with one of the fields.
        """
        ...
    
    def close(self):
        """Close this ServiceProxy. This only has an effect on persistent ServiceProxy instances."""
        ...
    


class ServiceImpl(_Service):
    """
    Implementation of ROS Service. This intermediary class allows for more configuration of behavior than the Service class.
    """
    def __init__(self, name, service_class, handler, buff_size=..., error_handler=...) -> None:
        ...
    
    def error_handler(self, e, exc_type, exc_value, tb):
        ...
    
    def shutdown(self, reason=...):
        """
        Stop this service
        @param reason: human-readable shutdown reason
        @type  reason: str
        """
        ...
    
    def spin(self):
        """
        Let service run and take over thread until service or node
        shutdown. Use this method to keep your scripts from exiting
        execution.
        """
        ...
    
    def handle(self, transport, header):
        """
        Process incoming request. This method should be run in its
        own thread. If header['persistent'] is set to 1, method will
        block until connection is broken.
        @param transport: transport instance
        @type  transport: L{TCPROSTransport}
        @param header: headers from client
        @type  header: dict
        """
        ...
    


class Service(ServiceImpl):
    """
    Declare a ROS service. Service requests are passed to the
    specified handler. 

    Service Usage::
      s = Service('getmapservice', GetMap, get_map_handler)
    """
    def __init__(self, name, service_class, handler, buff_size=..., error_handler=...) -> None:
        """
        ctor.

        @param name: service name, ``str``
        @param service_class: Service definition class
        
        @param handler: callback function for processing service
        request. Function takes in a ServiceRequest and returns a
        ServiceResponse of the appropriate type. Function may also
        return a list, tuple, or dictionary with arguments to initialize
        a ServiceResponse instance of the correct type.

        If handler cannot process request, it may either return None,
        to indicate failure, or it may raise a rospy.ServiceException
        to send a specific error message to the client. Returning None
        is always considered a failure.
        
        @type  handler: fn(req)->resp

        @param buff_size: size of buffer for reading incoming requests. Should be at least size of request message
        @type  buff_size: int

        @param error_handler: callback function for handling errors
        raised in the service code.
        @type  error_handler: fn(exception, exception_type, exception_value, traceback)->None
        """
        ...
    


