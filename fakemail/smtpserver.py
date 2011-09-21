import smtpd
import asyncore
import threading
import logging

__all__ = ['FakeSMTPServer', 'FakeSMTPServerThread', 'run_smtp_server']

class FakeSMTPServer(smtpd.SMTPServer):
    
    _mails = []

    def process_message(self, peer, mailfrom, rcpttos, data):
        mail = {
            'peer' : peer, 
            'mailfrom' : mailfrom, 
            'rcpttos' : rcpttos, 
            'data' : data
        }
        logging.debug(mail)
        self._mails.append(mail)

    def last(self):
        return self._mails[-1]

    def first(self):
        return self._mails[0]

    def mails(self):
        return self._mails


class FakeSMTPServerThread(threading.Thread):

    def __init__(self, localaddress=('localhost', 9969), remoteaddress=('localhost', 9970)):
        super(FakeSMTPServerThread, self).__init__()
        self.daemon = True
        self.localaddress = localaddress
        self.remoteaddress = remoteaddress
        print 'Running FakeSMTPServer at %(host)s:%(port)d...' % \
                {'host': self.localaddress[0], 'port': self.localaddress[1]}
        self.smtp_server = FakeSMTPServer(self.localaddress, self.remoteaddress)

    def run(self):
        asyncore.loop()


def run_smtp_server(localaddress=('localhost', 9969), remoteaddress=('localhost', 9970)):
    '''
    '''
    print 'Running FakeSMTPServer at %(host)s:%(port)d...' % \
                    {'host': localaddress[0], 'port': localaddress[1]}
    print 'Quit the server with CTRL-C.'
    server = FakeSMTPServer(localaddress, remoteaddress)
    asyncore.loop()


if __name__ == '__main__':
    try:
        run_smtp_server()
    except KeyboardInterrupt:
        print '\nFakeSMTPServer terminated'
