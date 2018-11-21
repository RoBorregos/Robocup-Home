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
      this.textCommand = null;
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
      if (initObj.hasOwnProperty('textCommand')) {
        this.textCommand = initObj.textCommand
      }
      else {
        this.textCommand = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type home_std_srvRequest
    // Serialize message field [debugMode]
    bufferOffset = _serializer.int8(obj.debugMode, buffer, bufferOffset);
    // Serialize message field [newFaceName]
    bufferOffset = _serializer.string(obj.newFaceName, buffer, bufferOffset);
    // Serialize message field [textCommand]
    bufferOffset = _serializer.string(obj.textCommand, buffer, bufferOffset);
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
    // Deserialize message field [textCommand]
    data.textCommand = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.newFaceName.length;
    length += object.textCommand.length;
    return length + 9;
  }

  static datatype() {
    // Returns string type for a service object
    return 'home_main_sys/home_std_srvRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'a6f1b0d3644656a0ddd1371d8aef44d8';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int8 debugMode
    string newFaceName
    string textCommand
    
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

    if (msg.textCommand !== undefined) {
      resolved.textCommand = msg.textCommand;
    }
    else {
      resolved.textCommand = ''
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
      this.actionID = null;
      this.textFromAudio = null;
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
      if (initObj.hasOwnProperty('actionID')) {
        this.actionID = initObj.actionID
      }
      else {
        this.actionID = 0;
      }
      if (initObj.hasOwnProperty('textFromAudio')) {
        this.textFromAudio = initObj.textFromAudio
      }
      else {
        this.textFromAudio = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type home_std_srvResponse
    // Serialize message field [success]
    bufferOffset = _serializer.int8(obj.success, buffer, bufferOffset);
    // Serialize message field [facesDetected]
    bufferOffset = _arraySerializer.string(obj.facesDetected, buffer, bufferOffset, null);
    // Serialize message field [actionID]
    bufferOffset = _serializer.int8(obj.actionID, buffer, bufferOffset);
    // Serialize message field [textFromAudio]
    bufferOffset = _serializer.string(obj.textFromAudio, buffer, bufferOffset);
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
    // Deserialize message field [actionID]
    data.actionID = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [textFromAudio]
    data.textFromAudio = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    object.facesDetected.forEach((val) => {
      length += 4 + val.length;
    });
    length += object.textFromAudio.length;
    return length + 10;
  }

  static datatype() {
    // Returns string type for a service object
    return 'home_main_sys/home_std_srvResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'b1e285d5f37d939954167facbe11a055';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int8 success
    string[] facesDetected
    int8 actionID
    string textFromAudio
    
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

    if (msg.actionID !== undefined) {
      resolved.actionID = msg.actionID;
    }
    else {
      resolved.actionID = 0
    }

    if (msg.textFromAudio !== undefined) {
      resolved.textFromAudio = msg.textFromAudio;
    }
    else {
      resolved.textFromAudio = ''
    }

    return resolved;
    }
};

module.exports = {
  Request: home_std_srvRequest,
  Response: home_std_srvResponse,
  md5sum() { return '0ab834d75b4e6c933d600484c31b505e'; },
  datatype() { return 'home_main_sys/home_std_srv'; }
};
