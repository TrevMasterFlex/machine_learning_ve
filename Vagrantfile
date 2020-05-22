Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-18.04"
  config.vm.provider :virtualbox do |vb|
    vb.cpus = 3
    vb.customize ["modifyvm", :id, "--memory", 4096]
  end
  config.vm.provision "shell", path: "provision.sh", privileged: true
end
