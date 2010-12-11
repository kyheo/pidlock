import unittest

import pidlock

class TestPidlock(unittest.TestCase):

    def setUp(self):
        self._no_perms = '/test_pidlock.pid
        self._perms = '/tmp/test_pidlock.pid

    def test_acquire(self):
        self.assertRaises(pidlock.PermissionDeniedException, pidlock.acquire(self._no_perms))
        self.assertTrue(pidlock.acquire(self._perms))
        self.assertRaises(pidlock.AlreadyAcquireException, pidlock.acquire(self._perms))
        self.assertTrue(pidlock.release())


if __name__ == '__main__':
    unittest.main()
