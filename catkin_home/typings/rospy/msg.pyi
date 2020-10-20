"""
This type stub file was generated by pyright.
"""

import genpy

"""Internal use: Support for ROS messages, including network serialization routines"""
class AnyMsg(genpy.Message):
    """
    Message class to use for subscribing to any topic regardless
    of type. Incoming messages are not deserialized. Instead, the raw
    serialized data can be accssed via the buff property.

    This class is meant to be used by advanced users only.
    """
    _md5sum = ...
    _type = ...
    _has_header = ...
    _full_text = ...
    __slots__ = ...
    def __init__(self, *args) -> None:
        """
        Constructor. Does not accept any arguments.
        """
        ...
    
    def serialize(self, buff):
        """AnyMsg provides an implementation so that a node can forward messages w/o (de)serialization"""
        ...
    
    def deserialize(self, str):
        """Copies raw buffer into self._buff"""
        ...
    


def args_kwds_to_message(data_class, args, kwds):
    """
    Given a data class, take in the args and kwds of a function call and return the appropriate
    data_class instance.

    If kwds are specified, a new data_class instance will be created with keyword-style init.

    If there is only a single arg and it is of the correct type, it
    will be returned. AnyMsg is considered to match all data_class
    types.

    Otherwise, args will be used as args for a new message instance.

    @param data_class: Message class that will be used to instantiate new instances, if necessary.
    @type  data_class: Message class
    @param args: function args
    @type  args: sequence
    @param kwds: function kwds
    @type  kwds: dict
    @raise TypeError: if args and kwds are both specified
    """
    ...

def serialize_message(b, seq, msg):
    """
    Serialize the message to the buffer 
    @param b: buffer to write to. WARNING: buffer will be reset after call
    @type  b: StringIO
    @param msg: message to write
    @type  msg: Message
    @param seq: current sequence number (for headers)
    @type  seq: int: current sequence number (for headers)
    @raise ROSSerializationException: if unable to serialize
    message. This is usually due to a type error with one of the
    fields.
    """
    ...

def deserialize_messages(b, msg_queue, data_class, queue_size=..., max_msgs=..., start=...):
    """
    Read all messages off the buffer 
        
    @param b: buffer to read data from
    @type  b: StringIO
    @param msg_queue: queue to append deserialized data to
    @type  msg_queue: list
    @param data_class: message deserialization class
    @type  data_class: Message class
    @param queue_size: message queue size. all but the last 
    queue_size messages are discarded if this parameter is specified.
    @type  queue_size: int
    @param start: starting position to read in b
    @type  start: int
    @param max_msgs int: maximum number of messages to deserialize or None
    @type  max_msgs: int
    @raise genpy.DeserializationError: if an error/exception occurs during deserialization
    """
    ...
