#!/usr/bin/python
"""
This is the most simple example to showcase Containernet.
"""
from mininet.net import Containernet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import info, setLogLevel
setLogLevel('info')

net = Containernet(controller=Controller)
info('*** Adding controller\n')
net.addController('c0')
info('*** Adding docker containers\n')
f1 = net.addDocker('f1', ip='10.0.0.251',
        dimage="my-coap-server:latest",
        ports=[5683],
        port_bindings={5683: 5683})
f2 = net.addDocker('f2', ip='10.0.0.252', dimage="mainflux/coap:latest")
info('*** Adding switches\n')
s1 = net.addSwitch('s1')
s2 = net.addSwitch('s2')
info('*** Creating links\n')
net.addLink(f1, s1)
net.addLink(s1, s2, cls=TCLink, delay='100ms', bw=1)
net.addLink(s2, f2)
info('*** Starting network\n')
net.start()
info('*** Testing connectivity\n')
net.ping([f1, f2])
info('*** Running CLI\n')
CLI(net)
info('*** Stopping network')
net.stop()
