import shlex
from subprocess import Popen, PIPE

def system(cmd):
    """
    Execute the external command and get its exit code, stdout and stderr.
    Based on https://stackoverflow.com/a/21000308
    
    Example:
        code, stdout, stderr = system('ls -l')   
        print('code = %d\nstderr = %s\nstdout = %s' % (code,stderr,stdout))

    """
    try:
        args = shlex.split(cmd)
        proc = Popen(args, stdout=PIPE, stderr=PIPE)
        out, err = proc.communicate()
        exitcode = proc.returncode
        return exitcode, out.decode(), err.decode()
    except OSError as e:
        msg = "Execution failed: " + cmd + "\n" + e[1]
        raise OSError(msg)
