from fabric.api import run, sudo, settings, hide, cd, env
from fabric.contrib.files import exists
from termcolor import colored

env.user = "vagrant"
env.password = "vagrant"

# In env.roledefs we define the remote servers. It can be IP Addrs or domain names.
env.roledefs = {
    'local': ['localhost'],
}

def server():
    with settings(warn_only=False):

        print colored('################################################################', 'red', attrs=['bold'])
        print colored('################################################################', 'red', attrs=['bold'])

        print colored(' _     _                    ____                           ', 'blue', attrs=['bold'])
        print colored('| |   (_)_ __  _   ___  __ / ___|  ___ _ ____   _____ _ __ ', 'blue', attrs=['bold'])
        print colored('| |   | |  _ \| | | \ \/ / \___ \ / _ \  __\ \ / / _ \  __|', 'blue', attrs=['bold'])
        print colored('| |___| | | | | |_| |>  <   ___) |  __/ |   \ V /  __/ |   ', 'blue', attrs=['bold'])
        print colored('|_____|_|_| |_|\__,_/_/\_\ |____/ \___|_|    \_/ \___|_|   ', 'blue', attrs=['bold'])

        print colored('                                                                  ', 'blue')
        print colored('                                                                  ', 'blue')

        print colored('                                          .;lk00OOOkl,.', 'cyan')
        print colored('                                        ,oOWMMMMMMMMMMMNOl', 'cyan')
        print colored('                                     .dKMMMMMMMMMMMMMMMNWMMNl.', 'cyan')
        print colored('                                    .KMMMMMMMMMMMMMMMMW .OMMMWl', 'cyan')
        print colored('                                   .KMMMMMMMMMMMMMMMMMMO0WMMMMMk', 'cyan')
        print colored('                                   :MMMMMMMMMMMMMMMMMMMMMMMMMMMMl', 'cyan')
        print colored('                                   oMMMMMMMMMMMMMMMMMMMMMMMMMMMMX.', 'cyan')
        print colored('                                   OMMMNOONMMMMMMMWkc::dXMMMMMMMMd', 'cyan')
        print colored('                                   OMM0.  .oWMMMMO.      xMMMMMMMW.', 'cyan')
        print colored('                                   OMM,lKOc dMMMM  :0KKo  0MMMMMMM ', 'cyan')
        print colored('                                   xMM,OMWW :OkkO..NMMWWl :MMMMMMO', 'cyan')
        print colored('                                   lMMkxMMMOOKKKOOdNMMMWc kMMMMMMW.', 'cyan')
        print colored('                                   lMMNoXMMWWMMMNWMMMMM0co0WMMMMMM:', 'cyan')
        print colored('                                   ;M0XMMMMMMMMMMMMMMMMXKMddMMMMMMO', 'cyan')
        print colored('                                    MOMMMMMMMMMMMMMWKO0KWMdkMMMMMMMc', 'cyan')
        print colored('                                    MKkKXKNMMMMX0K00XMMMWxoWMXclOMMW ', 'cyan')
        print colored('                                    MMK dKKKKKK0XMMMWOl,.  NMM0, KMMK.', 'cyan')
        print colored('                                   kMMk  .cOXXXXXOx:.      :NMMMMMMMMO.', 'cyan')
        print colored('                                  0MMWl                     ;WMMMMMMMMW:', 'cyan')
        print colored('                                lNMMX;                       lMMMMMMMMMWd.', 'cyan')
        print colored('                               0MMM0.                         kMMMMMMMMMMK ', 'cyan')
        print colored('                             oWMMMM                           .XMMMMMMMMMMWo', 'cyan')
        print colored('                           .OMMMMMMO:.                          NMMMMMMMMMMMK ', 'cyan')
        print colored('                          ,XMMMMMMNOo                           ;WMMMMMMMMMMMWl', 'cyan')
        print colored('                         ,NMMMMMK:                               ,NMMMMMMMMMMMMx', 'cyan')
        print colored('                        ;WMMMMMO.                                 ;WMMMMMWMMMMMMl', 'cyan')
        print colored('                       ,NMMMMMO.                                   lMMMMMKKMMMMMW:', 'cyan')
        print colored('                      :WMMMMMd                                      OMMMMMOKMMMMMW;', 'cyan')
        print colored('                     NMMMMMK                                       cMMMMMMOMMMMMMK.', 'cyan')
        print colored('                    .NMMMMMMl                                        MMMMMMOMMMMMMMo', 'cyan')
        print colored('                    OMMMMMMW.                                       .NMMMMMOMMMMMMMN.', 'cyan')
        print colored('                   ;MMMMMMMk                                         OMMMMk0MMMMMMMM.', 'cyan')
        print colored('                   lMMNXWMMk                                         KMMMNkWMMMMMMMM ', 'cyan')
        print colored('                    dddlolkd                                        .MMMMNMMMMMMMMMO', 'cyan')
        print colored('                   ;XMMMMWd...                                  .cllocoWMMMMMMMWOol.', 'cyan')
        print colored('                 .dWMMMMMMMK:ld                                OMMMMO OMMMMMMMd;0K0 ', 'cyan')
        print colored('               .cXMMMMMMMMMMWocKO:                              0MMMMK.xMMMMWklxWMMMl', 'cyan')
        print colored('         ,:oxOKNMMMMMMMMMMMMMM0:kWNx                            0MMMMMNOkkdxdOWMMMMMd', 'cyan')
        print colored('        kMMMMMMMMMMMMMMMMMMMMMMN:lWMMXl.                        OMMMMMMMMMMMMMMMMMMMWk.', 'cyan')
        print colored('        OMMMMMMMMMMMMMMMMMMMMMMMMd,KMMMK.                      .NMMMMMMMMMMMMMMMMMMMMMXl.', 'cyan')
        print colored('        oMMMMMMMMMMMMMMMMMMMMMMMMMO;0MMW.                      ,MMMMMMMMMMMMMMMMMMMMMMMMWx:.', 'cyan')
        print colored('        lMMMMMMMMMMMMMMMMMMMMMMMMMMK,lo,                     o cMMMMMMMMMMMMMMMMMMMMMMMMMMMK.', 'cyan')
        print colored('        lMMMMMMMMMMMMMMMMMMMMMMMMMMMWd.                  .:OWN.OMMMMMMMMMMMMMMMMMMMMMMMMMMMO', 'cyan')
        print colored('        OMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW:            . ckNMMMMd MMMMMMMMMMMMMMMMMMMMMMMMMKo.', 'cyan')
        print colored('       .NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW,:Okkkkkk0KNMMMMMMMMM,lMMMMMMMMMMMMMMMMMMMMMWOl.', 'cyan')
        print colored('        kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMk.KMMMMMMMMMMMMMMMMMX.dMMMMMMMMMMMMMMMMMMWk:.', 'cyan')
        print colored('          cdk0NMMMMMMMMMMMMMMMMMMMMMMMMMk OMMMMNKKKKKKKKKKNMK oMMMMMMMMMMMMMMMM0c.', 'cyan')
        print colored('               .. ;:oxOXWMMMMMMMMMMMMMWO   ....            .. ,WMMMMMMMMMMMMXl.', 'cyan')
        print colored('                        . :dONMMMMMMKo.                         OWMMMMMMMNO:', 'cyan')
        print colored('                             .ckkkkl.                            .lkkkkkc.', 'cyan')

        print colored('                                                                  ', 'blue')
        print colored('                                                                  ', 'blue')

        print colored('===================================================================', 'blue')
        print colored('LINUX SERVER PROVISIONING                          ', 'blue', attrs=['bold'])
        print colored('===================================================================', 'blue')

        with cd('/home/vagrant'):
            if exists('/home/vagrant/proton', use_sudo=True):
                with cd('/home/vagrant/proton'):
                    sudo('apt-get update')
                    run('git pull && git checkout dev-test')
                    run('fab -p vagrant -R local install_postfix_ubuntu_14')
                    run('fab -p vagrant -R local install_squid_ubuntu_14')
                    run('fab -p vagrant -R local install_apache24_ubuntu_14')
                    run('fab -p vagrant -R local nfs_server_ubuntu:/srv/nfs')
                    run('fab -p vagrant -R local install_logrotate_ubuntu_14')
                    run('fab -p vagrant -R local install_munin_master_ubuntu_14')
            else:
                run('git clone https://github.com/exequielrafaela/proton.git')
                with cd('/home/vagrant/proton'):
                    sudo('apt-get update')
                    run('git checkout dev-test')
                    run('fab -p vagrant -R local install_postfix_ubuntu_14')
                    run('fab -p vagrant -R local install_squid_ubuntu_14')
                    run('fab -p vagrant -R local nfs_server_ubuntu:/srv/nfs')
                    run('fab -p vagrant -R local install_logrotate_ubuntu_14')
                    run('fab -p vagrant -R local install_munin_master_ubuntu_14')

        print colored('##########################', 'blue')
        print colored('##### START FIREWALL #####', 'blue')
        print colored('##########################', 'blue')

        # CONSIDER:
        # root@mailproxylinux:/etc/munin/plugin-conf.d# netstat -putona | egrep -i '22|3128|25|80|443|4949'
        # tcp        0      0 0.0.0.0:52526           0.0.0.0:*               LISTEN      781/rpc.statd    off (0.00/0/0)
        # tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      1862/sshd        off (0.00/0/0)
        # tcp        0      0 172.16.0.10:3128        0.0.0.0:*               LISTEN      22317/squid3     off (0.00/0/0)
        # tcp        0      0 0.0.0.0:25              0.0.0.0:*               LISTEN      22172/master     off (0.00/0/0)
        # tcp        0      0 10.0.2.15:22            10.0.2.2:50106          ESTABLISHED 3855/sshd: vagrant  keepalive (2683.93/0/0)
        # tcp        0      0 10.0.2.15:22            10.0.2.2:40326          ESTABLISHED 24805/sshd: vagrant keepalive (3699.74/0/0)
        # tcp        0      0 10.0.2.15:22            10.0.2.2:40600          ESTABLISHED 27315/sshd: vagrant keepalive (2094.11/0/0)
        # tcp6       0      0 :::80                   :::*                    LISTEN      23617/apache2    off (0.00/0/0)
        # tcp6       0      0 :::4949                 :::*                    LISTEN      23695/perl       off (0.00/0/0)
        # tcp6       0      0 :::22                   :::*                    LISTEN      1862/sshd        off (0.00/0/0)
        # tcp6       0      0 :::25                   :::*                    LISTEN      22172/master     off (0.00/0/0)
        # tcp6       0      0 :::443                  :::*                    LISTEN      23617/apache2    off (0.00/0/0)
        # udp        0      0 0.0.0.0:51013           0.0.0.0:*                           22317/squid3     off (0.00/0/0)
        # udp        0      0 0.0.0.0:52293           0.0.0.0:*                           781/rpc.statd    off (0.00/0/0)
        # udp6       0      0 ::1:46032               ::1:40978               ESTABLISHED 22317/squid3     off (0.00/0/0)
        # udp6       0      0 ::1:40978               ::1:46032               ESTABLISHED 22320/(pinger)   off (0.00/0/0)
        # udp6       0      0 :::54445                :::*                                22317/squid3     off (0.00/0/0)

        # # To stop Ipv4 based iptables firewall
        # sudo('iptables-save > $HOME/firewall.txt')
        # sudo('iptables -X')
        # sudo('iptables -t nat -F')
        # sudo('iptables -t nat -X')
        # sudo('iptables -t mangle -F')
        # sudo('iptables -t mangle -X')
        # sudo('iptables -P INPUT ACCEPT')
        # sudo('iptables -P FORWARD ACCEPT')
        # sudo('iptables -P OUTPUT ACCEPT')
        #
        # # To stop Ipv6 based iptables firewall, enter:
        # sudo('ip6tables-save > $HOME/firewall-6.txt')
        # sudo('ip6tables -X')
        # sudo('ip6tables -t mangle -F')
        # sudo('ip6tables -t mangle -X')
        # sudo('ip6tables -P INPUT ACCEPT')
        # sudo('ip6tables -P FORWARD ACCEPT')
        # sudo('ip6tables -P OUTPUT ACCEPT')

        # To start Ipv4 based iptables firewall, enter:
        # SSH management
        sudo('iptables -A INPUT -p tcp -s 10.0.2.0/24 --dport ssh -j ACCEPT')
        sudo('iptables -A INPUT -p tcp -s 172.16.0.0/24 --dport ssh -j ACCEPT')
        sudo('iptables -A INPUT -p tcp -s 192.168.0.0/24 --dport ssh -j ACCEPT')
        #sudo('iptables -A INPUT -p tcp -s 0.0.0.0/0 --dport ssh -j DROP')

        # SMTP POSTFIX
        sudo('iptables -A INPUT -p tcp -s 172.16.0.0/24 --dport 25 -j ACCEPT')
        sudo('iptables -A INPUT -p tcp -s 192.168.0.0/24 --dport 25 -j ACCEPT')
        sudo('iptables -A INPUT -p tcp -s 0.0.0.0/0 --dport 25 -j DROP')

        # HTTP APACHE2
        sudo('iptables -A INPUT -p tcp -s 172.16.0.0/24 --dport 80 -j ACCEPT')
        sudo('iptables -A INPUT -p tcp -s 192.168.0.0/24 --dport 80 -j ACCEPT')
        sudo('iptables -A INPUT -p tcp -s 0.0.0.0/0 --dport 80 -j DROP')

        # HTTPS APACHE2
        sudo('iptables -A INPUT -p tcp -s 172.16.0.0/24 --dport 443 -j ACCEPT')
        sudo('iptables -A INPUT -p tcp -s 192.168.0.0/24 --dport 443 -j ACCEPT')
        sudo('iptables -A INPUT -p tcp -s 0.0.0.0/0 --dport 443 -j DROP')

        # PROXY SQUID3
        sudo('iptables -A INPUT -p tcp -s 172.16.0.0/24 --dport 3128 -j ACCEPT')
        sudo('iptables -A INPUT -p tcp -s 192.168.0.0/24 --dport 3128 -j ACCEPT')
        sudo('iptables -A INPUT -p tcp -s 0.0.0.0/0 --dport 3128 -j DROP')

        # PROXY SQUID3
        sudo('iptables -A INPUT -p tcp -s 172.16.0.0/24 --dport 4949 -j ACCEPT')
        sudo('iptables -A INPUT -p tcp -s 192.168.0.0/24 --dport 4949 -j ACCEPT')
        sudo('iptables -A INPUT -p tcp -s 0.0.0.0/0 --dport 4949 -j DROP')

        # DROP EVERY OTHER TRAFFIC
        #sudo('iptables -A INPUT -j DROP')

        print colored('######################################', 'blue')
        print colored('END FIREWALL - NAT TABLE STATUS:      ', 'blue')
        print colored('######################################', 'blue')
        with hide('output'):
            fw = sudo('iptables -t nat -L')
        print colored(fw, 'red')

        print colored('######################################', 'blue')
        print colored('END FIREWALL - FILTER TABLE STATUS:   ', 'blue')
        print colored('######################################', 'blue')
        with hide('output'):
            fw = sudo('iptables -L')
        print colored(fw, 'red')

        print colored('##########################', 'blue')
        print colored('## NETWORK CONFIGURATION #', 'blue')
        print colored('##########################', 'blue')
        with hide('output'):
            netconf = sudo('ip addr show')
        print colored(netconf, 'yellow')


def client():
    with settings(warn_only=False):

        print colored('################################################################', 'red', attrs=['bold'])
        print colored('################################################################', 'red', attrs=['bold'])

        print colored(' _     _                     ____ _ _            _   ', 'blue', attrs=['bold'])
        print colored('| |   (_)_ __  _   ___  __  / ___| (_) ___ _ __ | |_ ', 'blue', attrs=['bold'])
        print colored('| |   | |  _ \| | | \ \/ / | |   | | |/ _ \  _ \| __|', 'blue', attrs=['bold'])
        print colored('| |___| | | | | |_| |>  <  | |___| | |  __/ | | | |_ ', 'blue', attrs=['bold'])
        print colored('|_____|_|_| |_|\__,_/_/\_\  \____|_|_|\___|_| |_|\__|', 'blue', attrs=['bold'])

        print colored('                                                                  ', 'blue')
        print colored('                                                                  ', 'blue')

        print colored('===================================================================', 'blue')
        print colored('LINUX CLIENT PROVISIONING                          ', 'blue', attrs=['bold'])
        print colored('===================================================================', 'blue')

        with cd('/home/vagrant'):
            if exists('/home/vagrant/proton', use_sudo=True):
                with cd('/home/vagrant/proton'):
                    sudo('apt-get update')
                    run('git pull && git checkout dev-test')
                    run('fab -p vagrant -R local install_munin_node_ubuntu_14')
            else:
                run('git clone https://github.com/exequielrafaela/proton.git')
                with cd('/home/vagrant/proton'):
                    sudo('apt-get update')
                    run('git checkout dev-test')
                    run('fab -p vagrant -R local install_munin_node_ubuntu_14')

        print colored('##########################', 'blue')
        print colored('##### START FIREWALL #####', 'blue')
        print colored('##########################', 'blue')

        # # To stop Ipv4 based iptables firewall
        # sudo('iptables-save > $HOME/firewall.txt')
        # sudo('iptables -X')
        # sudo('iptables -t nat -F')
        # sudo('iptables -t nat -X')
        # sudo('iptables -t mangle -F')
        # sudo('iptables -t mangle -X')
        # sudo('iptables -P INPUT ACCEPT')
        # sudo('iptables -P FORWARD ACCEPT')
        # sudo('iptables -P OUTPUT ACCEPT')
        #
        # # To stop Ipv6 based iptables firewall, enter:
        # sudo('ip6tables-save > $HOME/firewall-6.txt')
        # sudo('ip6tables -X')
        # sudo('ip6tables -t mangle -F')
        # sudo('ip6tables -t mangle -X')
        # sudo('ip6tables -P INPUT ACCEPT')
        # sudo('ip6tables -P FORWARD ACCEPT')
        # sudo('ip6tables -P OUTPUT ACCEPT')

        print colored('######################################', 'blue')
        print colored('END FIREWALL - NAT TABLE STATUS:      ', 'blue')
        print colored('######################################', 'blue')
        with hide('output'):
            fw = sudo('iptables -t nat -L')
        print colored(fw, 'red')

        print colored('######################################', 'blue')
        print colored('END FIREWALL - FILTER TABLE STATUS:   ', 'blue')
        print colored('######################################', 'blue')
        with hide('output'):
            fw = sudo('iptables -L')
        print colored(fw, 'red')

        print colored('##########################', 'blue')
        print colored('## NETWORK CONFIGURATION #', 'blue')
        print colored('##########################', 'blue')
        with hide('output'):
            netconf = sudo('ip addr show')
        print colored(netconf, 'yellow')
