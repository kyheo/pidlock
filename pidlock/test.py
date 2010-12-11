import unittest

import pidlock

class TestPidlock(unittest.TestCase):

    def setUp(self):
        self._no_perms = '/test_pidlock.pid'
        self._perms = '/tmp/test_pidlock.pid'

    def test_acquire(self):
        pl = pidlock.Pidlock.acquire(self._perms)
        self.assertNotEqual(pl, None)
        self.assertEqual(pl.__class__.__name__, pidlock.Pidlock.__name__)
        pl.release()

    def test_acquire_no_perm(self):
        self.assertRaises(IOError, pidlock.Pidlock.acquire, self._no_perms)
        try:
            pl = pidlock.Pidlock.acquire(self._no_perms)
        except IOError, e:
            self.assertEqual(e.errno, 13)
            self.assertEqual(e.strerror, 'Permission denied')

    def test_acquire_twice(self):
        pl = pidlock.Pidlock.acquire(self._perms)
        self.assertRaises(pidlock.AlreadyAcquireException, \
            pidlock.Pidlock.acquire, self._perms)
        pl.release()


if __name__ == '__main__':
    unittest.main()
