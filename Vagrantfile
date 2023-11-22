


VX_BOX = "CumulusCommunity/cumulus-vx"
VX_VERSION = "4.3.0"

Vagrant.configure(2) do |config|

  config.vm.define "r1" do |r1|
    r1.vm.box = VX_BOX
    r1.vm.box_version = VX_VERSION
    r1.vm.network "private_network", virtualbox__intnet: "eth0", auto_config: false
    r1.vm.network "private_network", virtualbox__intnet: "swp1", ip: "192.168.15.78/24"
    end

  config.vm.define "r2" do |r2|
    r2.vm.box = VX_BOX
    r2.vm.box_version = VX_VERSION
    r2.vm.network "private_network", virtualbox__intnet: "eth0", auto_config: false
    r2.vm.network "private_network", virtualbox__intnet: "swp1", ip: "192.168.12.11/24"
  end

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "helloworld.yaml"
    ansible.verbose ="v"
  end
end