// Auto-generated. Do not edit!

// (in-package home_main_sys.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class home_std_srvRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.debugMode = null;
      this.newFaceName = null;
    }
    else {
      if (initObj.hasOwnProperty('debugMode')) {
        this.debugMode = initObj.debugMode
      }
      else {
        this.debugMode = 0;
      }
      if (initObj.hasOwnProperty('newFaceName')) {
        this.newFaceName = initObj.newFaceName
      }
      else {
        this.newFaceName = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type home_std_srvRequest
    // Serialize message field [debugMode]
    bufferOffset = _serializer.int8(obj.debugMode, buffer, bufferOffset);
    // Serialize message field [newFaceName]
    bufferOffset = _serializer.string(obj.newFaceName, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type home_std_srvRequest
    let len;
    let data = new home_std_srvRequest(null);
    // Deserialize message field [debugMode]
    data.debugMode = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [newFaceName]
    data.newFaceName = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.newFaceName.length;
    return length + 5;
  }

  static datatype() {
    // Returns string type for a service object
    return 'home_main_sys/home_std_srvRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '99f51edefd6f5685f5ece83d46d13021';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int8 debugMode
    string newFaceName
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new home_std_srvRequest(null);
    if (msg.debugMode !== undefined) {
      resolved.debugMode = msg.debugMode;
    }
    else {
      resolved.debugMode = 0
    }

    if (msg.newFaceName !== undefined) {
      resolved.newFaceName = msg.newFaceName;
    }
    else {
      resolved.newFaceName = ''
    }

    return resolved;
    }
};

class home_std_srvResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.success = null;
      this.facesDetected = null;
    }
    else {
      if (initObj.hasOwnProperty('success')) {
        this.success = initObj.success
      }
      else {
        this.success = 0;
      }
      if (initObj.hasOwnProperty('facesDetected')) {
        this.facesDetected = initObj.facesDetected
      }
      else {
        this.facesDetected = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type home_std_srvResponse
    // Serialize message field [success]
    bufferOffset = _serializer.int8(obj.success, buffer, bufferOffset);
    // Serialize message field [facesDetected]
    bufferOffset = _arraySerializer.string(obj.facesDetected, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type home_std_srvResponse
    let len;
    let data = new home_std_srvResponse(null);
    // Deserialize message field [success]
    data.success = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [facesDetected]
    data.facesDetected = _arrayDeserializer.string(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    object.facesDetected.forEach((val) => {
      length += 4 + val.length;
    });
    return length + 5;
  }

  static datatype() {
    // Returns string type for a service object
    return 'home_main_sys/home_std_srvResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c4beb2775f8d6671c83b18178053782a';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int8 success
    string[] facesDetected
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new home_std_srvResponse(null);
    if (msg.success !== undefined) {
      resolved.success = msg.success;
    }
    else {
      resolved.success = 0
    }

    if (msg.facesDetected !== undefined) {
      resolved.facesDetected = msg.facesDetected;
    }
    else {
      resolved.facesDetected = []
    }

    return resolved;
    }
};

module.exports = {
  Request: home_std_srvRequest,
  Response: home_std_srvResponse,
  md5sum() { return '89dc66184617246b047b25d24799087a'; },
  datatype() { return 'home_main_sys/home_std_srv'; }
};
