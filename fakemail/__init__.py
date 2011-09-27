import asyncore
import sys
import logging
import BaseHTTPServer
from optparse import OptionParser

from fakemail.smtpserver import FakeSMTPServerThread, FakeSMTPServer
from fakemail.httpserver import MailHandler

def main():
    '''
    Main script
    '''

    parser = OptionParser(usage="usage: %prog [options]")
    parser.add_option('-s', '--smtp', action='store_true', dest='smtp', default=False,
                        help='Just run fake smtp server')
    parser.add_option('-a', '--smtp-host', dest='smtp_host', type='string', default='localhost',
                        help='Set local smtp host')
    parser.add_option('-p', '--smtp-port', dest='smtp_port', type='int', default=9969,
                        help='Set local smtp port')
    parser.add_option('-A', '--http-host', dest='http_host', type='string', default='127.0.0.1',
                        help='Set http host')
    parser.add_option('-P', '--http-port', dest='http_port', type='int', default=9999,
                        help='Set http port')
    parser.add_option('-d', '--debug', dest='debug', default=False)

    (options, args) = parser.parse_args(sys.argv)
    
    if options.debug:
        logging.basicConfig(level=logging.DEBUG, format='%(message)s')
    else:
        logging.basicConfig(level=logging.INFO, format='%(message)s')

    try:
        thread = FakeSMTPServerThread((options.smtp_host, options.smtp_port), ('localhost', 0))
        thread.start()
        if options.smtp:
            options.https_host = 0
        else:
            print 'Running HTTP server at http://%(address)s:%(port)d' % \
                            {'address': options.http_host, 'port': options.http_port}

        MailHandler.smtp_server = thread.smtp_server
        http = BaseHTTPServer.HTTPServer((options.http_host, options.http_port), MailHandler)
        http.serve_forever()

    except KeyboardInterrupt:
        print '\nTerminated'


if __name__ == '__main__':
    main()
