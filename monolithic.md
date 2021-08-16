
DNS---Ec2---ReactJS---apis----Ec2--Flask--Database (RDS--mysql)




frontend --repo - appdemo --reactJS
api --repo - apidemo --- flask 


RDS
backup enable
monitoring -Cloudwatch - Dashboard for the RDS --cpu / number of connections / Storage 
alert RDS cpu usage goes more than 5% - email test 
-[ ] Create own repo - 





Taksks 

Create the repos in your branch
- [ ] appdemo --main / develop / stage/ preprod / prod - Protected ---index.html
- [ ] apidemo --main / develop / stage/ preprod / prod - Protected----helloworld.py- flask

- [ ] create the 4 vpcs 
      - [ ] dev -10.1 - bastion---rds--jenkins
      - [ ] stage -10.2
      - [ ] preprod-10.3
      - [ ] prod -10.4 - bastion --rds--jenkins
      - [ ]  create the dev bastion 
      - [ ]  create the jenkins in private 
      - [ ]  create the alb separate for the jenkins
      - [ ]  create the reactJS and flask api in the private subnet
      - [ ]  create the internete load balancer and attach to the reactjs
      - [ ]  craete the internal load balancer and attach to the flaskapi
- [ ] vpc peering between dev - stg, dev-preprod
      - [ ] do ssh/telnet from dev bastion to dev private environments (jenkins/reactjs/flask/rds)
      - [ ] do ssh/telnet from dev bastion to stage private environments (jenkins/reactjs/flask/rds)
      - [ ] do ssh/telnet from dev bastion to preprod private environments (jenkins/reactjs/flask/rds)


- [ ]  do ssh/telnet from prod bastion to prod private environments (jenkins/reactjs/flask/rds)



day-1
### DEV 
#### Infra
- [x] create the repos - apidemo,appdemo,infrademo (follow the branching strategy)
- [x] Create the vpc for dev : vpc name: dev - 10.1.0.0/16
    * dev-public-subnet-1a , public-subnet-1b
    * dev-private-subnet-1a 
    * dev-data-subnet-1a 
    * dev-igw
    * dev-natgw
    * dev-public-route
    * dev-private-route
    * dev-eip
- [x] create the bastion in :dev-bastion
- [x] create the jenkins :dev-jenkins
- [ ] create the react/api : dev-app, dev-api
- [ ] create the rds - dev-rds , dbname: dev_api , username: dev_apiuser
- [ ] create the 3 alb , 
      * jenkins-alb 
      * app-alb 
      * api-alb --private subnet--internal 



#### CICD:
- [ ] - create jenkins pipeline job for the : dev-appdeploy : /opt/app
- [ ] create the jenkins pipeline job for the: dev-apideploy : /opt/api

### validatoin:
hello world : dev.domain-name--app
hellowrold.py : ls -ltr /opt/api
test.py : ls -ltr /opt/api








#### Observability:
- [ ] Grafana , Prometheus - ec2 - check instances - 3
- [ ] Kibana, ElasticSearch - Ec2 - check kibana url 

