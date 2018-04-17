import shutil
import errno
import subprocess


#copy files to a local folder and print , store gradle dependency information
def parse_gradle(path):
    src = path
    dest = "/gradle_temp"
    try:
        shutil.copytree(src, dest)
    except OSError as e:
        # If the error was caused because the source wasn't a directory
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dest)
        else:
            print 'Directory not copied. Error: %s' % e
    p = subprocess.Popen(['gradle','dependencies'], cwd=dest)
    out, err = p.communicate()
    p.wait()
    print out

