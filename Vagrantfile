# -*- mode: ruby -*-
NUMBER_OF_WEBSERVERS = 2
CPU = 1
MEMORY = 512
ADMIN_USER = "vagrant"
ADMIN_PASSWORD = "vagrant"
VM_VERSION= "hashicorp/bionic64"
VAGRANT_VM_PROVIDER = "virtualbox"

VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  groups = {
    "webservers" => ["web[1:#{NUMBER_OF_WEBSERVERS}]"],
    "loadbalancers" => ["load_balancer"],
    "dbservers" => ["db"],
    "all_groups:children" => ["webservers","loadbalancers","dbservers"]
  }

  (1..NUMBER_OF_WEBSERVERS).each do |i|
    config.vm.define "web#{i}" do |node|
        node.vm.box = VM_VERSION
        node.vm.hostname = "web#{i}"
        node.vm.network :private_network, ip: "10.0.15.2#{i}"
        node.vm.network "forwarded_port", guest: 80, host: "808#{i}"
        node.vm.provider VAGRANT_VM_PROVIDER do |vb|
          vb.memory = MEMORY
          #vb.gui = true
        end

    # Only execute once the Ansible provisioner,
    # when all the machines are up and ready.

      if i == NUMBER_OF_WEBSERVERS
          node.vm.provision "ansible" do |ansible|
            ansible.playbook = "web.yml"
            ansible.become = true
            ansible.limit = "all"
            ansible.groups = groups
          end
        end

      end
    end


    # create load balancer
    config.vm.define "load_balancer" do |lb_config|
        lb_config.vm.box = VM_VERSION
        lb_config.vm.hostname = "lb"
        lb_config.vm.network :private_network, ip: "10.0.15.11"
        lb_config.vm.network "forwarded_port", guest: 80, host: 8011
        lb_config.vm.provider VAGRANT_VM_PROVIDER do |vb|
          vb.memory = MEMORY
        end
        lb_config.vm.provision "ansible" do |ansible|
          ansible.playbook = "loadbalancer.yml"
          ansible.become = true
          ansible.groups = groups
        end
    end
    # create redis db server
    config.vm.define "db" do |db_config|
        db_config.vm.box = VM_VERSION
        db_config.vm.hostname = "db"
        db_config.vm.network :private_network, ip: "10.0.15.12"
        db_config.vm.provider VAGRANT_VM_PROVIDER do |vb|
          vb.memory = MEMORY
        end
        db_config.vm.provision "ansible" do |ansible|
          ansible.playbook = "db.yml"
          ansible.become = true
          ansible.groups = groups
        end
    end
end
