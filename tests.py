import os
import server
import unittest


class DHTestCase(unittest.TestCase):
    def setUp(self):
        server.app.config['TESTING'] = True
        self.app = server.app.test_client()

    def test_key_match(self):
        client_secret = 999
        common_public = int(self.app.get('/common_base').data)

        public_mixed = pow(2, client_secret, common_public)

        server_common = int(self.app.get('/public/%d' % public_mixed).data)

        common_secret = pow(server_common, client_secret, common_public)

        check = self.app.get('/check/%d' % common_secret)

        assert 'secret matches' in str(check.data)


if __name__ == '__main__':
    unittest.main()
