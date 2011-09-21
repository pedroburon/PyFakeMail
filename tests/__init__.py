import unittest
import mock
import smtplib

from pyfakemail import FakeMailSMTPServer

class TestSMTPServer(unittest.TestCase):
    
    def test_receive_mail(self):
        smtp_server = FakeMailSMTPServer(('127.0.0.1', 1025), ('localhost', 1026))


        sender = 'foo@example.net'
        receiver = 'bar@example.net'
        content = 'content'
        smtp_server.process_message(('127.0.0.1', 38389), sender, receiver, content)

        last_mail = smtp_server.last()
        self.assertEquals(last_mail['mailfrom'], sender)
        self.assertEquals(last_mail['rcpttos'], receiver)
        self.assertEquals(last_mail['data'], content)
