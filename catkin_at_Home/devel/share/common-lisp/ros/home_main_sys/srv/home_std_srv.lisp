; Auto-generated. Do not edit!


(cl:in-package home_main_sys-srv)


;//! \htmlinclude home_std_srv-request.msg.html

(cl:defclass <home_std_srv-request> (roslisp-msg-protocol:ros-message)
  ((debugMode
    :reader debugMode
    :initarg :debugMode
    :type cl:fixnum
    :initform 0)
   (newFaceName
    :reader newFaceName
    :initarg :newFaceName
    :type cl:string
    :initform ""))
)

(cl:defclass home_std_srv-request (<home_std_srv-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <home_std_srv-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'home_std_srv-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name home_main_sys-srv:<home_std_srv-request> is deprecated: use home_main_sys-srv:home_std_srv-request instead.")))

(cl:ensure-generic-function 'debugMode-val :lambda-list '(m))
(cl:defmethod debugMode-val ((m <home_std_srv-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader home_main_sys-srv:debugMode-val is deprecated.  Use home_main_sys-srv:debugMode instead.")
  (debugMode m))

(cl:ensure-generic-function 'newFaceName-val :lambda-list '(m))
(cl:defmethod newFaceName-val ((m <home_std_srv-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader home_main_sys-srv:newFaceName-val is deprecated.  Use home_main_sys-srv:newFaceName instead.")
  (newFaceName m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <home_std_srv-request>) ostream)
  "Serializes a message object of type '<home_std_srv-request>"
  (cl:let* ((signed (cl:slot-value msg 'debugMode)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'newFaceName))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'newFaceName))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <home_std_srv-request>) istream)
  "Deserializes a message object of type '<home_std_srv-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'debugMode) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'newFaceName) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'newFaceName) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<home_std_srv-request>)))
  "Returns string type for a service object of type '<home_std_srv-request>"
  "home_main_sys/home_std_srvRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'home_std_srv-request)))
  "Returns string type for a service object of type 'home_std_srv-request"
  "home_main_sys/home_std_srvRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<home_std_srv-request>)))
  "Returns md5sum for a message object of type '<home_std_srv-request>"
  "89dc66184617246b047b25d24799087a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'home_std_srv-request)))
  "Returns md5sum for a message object of type 'home_std_srv-request"
  "89dc66184617246b047b25d24799087a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<home_std_srv-request>)))
  "Returns full string definition for message of type '<home_std_srv-request>"
  (cl:format cl:nil "int8 debugMode~%string newFaceName~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'home_std_srv-request)))
  "Returns full string definition for message of type 'home_std_srv-request"
  (cl:format cl:nil "int8 debugMode~%string newFaceName~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <home_std_srv-request>))
  (cl:+ 0
     1
     4 (cl:length (cl:slot-value msg 'newFaceName))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <home_std_srv-request>))
  "Converts a ROS message object to a list"
  (cl:list 'home_std_srv-request
    (cl:cons ':debugMode (debugMode msg))
    (cl:cons ':newFaceName (newFaceName msg))
))
;//! \htmlinclude home_std_srv-response.msg.html

(cl:defclass <home_std_srv-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:fixnum
    :initform 0)
   (facesDetected
    :reader facesDetected
    :initarg :facesDetected
    :type (cl:vector cl:string)
   :initform (cl:make-array 0 :element-type 'cl:string :initial-element "")))
)

(cl:defclass home_std_srv-response (<home_std_srv-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <home_std_srv-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'home_std_srv-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name home_main_sys-srv:<home_std_srv-response> is deprecated: use home_main_sys-srv:home_std_srv-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <home_std_srv-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader home_main_sys-srv:success-val is deprecated.  Use home_main_sys-srv:success instead.")
  (success m))

(cl:ensure-generic-function 'facesDetected-val :lambda-list '(m))
(cl:defmethod facesDetected-val ((m <home_std_srv-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader home_main_sys-srv:facesDetected-val is deprecated.  Use home_main_sys-srv:facesDetected instead.")
  (facesDetected m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <home_std_srv-response>) ostream)
  "Serializes a message object of type '<home_std_srv-response>"
  (cl:let* ((signed (cl:slot-value msg 'success)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'facesDetected))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((__ros_str_len (cl:length ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) ele))
   (cl:slot-value msg 'facesDetected))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <home_std_srv-response>) istream)
  "Deserializes a message object of type '<home_std_srv-response>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'success) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'facesDetected) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'facesDetected)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:aref vals i) __ros_str_idx) (cl:code-char (cl:read-byte istream))))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<home_std_srv-response>)))
  "Returns string type for a service object of type '<home_std_srv-response>"
  "home_main_sys/home_std_srvResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'home_std_srv-response)))
  "Returns string type for a service object of type 'home_std_srv-response"
  "home_main_sys/home_std_srvResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<home_std_srv-response>)))
  "Returns md5sum for a message object of type '<home_std_srv-response>"
  "89dc66184617246b047b25d24799087a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'home_std_srv-response)))
  "Returns md5sum for a message object of type 'home_std_srv-response"
  "89dc66184617246b047b25d24799087a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<home_std_srv-response>)))
  "Returns full string definition for message of type '<home_std_srv-response>"
  (cl:format cl:nil "int8 success~%string[] facesDetected~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'home_std_srv-response)))
  "Returns full string definition for message of type 'home_std_srv-response"
  (cl:format cl:nil "int8 success~%string[] facesDetected~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <home_std_srv-response>))
  (cl:+ 0
     1
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'facesDetected) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4 (cl:length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <home_std_srv-response>))
  "Converts a ROS message object to a list"
  (cl:list 'home_std_srv-response
    (cl:cons ':success (success msg))
    (cl:cons ':facesDetected (facesDetected msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'home_std_srv)))
  'home_std_srv-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'home_std_srv)))
  'home_std_srv-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'home_std_srv)))
  "Returns string type for a service object of type '<home_std_srv>"
  "home_main_sys/home_std_srv")