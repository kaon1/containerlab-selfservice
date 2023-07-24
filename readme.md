Repo related to blog post https://kaonbytes.com/p/self-service-containerlab-deployment-with-ansible-tower/

Self-Service ContainerLab Deployment with Ansible Tower
Generating dynamic ContainerLab topology files with ansible to facilitate team labbing and learning

## About

Not long ago, I was asked by [Kris Beevers](https://www.linkedin.com/in/beevek/), the CEO of [NetBox Labs](https://netboxlabs.com/) --- what actionable steps I recommend for individuals who are interested in a career in network engineering. My number one answer is to lab it up. Deploying a lab environment and getting hands on to solve a real (or made up) problem is the best way to accelerate your learning.

There are multiple ways to create network lab environments: if you have the resources to grab real physical gear go for it. However, this has limitations, there is a cost to this, power, cabling, and space requirements. Another option is to use an application such as Eve-NG or GNS3. These platforms let you deploy virtual machine based lab images. However, the images are usually memory intensive and not programmatically friendly.

Luckily for us, in the last few years more and more vendors are providing containerized network operating systems. A network OS hosted on a docker container uses significantly less cpu and memory and can be deployed using infrastructure-as-code methods (IAC)

SRL Labs has built an open source tool called [ContainerLab](https://containerlab.dev/) which can orchestrate a routing topology for these network containers. In addition to network operating systems, ContainerLab allows us to deploy and virtually wire-up arbitrary linux containers to host applications. This can allow for full end-to-end testing of the application and network stack.

ContainerLab does have somewhat of a learning curve get labs up and running. I realize that not all network engineers want to learn a new platform or how docker containers work. For these cases, I built an Ansible wrapper which lets a user deploy their own pre-canned lab environment using Ansible Tower. The hope is that this limits the barrier to entry for using ContainerLab.

The solution can be found here