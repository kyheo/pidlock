import os

class PermissionDeniedException(Exception):
    pass

class AlreadyAcquireException(Exception):
    pass


class Pidlock(object):

    @classmethod
    def acquire(cls, file):
        locked = True
        #Check if pid_file exists
        if os.access(file, os.F_OK):
            fp = open(file, 'r')
            fp.seek(0)
            old_pid = fp.readline()
            fp.close()
            if os.path.exists('/proc/%s' % (old_pid,)):
                locked = False
            else:
                os.remove(file)
        
        if locked:
            fp = open(file, 'w')
            fp.write("%s" % (os.getpid()))
            fp.close()
            pl = Pidlock(file)
            return pl
        else:
            raise AlreadyAcquireException(file)


    def __init__(self, file):
        self._file = file


    def release(self):
        return os.remove(self._file)
