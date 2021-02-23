from config.settings import EMAIL_ACCOUNT, EMAIL_AUTH
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


class SendServer(object):
    '''A server to send email.'''

    def __init__(self,):
        self.email = EMAIL_ACCOUNT
        self.auth = EMAIL_AUTH

    def _authLogin(self):
        server = smtplib.SMTP_SSL('smtp.qq.com', 465)
        try:
            server.login(self.email, self.auth)
            return server
        except Exception as e:
            print(e)
            return False

    def _compContent(self, receiver, mail):
        message = MIMEMultipart('related')
        message['Subject'] = mail['subject']
        message['From'] = self.email
        message['To'] = receiver
        text = mail['content']
        content = MIMEText(
            f'<html><body>{text}</body></html>', 'html', 'utf-8')
        message.attach(content)

        return message

    def send(self, receiver, mail) -> bool:
        server = self._authLogin()
        if not server:
            return 0

        msg = self._compContent(receiver, mail)

        try:
            server.sendmail(self.email, receiver, msg.as_string())
            server.quit()
            return True
        except smtplib.SMTPException as e:
            print(e)
            return -1


sender = SendServer()
