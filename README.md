# voter-fraud
A simple python blockchain based application for voter fraud deflection

Implementation of the Project[Can be added to readme.md]:

*Go into repo and create and activate virtual environment as usual:

py -3 -m venv venv

venv\Scripts\activate

*INSTALLATIONS to be done in the venv(Until/as long as there isn't a requirements.txt file):

pip install Flask
* Get MySQL workbench/command line client installed before the next step
pip install flask-mysqldb
pip install requests(For Sumuk to see and add if any other installation requirements are there)
 
*Open MySQL workbench/command line client

Step-4: Execute the queries in 'mysqlconn.txt' in local db, which are also 
CREATE DATABASE IF NOT EXISTS {yourdbname} CHARACTER SET utf8 COLLATE utf8_general_ci;
USE {yourdbname};

CREATE TABLE IF NOT EXISTS accounts (
id int(11) NOT NULL AUTO_INCREMENT,
username varchar(50) NOT NULL,
password varchar(255) NOT NULL,
email varchar(100) NOT NULL,
organisation varchar(100) NOT NULL,
address varchar(100) NOT NULL, 
country varchar(100) NOT NULL,
city varchar(100) NOT NULL,
state varchar(100) NOT NULL,
postalcode varchar(100) NOT NULL,
PRIMARY KEY (id))
ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

*Note: Same DB to be connected to in "app.py" in lines(18-21) that look like as follows:

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root' 
app.config['MYSQL_PASSWORD'] = 'yourpassword'
app.config['MYSQL_DB'] = 'yourdbname'
