# aitools_members
AI Tools Member Application


1. Install Git
`sudo yum install git`

2. Git Clone the aitools_admin repo
remember to use your github token as password
`git clone https://github.com/flukkytom/aitools_members.git`

To create Tokens for Password for Git Clone
`Tokens: https://www.educative.io/answers/how-to-create-a-personal-access-token-for-github-access`

3. Install Virtualenv
`yum install virtualenv`

4. cd into your repo directory - `cd aitools_members`

5. Create a virtual environment (cd into your repo directory)
`virtualenv environment`

6. Install GCC
`yum install gcc`

7. Install Python Devel
`yum install python-devel`

8. Find Mysql Devel
`sudo yum search mysql | grep devel`
   ont worry if this step gives you an error, try #step 7 nonetheless if your are using Linux AMI 2023)

9. Install the Devel found (mariadb105-devel)
`sudo yum install mariadb105-devel`

10. Activate your Virtual Environment
`source environment/bin/activate`

11. Install the Application requirements
`pip install -r requirements.txt`

12. Run your Application
`python application.py`


Remember to update the application.py to 8090
=======
Database Connection
===================

If you get your database connection strings

edit the file config.py `SQLALCHEMY_DATABASE_URI = 'mysql://<database_user>:<database_password>@<endpoint>/<database_name>'`

