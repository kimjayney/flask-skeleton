from allinone import mail
from flask.ext.mail import Message
from flask import url_for


def mail_send_invite(participant):
    from_user = participant.from_user
    to_user = participant.user
    msg = Message(
        'Hello',
        sender='admin@gmail.com',
        recipients=[to_user.email])
    msg.html = "asfewsfaewa"
    mail.send(msg)