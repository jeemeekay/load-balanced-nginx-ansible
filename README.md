# Vagrant nginx-loadbalancer for 2 nginx webservers

## Overview: 
The solution is based on 2 nginx web servers, 1 nginx load balancer and 1 redis db. The nginx web servers have a proxypass config to a python flask web app that returns a 'hello world' string that is read from the redis database server. 



## Requirements: 
The solution was built on a mac laptop (as the vagrant host) with the following versions of software installed on vagrant host. 
- Vagrant 2.2.6
- Virtualbox 5.2.4 as vm provider
- Ansible 2.9.2 (as config manager/provisioner) with python 3.7.5




## Installation:  

        vagrant up
        

## Testing:
To test that loadbalancing works run the python script as below: In this example 4 requests are sent.  

        python3 test.py --url http://localhost:8011 --requests 4
        Making sure loadbalancing is working. Should get an even number of hits on each node
        b'Hello World in Redis DB served by web1': 2
        b'Hello World in Redis DB served by web2': 2


       









