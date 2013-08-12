from unittest.mock import Mock, patch
import unittest


class BodyRequiredException(Exception):
    pass


class EmailService(object):

    def send(self, to, subject, body, bcc=[]):
        if not body:
            return False
        return True

    def send_warning(self, body):
        if not self.send('admins@mysite.com', 'WARNING!', body):
            self.send_error(body)
        else:
            return True

    def send_error(self, body):
        return self.send('admins@mysite.com', 'ERROR!', body)


class TestMocks(unittest.TestCase):

    def setUp(self):
        self.emailer = EmailService()

    def test_send_error_calls_send_with_correct_params(self):
        '''
        assert self.emailer.send was called with certain params
        '''

        self.emailer.send = Mock()

        self.fail()

    def test_send_warning_calls_send_with_correct_params(self):
        '''
        This test should already pass
        '''
        self.emailer.send = Mock(return_value=True)
        self.emailer.send_warning('body')
        self.emailer.send.assert_called_with('admins@mysite.com', 'WARNING!', 'body')

    def test_send_warning_should_send_error_if_false(self):
        '''
        self.emailer.send should return false using a Mock
        so email_error is called with correct args
        '''

        self.fail()

if __name__ == '__main__':
    unittest.main(verbosity=2)
