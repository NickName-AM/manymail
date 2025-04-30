from django.core.mail import send_mail

import re

class CustomMassMail:
    def __init__(self, email, passw, subject, body, fields, recipient_list):
        self.email = email
        self.passw = passw
        self.subject = subject
        self.body = body
        self.fields = fields
        self.recipient_list = recipient_list

    # Generate custom email body for a particular recipient
    def __generate_custom_body(self, fields_data):
        message = self.body
        if self.fields:
            for field in zip(self.fields, fields_data):
                message = re.sub(field[0], field[1], message)
        
        return message

    # Send mass mail to each recipient while changing
    # message content
    def custom_send_mass_mail(self):
        for recipient in self.recipient_list:
            custom_body = self.__generate_custom_body(recipient["email_change_data"])
            send_mail(
                self.subject,
                custom_body,
                self.email,
                [recipient["email_to"]],
                fail_silently=False,
                auth_user=self.email,
                auth_password=self.passw
            )

            # print(self.email)
            # print(self.passw)
            # print(self.subject)
            # print(self.body)
            # print(custom_body)
            # print(self.fields)
            # print(self.recipient_list)