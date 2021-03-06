import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

from config.settings import EMAIL_ACCOUNT, EMAIL_AUTH, EMAIL_NICKNAME


class SendServer(object):
    '''A server to send email.'''

    def __init__(self, ):
        self.email = EMAIL_ACCOUNT
        self.auth = EMAIL_AUTH

    def _authLogin(self):
        '''Login in smtp'''
        server = smtplib.SMTP_SSL('smtp.qq.com', 465)
        try:
            server.login(self.email, self.auth)
            return server
        except Exception as e:
            print(e)
            return False

    def _compContent(self, receiver, mail):
        '''Contract the email content.'''
        message = MIMEMultipart('related')
        message['Subject'] = mail['subject']
        message['From'] = formataddr([EMAIL_NICKNAME, self.email])
        message['To'] = receiver
        text = mail['content']
        content = MIMEText(
            f'<html><body>{text}</body></html>', 'html', 'utf-8')
        message.attach(content)

        return message

    def send(self, receiver, mail) -> bool:
        '''Email sender. Can call by outside.'''
        # server = self._authLogin()
        # if not server:
        #     return 0

        # msg = self._compContent(receiver, mail)

        # try:
        #     server.sendmail(self.email, receiver, msg.as_string())
        #     server.quit()
        #     return True
        # except smtplib.SMTPException as e:
        #     print(e)
        #     return -1
        # TODO: config the mail account and token
        return True


sender = SendServer()
