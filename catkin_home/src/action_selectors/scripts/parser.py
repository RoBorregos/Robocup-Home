#!/usr/bin/env python
import rospy
#import requests
from action_selectors.msg import RawInput
from intercom.msg import action_selector_cmd

'''
Voz: repetir de vuelta un comando de voz con el formato "Bring [OBJETO] from [LUGAR]."
Punto Inicial: enmedio de la arena.
Calificacion Base: 5 si entiende el objeto, 5 si entiende el lugar.
Reto Adicional: entender ambos el objeto y el lugar por medio de utilizar algun esquema de Interaccion Humano-Robot donde el robot 
tiene la iniciativa de la conversacion; 2.5 puntos adicionales por la correcta comprension de ambos.

El robot comienza en el punto inicial, donde recibe el comando por voz en el formato "Bring [OBJETO] frome [LUGAR]."
Se puede utilizar otro esquema, pero no se daran puntos adicionales.
El robot navega al lugar pedido.
El robot agarra el objeto pedido.


'''
def callRASA(text):
    cmd_id = 0
    cmd_priority = 0
    critic_shutdown = 0
    args = [""]
    #make request to rasa server
    return cmd_id, cmd_priority, critic_shutdown, args


def callback(msg):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", msg.inputText)

    #open list of actions
    #call parser
    #send message to engine 
    pub = rospy.Publisher('action_selector_cmds', action_selector_cmd, queue_size=10)
    #Here the parsing is done
    cmd_id, cmd_priority, critic_shutdown, args = callRASA(msg.inputText)




    action_code = action_selector_cmd()
    action_code.cmd_id = cmd_id
    action_code.cmd_priority = cmd_priority
    action_code.critic_shutdown = critic_shutdown
    action_code.args = args
    rospy.loginfo(action_code)
    pub.publish(action_code)

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('parser', anonymous=True)

    rospy.Subscriber("RawInput", RawInput, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()