"""
This type stub file was generated by pyright.
"""

import logging

_logger = logging.getLogger('rospy.impl.statistics')
class SubscriberStatisticsLogger:
    """
    Class that monitors each subscriber.

    this class basically just keeps a collection of ConnectionStatisticsLogger.
    """
    @classmethod
    def is_enabled(cls):
        ...
    
    def __init__(self, subscriber) -> None:
        ...
    
    def read_parameters(self):
        """
        Fetch window parameters from parameter server
        """
        ...
    
    def callback(self, msg, publisher, stat_bytes):
        """
        This method is called for every message that has been received.

        @param msg: The message received.
        @param publisher: The name of the publisher node that sent the msg
        @param stat_bytes: A counter, how many bytes have been moved across
        this connection since it exists.

        This method just looks up the ConnectionStatisticsLogger for the specific connection
        between publisher and subscriber and delegates to statistics logging to that
        instance.
        """
        ...
    
    def shutdown(self):
        ...
    


class ConnectionStatisticsLogger:
    """
    Class that monitors lots of stuff for each connection.

    is created whenever a subscriber is created.
    is destroyed whenever its parent subscriber is destroyed.
    its lifecycle is therefore bound to its parent subscriber.
    """
    def __init__(self, topic, subscriber, publisher) -> None:
        """
        Constructor.

        @param topic: Name of the topic
        @param subscriber: Name of the subscriber
        @param publisher: Name of the publisher

        These three should uniquely identify the connection.
        """
        ...
    
    def sendStatistics(self, subscriber_statistics_logger):
        """
        Send out statistics. Aggregate collected stats information.

        Currently done blocking. Might be moved to own thread later. But at the moment
        any computation done here should be rather quick.
        """
        ...
    
    def callback(self, subscriber_statistics_logger, msg, stat_bytes):
        """
        This method is called for every message, that is received on this
        subscriber.

        this callback will keep some statistics and publish the results
        periodically on a topic. the publishing should probably be done
        asynchronically in another thread.

        @param msg: The message, that has been received. The message has usually
        been already deserialized. However this is not always the case. (AnyMsg)
        @param stat_bytes: A counter, how many bytes have been moved across
        this connection since it exists.

        Any computing-heavy stuff should be done somewhere else, as this
        callback has to return before the message is delivered to the user.
        """
        ...
    
    def shutdown(self):
        ...
    


