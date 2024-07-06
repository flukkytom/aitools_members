# aitools_members
AI Tools Member Application

# aitools_members
AiKloud Admin Application

The Admin (Adama) Application helps to approve Ai Tools Submission.

Run the download_nltk.py script once to enable searfch application


1. Install Git
`sudo yum install git`

2. Git Clone the aitools_admin repo
remember to use your github token as password
`git clone https://github.com/flukkytom/aitools_members.git`

To create Tokens for Password for Git Clone
`Tokens: https://www.educative.io/answers/how-to-create-a-personal-access-token-for-github-access`
3. Install Virtualenv
`yum install virtualenv`

4. Create a virtual environment (cd into your repo directory)
`virtualenv environment`
(If you encounter a virtualenv: command not found. Use `yum install virtualenv`)

5. Install GCC
`yum install gcc`

6. Install Python Devel
`yum install python-devel`

7. Find Mysql Devel
`sudo yum search mysql | grep devel`
   ont worry if this step gives you an error, try #step 7 nonetheless if your are using Linux AMI 2023)

8. Install the Devel found (mariadb105-devel)
`sudo yum install mariadb105-devel`

9. Activate your Virtual Environment
`source environment/bin/activate`

10. Install the Application requirements
`pip install -r requirements.txt`

11. Run your Application
`python application.py`


Remember to update the application.py to 8090
=======
Database Connection
===================

If you get your database connection strings

edit the file config.py `SQLALCHEMY_DATABASE_URI = 'mysql://<database_user>:<database_password>@<endpoint>/<database_name>'`

