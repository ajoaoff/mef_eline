from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSSwitch, Controller, RemoteController, Node
from mininet.cli import CLI
from mininet.util import waitListening
import time, datetime
import pytest

@pytest.fixture(scope='module')
def network():
    net = Mininet(controller=Controller, switch=OVSSwitch)
    c1 = net.addController('c1', controller=RemoteController, ip='127.0.0.1', port=6653)
    c2 = net.addController('c2', controller=RemoteController, ip='127.0.0.1', port=6634)

    h111 = net.addHost('h111')
    h112 = net.addHost('h112')
    h113 = net.addHost('h113')
    h121 = net.addHost('h121')
    h122 = net.addHost('h122')
    h211 = net.addHost('h211')
    h212 = net.addHost('h212')
    h213 = net.addHost('h213')
    h311 = net.addHost('h311')
    h321 = net.addHost('h321')
    h322 = net.addHost('h322')
    h323 = net.addHost('h323')
    h411 = net.addHost('h411')
    h412 = net.addHost('h412')
    h413 = net.addHost('h413')
    h414 = net.addHost('h414')
    h421 = net.addHost('h421')
    h422 = net.addHost('h422')
    h431 = net.addHost('h431')
    h432 = net.addHost('h432')
    h433 = net.addHost('h433')
    h611 = net.addHost('h611')
    h612 = net.addHost('h612')
    h621 = net.addHost('h621')
    h622 = net.addHost('h622')
    h623 = net.addHost('h623')

    s1 = net.addSwitch('s1', protocols='OpenFlow13')
    s2 = net.addSwitch('s2', protocols='OpenFlow13')
    s3 = net.addSwitch('s3', protocols='OpenFlow13')
    s4 = net.addSwitch('s4', protocols='OpenFlow13')
    s5 = net.addSwitch('s5', protocols='OpenFlow13')
    s6 = net.addSwitch('s6', protocols='OpenFlow13')

    my_switches = [s1, s2, s3, s4, s5, s6]

    s11 = net.addSwitch('s11')
    s12 = net.addSwitch('s12')
    s21 = net.addSwitch('s21')
    s31 = net.addSwitch('s31')
    s32 = net.addSwitch('s32')
    s41 = net.addSwitch('s41')
    s42 = net.addSwitch('s42')
    s43 = net.addSwitch('s43')
    s61 = net.addSwitch('s61')
    s62 = net.addSwitch('s62')

    other_switches = [{s11: [h111, h112, h113]},
                      {s12: [h121, h122]},
                      {s21: [h211, h212, h213]},
                      {s31: [h311]},
                      {s32: [h321, h322, h323]},
                      {s41: [h411, h412, h413, h414]},
                      {s42: [h421, h422]},
                      {s43: [h431, h432, h433]},
                      {s61: [h611, h612]},
                      {s62: [h621, h622, h623]}]

    # Internal network links
    net.addLink(s1, s3)
    net.addLink(s1, s4)
    net.addLink(s1, s6)
    net.addLink(s2, s3)
    net.addLink(s2, s5)
    net.addLink(s3, s5)
    net.addLink(s4, s5)
    net.addLink(s5, s6)

    # Clients to network links
    net.addLink(s1, s11, port1=11)
    net.addLink(s1, s12, port1=12)
    net.addLink(s2, s21, port1=11)
    net.addLink(s3, s31, port1=11)
    net.addLink(s3, s32, port1=12)
    net.addLink(s4, s41, port1=11)
    net.addLink(s4, s42, port1=12)
    net.addLink(s4, s43, port1=13)
    net.addLink(s6, s61, port1=11)
    net.addLink(s6, s62, port1=12)

    # Hosts' links
    net.addLink(s11, h111, port1=11)
    net.addLink(s11, h112, port1=12)
    net.addLink(s11, h113, port1=13)
    net.addLink(s12, h121, port1=11)
    net.addLink(s12, h122, port1=12)
    net.addLink(s21, h211, port1=11)
    net.addLink(s21, h212, port1=12)
    net.addLink(s21, h213, port1=13)
    net.addLink(s31, h311, port1=11)
    net.addLink(s32, h321, port1=11)
    net.addLink(s32, h322, port1=12)
    net.addLink(s32, h323, port1=13)
    net.addLink(s41, h411, port1=11)
    net.addLink(s41, h412, port1=12)
    net.addLink(s41, h413, port1=13)
    net.addLink(s41, h414, port1=14)
    net.addLink(s42, h421, port1=11)
    net.addLink(s42, h422, port1=12)
    net.addLink(s43, h431, port1=11)
    net.addLink(s43, h432, port1=12)
    net.addLink(s43, h433, port1=13)
    net.addLink(s61, h611, port1=11)
    net.addLink(s61, h612, port1=12)
    net.addLink(s62, h621, port1=11)
    net.addLink(s62, h622, port1=12)
    net.addLink(s62, h623, port1=13)

    print(net.values())
    net.build()
    c1.start()
    c2.start()

    for switch in my_switches:
        switch.start([c1])

    for switch_host in other_switches:
        for switch, hosts in switch_host.items():
            switch.start([c2])
            port = 11
            for host in hosts:
                vlan = host.name[1:]
                switch.dpctl('add-flow', '"in_port=%s actions=mod_vlan_vid:%s,output:1"' % (port, vlan))
                switch.dpctl('add-flow', '"in_port=1,dl_vlan=%s actions=pop_vlan,output:%s"' % (vlan, port))
                port += 1

    # root NS
    # root = Node('root', inNamespace=False)
    # intf = net.addLink(root, s62).intf1
    # root.setIP('10.0.1.78/32')
    # root.cmd('route add -net 192.168.0.0/24 dev %s' % str(intf))

    i = 2
    for host in net.hosts:
        host.setIP('192.168.0.%s' % i)
        i+=1
        # host.cmd('/usr/sbin/sshd -D -o UseDNS=no -u0&')

    for host in net.hosts:
        print( '%s %s\n' % (host.name, host.IP()))

    # for host in net.hosts:
    #     waitListening(server=host, port=22, timeout=0.5)

    time.sleep(60)
    yield net
    net.stop()

def test_pings(network):
    hosts = {}
    for host in network.hosts:
        hosts[host.name] = host
    now = datetime.datetime.now()
    sec = now.second
    time.sleep(60 - sec)
    now = datetime.datetime.now()
    min = now.minute
    sec = now.second
    print('%d minutes and %d seconds' % (min, sec))

    for i in range(10):
        # Test1
        assert ping(hosts['h111'], hosts['h422'], rule_schedule(0, 4, 2), min) is True

        # Test2
        assert ping(hosts['h321'], hosts['h612'], rule_schedule(0, 2, 3), min) is True

        # Test3
        assert ping(hosts['h431'], hosts['h213'], rule_schedule(0, 4, 2), min) is True

        # Test4
        assert ping(hosts['h611'], hosts['h211'], rule_schedule(0, 45, 60), min) is True

        # Test5
        assert ping(hosts['h414'], hosts['h311'], rule_schedule(0, 1, 2), min) is True

        # Test6
        assert ping(hosts['h421'], hosts['h623'], rule_schedule(0, 8, 10), min) is True

        time.sleep(60)
        min += 1


def test_link_down(network):
    hosts = {}
    for host in network.hosts:
        hosts[host.name] = host

    switches = {}
    for switch in network.switches:
        switches[switch.name] = switch

    network.configLinkStatus('s1', 's4', 'down')
    time.sleep(1)
    now = datetime.datetime.now()
    min = now.minute
    assert ping(hosts['h111'], hosts['h422'], rule_schedule(0, 4, 2), min) is True

    network.configLinkStatus('s5', 's4', 'down')
    time.sleep(1)
    now = datetime.datetime.now()
    min = now.minute
    assert ping(hosts['h111'], hosts['h422'], rule_schedule(0, 4, 2), min) is False

    network.configLinkStatus('s1', 's4', 'up')
    time.sleep(1)
    now = datetime.datetime.now()
    min = now.minute
    assert ping(hosts['h111'], hosts['h422'], rule_schedule(0, 4, 2), min) is True


def test_link_protection_backup(network):
    hosts = {}
    for host in network.hosts:
        hosts[host.name] = host

    switches = {}
    for switch in network.switches:
        switches[switch.name] = switch

    network.configLinkStatus('s5', 's6', 'down')
    time.sleep(1)
    now = datetime.datetime.now()
    min = now.minute
    assert ping(hosts['h414'], hosts['h311'], rule_schedule(0, 1, 2), min) is True

    time.sleep(30)

    network.configLinkStatus('s5', 's2', 'down')
    time.sleep(1)
    now = datetime.datetime.now()
    min = now.minute
    assert ping(hosts['h414'], hosts['h311'], rule_schedule(0, 1, 2), min) is True

    time.sleep(30)

    network.configLinkStatus('s5', 's6', 'up')
    time.sleep(1)
    now = datetime.datetime.now()
    min = now.minute
    assert ping(hosts['h414'], hosts['h311'], rule_schedule(0, 1, 2), min) is True

    time.sleep(30)
    network.configLinkStatus('s5', 's4', 'down')
    time.sleep(1)
    now = datetime.datetime.now()
    min = now.minute
    assert ping(hosts['h414'], hosts['h311'], rule_schedule(0, 1, 2), min) is True

    time.sleep(30)
    network.configLinkStatus('s5', 's2', 'up')
    time.sleep(1)
    now = datetime.datetime.now()
    min = now.minute
    assert ping(hosts['h414'], hosts['h311'], rule_schedule(0, 1, 2), min) is True

    time.sleep(30)
    network.configLinkStatus('s6', 's1', 'down')
    time.sleep(1)
    now = datetime.datetime.now()
    min = now.minute
    assert ping(hosts['h414'], hosts['h311'], rule_schedule(0, 1, 2), min) is True

    time.sleep(30)
    network.configLinkStatus('s5', 's4', 'up')
    time.sleep(1)
    now = datetime.datetime.now()
    min = now.minute
    assert ping(hosts['h414'], hosts['h311'], rule_schedule(0, 1, 2), min) is True

    time.sleep(30)

    network.configLinkStatus('s1', 's6', 'up')
    time.sleep(1)
    now = datetime.datetime.now()
    min = now.minute
    assert ping(hosts['h414'], hosts['h311'], rule_schedule(0, 1, 2), min) is True

    time.sleep(30)


def rule_schedule(start, stop, div):
    def wrapper(min):
        if stop > start:
            return start <= min % div < stop
        else:
            return min % div < start or min % div >= stop

    return wrapper


def ping(host1, host2, rule, min):
    out = host1.cmd('ping -c 1 %s' % host2.IP())
    index = out.find('received')
    ret = out[index - 2]
    if rule(min):
        return ret == '1'
    else:
        return ret == '0'