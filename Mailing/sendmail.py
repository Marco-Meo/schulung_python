import os
import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.multipart import MIMEMultipart


class Mailer:
    def __init__(self, server, user, password):
        self.server = server
        self.user = user
        self.password = password

    def senden(self, sender, receiver, subject, body, file_attachment=None, html=False):
        try:
            server = smtplib.SMTP(self.server)
            server.starttls()
            server.login(self.user, self.password)
        except Exception as e:
            server.quit()
            return -1

        msg = MIMEMultipart()
        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = ";".join(receiver)
        if html:
            msg.attach(MIMEText(body, 'html'))
        else:
            msg.attach(MIMEText(body, 'plain'))
        part = MIMEBase('application', 'octet-stream')
        # If it has an attachment
        if file_attachment:
            part.set_payload((file_attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename={}".format(os.path.basename(file_attachment.name)))
            msg.attach(part)
        try:
            response = server.sendmail(sender, receiver, msg.as_string())
        except Exception as e:
            return -1
        finally:
            server.quit()
        return response
