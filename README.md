# flask_4_databases_mysql_vm

## MySQL Setup on Azure VM

### Creating MySQL VM on Azure

<img width="1440" alt="Screenshot 2023-12-12 at 09 13 03" src="https://github.com/ktdutta/flask_4_databases_mysql_vm/assets/141374153/8de8df9b-4ca6-45c3-89f8-10199aa51367">

Make sure the proper inbound port rules are selected. As we are using MySQL it is important that the Port 3306 is added in order to get for inbound traffic from MySQL workbench.

<img width="578" alt="Screenshot 2023-12-12 at 10 25 49" src="https://github.com/ktdutta/flask_4_databases_mysql_vm/assets/141374153/40fca48b-e914-41c1-9f52-f29b1ee428e3">


### Installing MySQL on Created VM 

First we logged into the virtual machine we created on Azure using the following command
```ssh username@ip address```


Then we update the operating system  
```sudo apt-get update```

Following the updates we install 2 pieces of software required to run MySQL
```sudo apt install mysql-client mysql-server```

Open up mysql with the following command
```sudo mysql```

<img width="959" alt="Screenshot 2023-12-12 at 09 44 52" src="https://github.com/ktdutta/flask_4_databases_mysql_vm/assets/141374153/55d9a906-7b4a-4cba-be95-575efa988f5d">

Create a username and password for MySQL Workbench connection
```create user 'keerthana'@'%' identified by 'keerthana2023';```

Update privileges/user permissions
```grant all privileges on *.* to ‘keerthana’@’%’ with grant option;```

Go into the configuration file to enable additional privileges which would allow any computer to connect by changing the binding address to 0.0.0.0. Then you must run a reset command before attempting to connect the virtual machine to MySQL workbench. 

### 2 Table Database Creation

```
create database emr;
show databases;
```
<img width="654" alt="Screenshot 2023-12-12 at 11 16 54" src="https://github.com/ktdutta/flask_4_databases_mysql_vm/assets/141374153/e741a532-b05b-4313-ac2f-44ab5d2dbaff">

#### Creating 2 Tables 

<img width="577" alt="Screenshot 2023-12-12 at 11 27 45" src="https://github.com/ktdutta/flask_4_databases_mysql_vm/assets/141374153/a17a6eec-5004-4a82-b527-9edb3138236d">

### Connecting to MySQL Workbench 

After adding our new connection to MySQL Workbench, we can see that the database and two tables we created within the database called emr are present in MySQL Workbench schema. 

<img width="1037" alt="Screenshot 2023-12-12 at 12 49 49" src="https://github.com/ktdutta/flask_4_databases_mysql_vm/assets/141374153/36c6b1de-4901-4687-aa23-a3e4b5009e26">
