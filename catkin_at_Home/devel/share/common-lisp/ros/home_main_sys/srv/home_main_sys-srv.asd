
(cl:in-package :asdf)

(defsystem "home_main_sys-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "home_std_srv" :depends-on ("_package_home_std_srv"))
    (:file "_package_home_std_srv" :depends-on ("_package"))
  ))