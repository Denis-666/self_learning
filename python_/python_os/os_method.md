os.sep 可以取代操作系统特定的路径分割符.

os.name 字符串指示你正在使用的平台。比如对于 Windows，它是'nt'，而对于 Linux/Unix 用户，它是'posix'.

os.getcwd()函数得到当前工作目录，即当前 Python 脚本工作的目录路径.

os.getenv()和 os.putenv()函数分别用来读取和设置环境变量.

os.listdir()返回指定目录下的所有文件和目录名.

os.curdir:返回当前目录('.').

os.remove()函数用来删除一个文件.

os.system()函数用来运行 shell 命令.

os.rename()更改文件或目录名.

os.rmdir()删除目录.

os.removedirs()删除多级目录.

os.getloadavg()系统负载，5、10、15 分钟.

os.chmod()更改文件或目录权限.

os.chown()更改文件或目录属主和属组.

os.getuid()当前用户的 uid.

os.getgid()当前用户的 gid

os.uname()系统信息，shell 下的 uname 命令结果组成的元组.

os.chdir(dirname):改变工作目录到 dirname.

os.linesep 字符串给出当前平台使用的行终止符。例如，Windows 使用'\r\n'，Linux 使用'\n'而 Mac 使用'\r'.

os.path.isdir(name):判断 name 是不是一个目录，name 不是目录就返回 false.

os.path.isfile(name):判断 name 是不是一个文件，不存在 name 也返回 false.

os.path.exists(name):判断是否存在文件或目录 name.

os.path.getsize(name):获得文件大小，如果 name 是目录返回 0L.

os.path.abspath(name):获得绝对路径.

os.path.normpath(path):规范 path 字符串形式

os.path.split(name):分割文件名与目录(事实上，如果你完全使用目录，它也会将最后一个目录作为文件名而分离，同时它不会判断文件或目录是否存在)

os.path.splitext():分离文件名与扩展名

os.path.join(path,name):连接目录与文件名或目录

os.path.basename(path):返回文件名

os.path.dirname(path):返回文件路径

pwd 模块常用内容：

pwd.getpwall() 返回/etc/passwd 全部内容

pwd.getpwnam() 返回指定用户在/etc/passwd 中的信息

pwd.getpwuid() 返回指定 uid 对应的用户信息
