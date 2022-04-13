# Docker Deployment with Security Implementation

[In Progress...]

### Deployment Steps                
Follow the steps to deploy the network.

**1. Installing Prerequisites:**

Use the following commands to install the prerequisites including updating, installing Python and Ansibe:
    
```
sudo apt-get update
sudo apt-get install python-minimal
sudo apt -y install ansible
```

**2. Running Ansible Playbook to deploy the Network:**

Deploy the network using the following command:

``` ansible-playbook -K [Name of file].yml -e "internet_network_interface=[network interface name] ```

Replace the [Name of file] with the name of the playbook. Also, replace [network interface name] with the name of the interface. This can be found using ```ifconfig``` command.

Once the command runs, it starts to set up the network and configures the core network functions from Free5GC. This process of configuration is shown in the Figure.

![](Results/1-Configuring_Core_network_functions.PNG)

Ansible runs all the network entities in separate containers. This process is shown in the Figure.

![](Results/2-Running_containers.PNG)

We verify the running containers using the command:

``` sudo docker ps ```

This command shows all the running containers in the system and this is shown in the Figure.

![](Results/3-Check_Running_dockers.PNG )

