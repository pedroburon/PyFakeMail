import BaseHTTPServer
import logging
logger = logging.getLogger(__name__)

class MailHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    
    def do_GET(self):
        logger.debug(self.path)
        self.wfile.write('<!doctype html><html><body><h1>PyFakeMail</h1><ul>')
        

        mails = self.smtp_server.mails() if self.smtp_server else []
        for mail in mails:
            logger.debug(mail)
            self.wfile.write('''
            <li>
                <dl>
                    <dt>peer</dt><dd>%(peer)s</dd>
                    <dt>mailfrom</dt><dd>%(mailfrom)s</dd>
                    <dt>rcpttos</dt><dd>%(rcpttos)s</dd>
                    <dt>data</dt><dd>%(data)s</dd>
                </dl>
            </li>
            ''' % mail)
        self.wfile.write('</ul></body></html>')

