

# Serializer


# Proxy object
    Every single Proxy object will have its own socket connection to the daemon.
    You can share Proxy objects among threads, it will re-use the same socket connection.
    Usually every connection in the daemon has its own processing thread there, but for more details see the Servers: hosting Pyro objects chapter.
    The connection will remain active for the lifetime of the proxy object. Hence, consider cleaning up a proxy object explicitly if you know you won’t be using it again in a while. That will free up resources and socket connections. You can do this in two ways:
    calling _pyroRelease() on the proxy.
    using the proxy as a context manager in a with statement. This is the preffered way of creating and using Pyro proxies. This ensures that when you’re done with it, or an error occurs (inside the with-block), the connection is released:
    with Pyro4.Proxy(".....") as obj:
      obj.method()
    Note: you can still use the proxy object when it is disconnected: Pyro will reconnect it as soon as it’s needed again.
    At proxy creation, no actual connection is made. The proxy is only actually connected at first use, or when you manually connect it using the _pyroReconnect() or _pyroBind() methods.

# Timeout
    You can choose to configure a timeout however. This can be done globally (for all Pyro network related operations) by setting the timeout config item
    You can also do this on a per-proxy basis by setting the timeout property on the proxy
    
# Server
    In its most basic form, you create one or more classes that you want to publish as Pyro objects, you create a daemon, register the class(es) with the daemon, and then enter the daemon’s request loop
    Once a client connects, Pyro will create an instance of the class and use that single object to handle the remote method calls during one client proxy session. The object is removed once the client disconnects. Another client will cause another instance to be created for its session. 
    with Pyro4.Daemon() as daemon:
        daemon.register(...)
        daemon.requestLoop()
    
    
