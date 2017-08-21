import os 

def clean():
    dir = "../data/result/"
    try:
        os.rmdir(dir)
        os.mkdir(dir)
    except OSError as ex:
'''
        if ex.errno == errno.ENOTEMPTY:
            print "removing cache"
            shutil.rmtree(dir)
            os.mkdir(dir)
        else:
            print ex.errno
'''
        print ex
