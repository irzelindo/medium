
## Automating with Python
#### Sending emails
Often, during our work, we came across repetitive tasks. Which usually ends up not adding any knowledge but becoming rather tiring. Is that your case?
How do you use such a situation to invest in your knowledge and add another good experience to your portfolio?
#### * Have you ever heard of programming?
#### * What benefits does it bring to your daily life?
#### * How can programming leverage your career?

Programming involves writing instructions for computers to execute. It's an essential skill in the field of computer science and technology. It's used to develop software, websites, mobile apps, and more. 
There is a tone of benefits it can bring into our daily lives, but for now, let us focus on the one that we want to tackle, 
Automation: Programming allows you to automate repetitive tasks, saving time and effort. This benefit of programming tackles the first paragraph of this article.
Regarding career leveraging, I can tell there's a high demand for skilled programmers across various industries. According to the World Economic Forum, Technology adoption will remain a key driver of business transformation in the next five years.
## Let's put our hands to work.
From the beginning, our goal has been to be able to automate sending emails  using Python programming language. We will use an advanced email sender library called Red Mail. Assuming we already have basic Python programming skills, we won't touch each detail of the programming language itself. If you want to learn Python, please visit Python books or the W3Schools Python tutorial.
First, let's find a recurring task. Assuming that we have to share a daily report of top-sold brands by store as shown in the table below.

Project Structure
├── app.py ------------- Script Entrypoint main file
├── configs ------------ Folder containing the environment variables and map to them
│   ├── env.ini -------- Env. variables (Email-Server, Port, Username, Passwords)
│   └── vars.py -------- Env, variables mapping 
├── report.csv --------- Data of daily sales by store in *.csv file
└── requirements.txt --- List of packages used (pip install -r requirements.txt)

Let's look at the code for each file:
### app.py
```python
"""
    Script for sending scheduled daily reports of top-sold brands 
    by email.
"""
# Importing libraries
import pandas as pd
from pathlib import Path
from redmail import EmailSender
from configs import vars

# Create a dictionary with the email configurations
EMAIL = {
    "host": vars.GMAIL_SERVER,
    "port": vars.PORT,
    "username": vars.GMAIL_EMAIL,
    "password": vars.GMAIL_PASSWORD,
}

# Define email sender object function
def email_sender(email):
    """
    Creates the Redmail object from the configuration
    parameters of the email.
    Parameters:
      email(dictionary) => Dictionary with email server 
      configuration parameters
    Returns:
      EmailSender object
    """
    return EmailSender(**email)

# Instaciate the email sender object
rm = email_sender(EMAIL)

# Define a function to read the CSV file
def read_csv(file):
    """
    Read the CSV file.
    Parameters: 
        path to the file
    Returns: 
        Dataframe
    """
    # Read data from the CSV file in the current directory
    return pd.read_csv(file)

# Define a function to send email for each store
def send_email_singular(data, email):
    """
    Sends an email to each email address in the CSV file.
    Parameters:
        data (DataFrame): CSV data to be used for sending emails.
    Returns:
        None
    """
    # Iterate through the data frame and send an email for each row
    for index, row in df.iterrows():
        rm.send(
            subject=f"""Total Items Sold by {row['STORE']}""",
            sender=email["username"],
            receivers=[email["BRAND"]],
            html=f"""
            <H3>
                Hi {row['BRAND']},
            </H3>
            <P>
                Today, we sold <strong>{row['SOLD']}</strong> items in <strong>{row['STORE']}</strong>
            </P>
            <P>
                Regards...
            </P>
            """,
        )

# Define a function to send an email with the report attached
def send_email_attach(data, email):
    """
    Sends an email with the report attached
    Parameters:
        data (DataFrame): The CSV data used to send emails.
        email (str): The email address to send the report.
    Returns:
        None
    """
    rm.send(
        subject=f"Total Items Sold by Store",
        sender=email["username"],
        receivers=[<EMAIL_ADDRESSES>] # Replace <EMAIL_ADDRESSES> with email addresses ,
        html=f"""
        <H3>
            Hi [Manager_NAME],
        </H3>
        <P>
            Find the total sold items by store and brand in the attached CSV file
        </P>
        <P>
            Regards...
        </P>
        """,
        attachments={
            "report.csv": Path("./report.csv"),
        },
    )

if __name__ == "__main__":
    # Read the CSV file
    df = read_csv("./report.csv")

    # Send an email for each store
    send_email_singular(df, EMAIL)

    # Send an email with the attachment
    send_email_attach(df, EMAIL)
```
The app.py file has four (4) defined functions:
email_sender: returns a Redmail EmailSender class instance (object).
read_csv(file): Receives the *.csv file path as a parameter and returns a pandas data frame.
send_email_singular(data, email): Receives two (2) parameters: the data frame and the email(email server, host, username, and password). Make sure to pass valid configurations to send the email. This function iterates over each row of the data frame(table) and sends an email to each brand about the quantity of sold items by store using the send() function of the EmailSender class. For more details, check the docs.
send_email_attach(data, email): This function attaches the *.csv file to the email and sends it to a specified list of email addresses on the receivers=[<EMAIL_ADDRESSES>] argument of the send() function.

### vars.py
```python
# Import Python OS module from the standard library
import os

# Import config parser from the standard library
from configparser import ConfigParser

# Define ROOT_DIR and APP_DIR
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.path.dirname(ROOT_DIR)

# Create ConfigParser object
cfg = ConfigParser()
# Pass path to env.ini
cfg.read(os.path.join(ROOT_DIR, "env.ini"))

# Read values from env.ini into the ConfigParser object

# Default
PORT = cfg.get("default", "port")
TLS = cfg.get("default", "tls")

# Outlook
OUTLOOK_SERVER = cfg.get("outlook", "server")
OUTLOOK_EMAIL = cfg.get("outlook", "username")
OUTLOOK_PASSWORD = cfg.get("outlook", "password")

# Gmail
GMAIL_SERVER = cfg.get("gmail", "server")
GMAIL_EMAIL = cfg.get("gmail", "username")
GMAIL_PASSWORD = cfg.get("gmail", "password")
It's a good practice not to share the environment variables in the code so we can store them securely using the *.inifile. Remember to add the *.ini into.gitignore to avoid pushing this file into the GitHub repository, this way the environment variables will be only visible on the local machine. From the vars.pyfile, we can quickly point to the variable's names in the env.ini file using the Python configparser library. Below is an overview of what the *.ini file looks like.
[default] 
port = 587
tls = True

[outlook]
server = smtp.office365.com
username = <EMAIL ADDRESS>
password = <PASSWORD>

[gmail]
server = smtp.gmail.com
username = <EMAIL ADDRESS>
password = <PASSWORD>
```
*** Requirements.txt
The simplest way to store the used libraries and dependencies on the project is to run pip freeze > requirements.txt and save those into a text file that can be made portable to run the project on another machine. To install the libraries and dependencies, use the command pip install -r requirements.txt 
```python
Jinja2==3.1.2
MarkupSafe==2.1.3
numpy==1.26.2
pandas==2.1.4
python-dateutil==2.8.2
pytz==2023.3.post1
redmail==0.6.0
six==1.16.0
tzdata==2023.3
```

With all these in place, we can now send emails using Python for more options like embedding HTML, Jinja templating, adding images, sending emails with CC, and more. Please refer to this Redmail documentation.
---

How do we make this script recurring?
On Windows, we can use (Task Scheduler, NSSM, …)
On Linux & Mac, we can make use of cron jobs from Crontab
In this specific article, we're going to schedule the script using the Windows task scheduler.
Task Scheluder (Microsoft Windows 11)To create a new task, we can either right-click on the left list pane Task Scheduler Libraryand select Create Task or, on the right list pane click on Create Task as well. The window below will pop out. Here, we can insert the task name and choose the group of users.
On the triggers tab, left click on the new button to create a task schedule. 
Here, we set the task to run daily to this schedule to work; it must be set to enabled. Lastly, we must put the script file to run on this schedule. Choose the Start a program option from the combo-box Action: In the Settings section on the tab actions, Browse to the Python executable file, i.e., C:\\schedule\env\scripts\python.exe, for the virtual environment, on the Add argument (optional): input insert the name of the main Python file (the file that runs when the program is executed), on the Start in (optional): input the path to the script folder i.e., C:\\schedule\ after completing these steps the schedule for the script is completed.
Select the task name from the task scheduler list of tasks and left-click on the right-side pane run button to execute the task as shown below.
If all is well set, we should be able to run our task, and the script will be scheduled to run every day at midnight according to our schedule settings. We should also have our script automated. 
Our first automation episode (#1) is ready to work with that in place. feel free to fork  (branch email_sender) and have some fun.
Thanks for reading…
Irzelindo Salvador…
Regards…
