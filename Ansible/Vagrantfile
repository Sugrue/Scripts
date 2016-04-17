
secret = YAML.load_file("Jumphost/.secret.yaml")

Vagrant.configure('2') do |config|
  node = { hostname: "Ubuntu.Trusty64-Jumphost",
               box: 'ubuntu/trusty64',
               mem: 1024,
               cpu: 1 }
  # commented out until vagrant 1.8.2
  # config.vm.provider :vcenter do |vcenter|
  #   node[:ip] = "10.2.20.10"
  #   node[:mask] = "255.255.255.0"
  #   node[:gw] = 10.2.20.1"
  #   node[:dns_server_list] = ['10.2.10.2', '8.8.8.8']
  #   node[:dns_suffix_list] = ['lab.sugrue.ca']
  #   node[:mem] = 1024
  #   node[:cpu] = 1
  #
  #   vcenter.hostname = 'vcenter.sugrue.ca'
  #   vcenter.username = secret['username']
  #   vcenter.password = secret['password']
  #   #vcenter.folder_name = ''
  #   vcenter.datacenter_name = 'Datacenter'
  #   vcenter.computer_name = 'esxi.c220.oshawa.sugrue.ca'
  #   vcenter.datastore_name = 'C220 - SAS - RAID 6'
  #   vcenter.network_name = 'VLAN 2200 - Dev Servers'
  # end


  config.vm.define node[:hostname] do |node_config|
    node_config.vm.box = node[:box]
    node_config.vm.hostname = node[:hostname]


    if node.key?("ip")
      node_config.vm.network :public_network,
                             ip: node[:ip],
                             netmask: node[:mask],
                             gateway: node[:gw],
                             dns_server_list: node[:dns_server_list],
                             dns_suffix_list: node[:dns_suffix_list]
    end
    #direct ansible provisioning workaround until 1.8.2
    config.vm.provision :shell, inline: <<SCRIPT
    #!/usr/bin/env bash
    sudo apt-get install software-properties-common
    sudo apt-add-repository ppa:ansible/ansible
    sudo apt-get update
    sudo apt-get install -y ansible
    ansible-playbook -i 'localhost ansible_connection=local,' /vagrant/Jumphost/jumphost.yml
SCRIPT

  end
end
