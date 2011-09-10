import os

class AlreadyAcquireException(Exception):
    pass


class Pidlock(object):

    @classmethod
    def acquire(cls, file_):
        locked = True
        #Check if pid_file exists
        if os.access(file_, os.F_OK):
            fp = open(file_, 'r')
            fp.seek(0)
            old_pid = fp.readline()
            fp.close()
            if os.path.exists('/proc/%s' % (old_pid,)):
                locked = False
            else:
                os.remove(file)
        
        if locked:
            fp = open(file_, 'w')
            fp.write("%s" % (os.getpid()))
            fp.close()
            pl = Pidlock(file_)
            return pl
        else:
            raise AlreadyAcquireException(file_)


    def __init__(self, file_):
        self._file = file_


    def release(self):
        return os.remove(self._file)
