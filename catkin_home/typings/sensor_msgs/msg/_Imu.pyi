"""
This type stub file was generated by pyright.
"""

import sys
import genpy

"""autogenerated by genpy from sensor_msgs/Imu.msg. Do not edit."""
python3 = True if sys.hexversion > 50331648 else False
class Imu(genpy.Message):
  _md5sum = ...
  _type = ...
  _has_header = ...
  _full_text = ...
  __slots__ = ...
  _slot_types = ...
  def __init__(self, *args, **kwds) -> None:
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,orientation,orientation_covariance,angular_velocity,angular_velocity_covariance,linear_acceleration,linear_acceleration_covariance

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    ...
  
  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    ...
  
  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    ...
  
  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    ...
  
  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    ...
  


_struct_I = genpy.struct_I
_struct_3I = None
_struct_3d = None
_struct_4d = None
_struct_9d = None
