"""
    Script for sending scheduled daily reports of top-sold brands 
    by store by email every day using cron job
"""
# Importing libraries
import pandas as pd
from pathlib import Path
from redmail import EmailSender
from configs import vars

# Create a dictionary with the email variables
EMAIL = {
    "host": vars.GMAIL_SERVER,
    "port": vars.PORT,
    "username": vars.GMAIL_EMAIL,
    "password": vars.GMAIL_PASSWORD,
}


# Define email sender object function
def email_sender(email):
    return EmailSender(**email)


# Instaciate the email sender object
rm = email_sender(EMAIL)


# Define a function to read the csv file
def read_csv(file):
    """
    Description: Function to read the csv file
    Parameters: filename or path
    Returns: Dataframe
    """
    # Read data from csv file in the current directory
    return pd.read_csv(file)


# Define a function to send email for each store
def send_email_singular(data, email):
    """
    Sends an email to each email address in the csv file.
    Parameters:
        data (DataFrame): CSV data to be used for sending emails.
    Returns:
        None
    """
    # Iterate through the dataframe and send email for each row
    for index, row in df.iterrows():
        rm.send(
            subject=f"""Total Items Sold by {row['STORE']}""",
            sender=email["username"],
            receivers=[data.loc[5, "EMAIL"]],  # [row["EMAIL"]],
            # text=f"""
            # Hi {row['BRAND']},
            # Today, we sold {row['SOLD']} items in {row['STORE']}
            # Regards...
            # """,
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


# Define a function to send an aggregated email report to only one email
def send_email_attach(data, email):
    """
    Sends an email with the aggregated report and attaches the csv file
    Parameters:
        data (DataFrame): The csv data to be used for sending emails.
        email (str): The email address to send the report to.
    Returns:
        None
    """
    rm.send(
        subject=f"Total Items Sold by Store",
        sender=email["username"],
        receivers=[data.loc[5, "EMAIL"]],  # [row["EMAIL"]],
        # text=f"""
        # Hi {data.loc[5, "BRAND"]},
        # Today, we sold {data.loc[5, "SOLD"]} items in {data.loc[5, "STORE"]}
        # Regards...
        # """,
        html=f"""
        <H3>
            Hi [Manager_NAME],
        </H3>
        <P>
            Find the total sold items by store and brand in the attached csv file
        </P>
        <P>
            Regards...
        </P>
        """,
        attachments={
            "report.csv": Path("./report.csv"),
        },
    )


# Read the csv file
df = read_csv("./report.csv")

# Send email for each store
send_email_singular(df, EMAIL)

# Send email with attachment
send_email_attach(df, EMAIL)
