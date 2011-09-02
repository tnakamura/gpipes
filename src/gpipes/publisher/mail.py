class MailPublisher(object):
    def __init__(self, config, environ):
        self.user_address = config.get("user_address")
        self.subject = config.get("subject", "send from Gpipes")
        self.sender_address = config.get("sender_address", "griefworker@gmail.com")

    def execute(self, content):
        from google.appengine.api import mail
        from gpipes import utils

        if not mail.is_email_valid(self.user_address):
            raise Exception("not valid mail address")

        body = ""
        for entry in content["entries"]:
            body = body + entry["title"] + "\n"
            body = body + entry["link"] + "\n"
            body = body + utils.get_summary(entry) + "\n\n"

        # Debug
        print(body)

        mail.send_mail(self.sender_address, self.user_address, self.subject, body)
        return content


def create(config, environ):
    return MailPublisher(config, environ)

