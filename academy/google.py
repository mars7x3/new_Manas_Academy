import base64
from email.message import EmailMessage

import httplib2
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient import discovery
from django.conf import settings

SCOPES = ('https://mail.google.com/', 'https://www.googleapis.com/auth/gmail.modify', 'https://www.googleapis.com/auth/gmail.compose', 'https://www.googleapis.com/auth/gmail.send',)

flow = InstalledAppFlow.from_client_secrets_file(settings.GOOGLE_PATH, SCOPES)
creds = flow.run_local_server(port=0)
# credentials = Credentials.from_authorized_user_file(settings.GOOGLE_PATH, SCOPES)
# delegated_credentials = credentials.with_subject('send-mail@schoolhouse-319706.iam.gserviceaccount.com')
# httpAuth = credentials.authorize(httplib2.Http())

gmail_service = discovery.build('gmail', 'v1', credentials=creds)


def google_send_mail():
    message = EmailMessage()

    message.set_content('This is automated draft mail')

    message['To'] = 'm.ysakov.jcc@gmail.com'
    # message['From'] = 'gduser2@workspacesamples.dev'
    message['Subject'] = 'Аллаху Агбар!'

    # encoded message
    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    create_message = {
            'raw': encoded_message
    }
    # pylint: disable=E1101
    send_message = (gmail_service.users().drafts().send(
        userId="m.ysakov.jcc@gmail.com",
        body=create_message
    ).execute())
    print(F'Message Id: {send_message["id"]}')
