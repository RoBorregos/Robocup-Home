;; Auto-generated. Do not edit!


(when (boundp 'home_main_sys::home_std_srv)
  (if (not (find-package "HOME_MAIN_SYS"))
    (make-package "HOME_MAIN_SYS"))
  (shadow 'home_std_srv (find-package "HOME_MAIN_SYS")))
(unless (find-package "HOME_MAIN_SYS::HOME_STD_SRV")
  (make-package "HOME_MAIN_SYS::HOME_STD_SRV"))
(unless (find-package "HOME_MAIN_SYS::HOME_STD_SRVREQUEST")
  (make-package "HOME_MAIN_SYS::HOME_STD_SRVREQUEST"))
(unless (find-package "HOME_MAIN_SYS::HOME_STD_SRVRESPONSE")
  (make-package "HOME_MAIN_SYS::HOME_STD_SRVRESPONSE"))

(in-package "ROS")





(defclass home_main_sys::home_std_srvRequest
  :super ros::object
  :slots (_debugMode _newFaceName ))

(defmethod home_main_sys::home_std_srvRequest
  (:init
   (&key
    ((:debugMode __debugMode) 0)
    ((:newFaceName __newFaceName) "")
    )
   (send-super :init)
   (setq _debugMode (round __debugMode))
   (setq _newFaceName (string __newFaceName))
   self)
  (:debugMode
   (&optional __debugMode)
   (if __debugMode (setq _debugMode __debugMode)) _debugMode)
  (:newFaceName
   (&optional __newFaceName)
   (if __newFaceName (setq _newFaceName __newFaceName)) _newFaceName)
  (:serialization-length
   ()
   (+
    ;; int8 _debugMode
    1
    ;; string _newFaceName
    4 (length _newFaceName)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int8 _debugMode
       (write-byte _debugMode s)
     ;; string _newFaceName
       (write-long (length _newFaceName) s) (princ _newFaceName s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int8 _debugMode
     (setq _debugMode (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _debugMode 127) (setq _debugMode (- _debugMode 256)))
   ;; string _newFaceName
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _newFaceName (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass home_main_sys::home_std_srvResponse
  :super ros::object
  :slots (_success _facesDetected ))

(defmethod home_main_sys::home_std_srvResponse
  (:init
   (&key
    ((:success __success) 0)
    ((:facesDetected __facesDetected) (let (r) (dotimes (i 0) (push "" r)) r))
    )
   (send-super :init)
   (setq _success (round __success))
   (setq _facesDetected __facesDetected)
   self)
  (:success
   (&optional __success)
   (if __success (setq _success __success)) _success)
  (:facesDetected
   (&optional __facesDetected)
   (if __facesDetected (setq _facesDetected __facesDetected)) _facesDetected)
  (:serialization-length
   ()
   (+
    ;; int8 _success
    1
    ;; string[] _facesDetected
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _facesDetected)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int8 _success
       (write-byte _success s)
     ;; string[] _facesDetected
     (write-long (length _facesDetected) s)
     (dolist (elem _facesDetected)
       (write-long (length elem) s) (princ elem s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int8 _success
     (setq _success (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _success 127) (setq _success (- _success 256)))
   ;; string[] _facesDetected
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _facesDetected (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _facesDetected i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;;
   self)
  )

(defclass home_main_sys::home_std_srv
  :super ros::object
  :slots ())

(setf (get home_main_sys::home_std_srv :md5sum-) "89dc66184617246b047b25d24799087a")
(setf (get home_main_sys::home_std_srv :datatype-) "home_main_sys/home_std_srv")
(setf (get home_main_sys::home_std_srv :request) home_main_sys::home_std_srvRequest)
(setf (get home_main_sys::home_std_srv :response) home_main_sys::home_std_srvResponse)

(defmethod home_main_sys::home_std_srvRequest
  (:response () (instance home_main_sys::home_std_srvResponse :init)))

(setf (get home_main_sys::home_std_srvRequest :md5sum-) "89dc66184617246b047b25d24799087a")
(setf (get home_main_sys::home_std_srvRequest :datatype-) "home_main_sys/home_std_srvRequest")
(setf (get home_main_sys::home_std_srvRequest :definition-)
      "int8 debugMode
string newFaceName
---
int8 success
string[] facesDetected
")

(setf (get home_main_sys::home_std_srvResponse :md5sum-) "89dc66184617246b047b25d24799087a")
(setf (get home_main_sys::home_std_srvResponse :datatype-) "home_main_sys/home_std_srvResponse")
(setf (get home_main_sys::home_std_srvResponse :definition-)
      "int8 debugMode
string newFaceName
---
int8 success
string[] facesDetected
")



(provide :home_main_sys/home_std_srv "89dc66184617246b047b25d24799087a")


