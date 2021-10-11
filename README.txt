1. Introduction

This project consists in an Ansible Playbook that first builds a Docker image containing an Apache Tomcat 9.0 server, and a web application called "sample" deployed on it.
After to build the Docker image, the Ansible Playbook creates a Docker container based on this image. The Apache Tomcat uses the port 8080 to serve the web application.
The Ansible Playbook uses a Pytest script to check if the container already exists. If the container doesn't exist, the Ansible Playbook builds the image and instantiate a container fom it.
Otherwise, nothing happens.
All the Python dependency (Pip, Pytest, Pytest-base-url, and Docker-py) needed to run the project is installed by the Ansible Playbook.

To create this project I used:

- Ubuntu Linux 20.04 LTS
- Git version 2.25.1
- Docker version 20.10.9, build c2ea9bc
- Python 3.8.10
- Ansible [core 2.11.5] 


2. Prerequisites

	Before to run the Ansible script, it's necessary to check if the following set of softwares are installed on your machine.

2.1 Git

	To check if Git is installed, run the following command:

	$ git --version

	On Ubuntu Linux, the result seems like this:

	$ git --version
	git version 2.25.1

	If Git is not installed on your machine, on Ubuntu Linux, run the following commands to install:

	$ sudo apt-get update
	$ sudo apt-get install git

	If you have questions on how to install Git, or if you are not using Ubuntu Linux, check out this documentation:

	https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

2.2 Docker

	To check if Docker is installed and running, run the following command:

	$ docker --version
	
	On Ubuntu Linux, the result seems like this:

	$ docker --version
	Docker version 20.10.9, build c2ea9bc

	If Docker is not installed on your machine, check out this documentation to install the latest version:

	https://docs.docker.com/get-docker/

	After to install Docker, let's check if it's running properly. On Ubuntu Linux, run the command below:

	$ sudo docker run hello-world

	If Docker is running, the result will be:

	$ sudo docker run hello-world
	Hello from Docker!

2.3 Python 3

	To check if Python 3 is installed, run the following command:

	$ python3 --version
	
	On Ubuntu Linux, the result seems like this:

	$ python3 --version
	Python 3.8.10

	If Python 3 is not installed on your machine, check out this documentation to install it:

	https://docs.python-guide.org/

	Now, let's check if Pytest is installed.
	On Ubuntu Linux, run this command:

	$ pytest --version
	
	If it's installed, the result will be:

	$ pytest --version
	pytest 6.2.5

	If Pytest is not installed, don't worry about it. Our Ansible script will install it.
	But, if you want to install Pytest in a manual way, check out this documentation:

	https://docs.pytest.org/en/6.2.x/getting-started.html

2.4 Ansible

	To check if Ansible is installed, run the following command:

	$ ansible --version

	The result will be like this, on Ubuntu Linux:

	$ ansible --version
	ansible [core 2.11.5] 

	If it's not installed, on Ubuntu Linux, you can run the following commands to install it:

	$ sudo apt-add-repository ppa:ansible/ansible
	$ sudo apt update
	$ sudo apt install ansible

	If you are using a different operating system, or if you have questions, check out this documentation: 

	https://docs.ansible.com/ansible/latest/installation_guide/index.html
	
3. Getting the project from Github

	Now, let's clone the project from Github.
	Access any directory that your user is the owner, and run the command below:

	$ git clone https://github.com/adornogomes/docker_webapp_project.git

	This is an example from Ubuntu Linux:

	$ pwd
	/home/adorno
	
	$ git clone https://github.com/adornogomes/docker_webapp_project.git
	Cloning into 'docker_webapp_project'...
	remote: Enumerating objects: 28, done.
	remote: Counting objects: 100% (28/28), done.
	remote: Compressing objects: 100% (22/22), done.
	remote: Total 28 (delta 6), reused 0 (delta 0), pack-reused 0
	Unpacking objects: 100% (28/28), 6.51 KiB | 606.00 KiB/s, done.

	A new directory will be created with the name "docker_webapp_project".
	Access the new directory and list the content.

	$ cd docker_webapp_project
	$ls -la 
	
	$ ls -la
	total 32
	drwxrwxr-x  4 adorno adorno 4096 Oct 11 10:10 .
	drwxr-xr-x 19 adorno adorno 4096 Oct 11 10:10 ..
	drwxrwxr-x  2 adorno adorno 4096 Oct 11 10:10 docker
	drwxrwxr-x  8 adorno adorno 4096 Oct 11 10:10 .git
	-rw-rw-r--  1 adorno adorno  106 Oct 11 10:10 hosts
	-rw-rw-r--  1 adorno adorno 1121 Oct 11 10:10 main.yml
	-rw-rw-r--  1 adorno adorno  196 Oct 11 10:10 pytest_url.py
	-rw-rw-r--  1 adorno adorno   46 Oct 11 10:10 README.md

4. Checking the connection between Ansible and localhost

	It's expected that our Ansible script runs on localhost using Python 3.
	The file "hosts", present in the project, has the following configuration:

	localhost-py3 ansible_host=localhost ansible_connection=local ansible_python_interpreter=/usr/bin/python3

	But, if you want to make sure that Ansible is running on localhost and using Python 3, add these 2 lines below to the file ansible.cfg:

	transport                  = local
	ansible_python_interpreter = /usr/bin/python3

	On Ubuntu Linux, you will find the file ansible.cfg in the directory "/etc/ansible/ansible.cfg".

	Now, we have to check if Ansible can connect to localhost.
	
	Access the directory "docker_webapp_project" and run the command below:

	$ ansible localhost-py3 -m ping -i hosts
		
	If everything is Ok, we have to receive this result:

	$ ansible localhost-py3 -m ping -i hosts
	localhost-py3 | SUCCESS => {
    	    "changed": false,
    	    "ping": "pong"
	}

5. Checking the port 8080

	Before to run the Ansible script, it's necessary to check if the port 8080 is being used by another application.
	As the container that will be created has an application running on this port, we need to check if the port is available.
	On Ubuntu Linux, use the command below to check:

	$ sudo lsof -i -P -n | grep LISTEN | grep 8080

	If the command doesn't return any result, the port is available.

6. Running the Ansible script

	To run the Ansible script, access the directory "docker_webapp_project" and run the command below:

	$ ansible-playbook -i hosts main.yml --ask-become-pass

7. Accessing the "sample" application

	If the Ansible script ran with success, a Docker container was created running an Apache Tomcat 9.0 server, and a web application called "sample" will be available.
	Open an web browser and access this URL:

	http://localhost:8080/sample/

	Also, you can access the application using a terminal. For this, run the command below:

	$ curl http://localhost:8080/sample/
	


