【Linux】Linux 常用操作命令
概述

命令属于死东西，属于 多用多会，不用就忘 的知识，孰能生巧；

Tab 键 可以实现 自动补全 和提示，要合理使用；

history 命令可以显示历史执行记录，或者使用 方向键 来切换前后执行过的命令；

# 显示目录内容

ls （list files）命令：用于显示指定工作目录下之内容（列出目前工作目录所含之文件及子目录)。

-a 显示所有文件及目录 (.开头的隐藏文件也会列出)

-l 除文件名称外，亦将文件型态、权限、拥有者、文件大小等资讯详细列出 注意 ls -l = ll

ls path

ls -a path # 查看所有文件 包括隐藏文件

ls -l =ll # 查看文件详细信息 包括权限 类型 时间 大小等

ll -h path # 表示以人性化的显示内容

ll _ # _ 通配符表示任意字符 ? 表示有且只有一个字符

# 切换目录

cd （change directory）命令：用于切换当前工作目录。切换的路径可为绝对路径或相对路径。若

路径省略，则

变换至使用者的 home 目录 。

~ 也表示为 home 目录的意思

. 则是表示目前所在的目录

.. 则表示目前目录位置的上一层目录

pwd # 查看自己当前所在目录

cd path # 注意自己写的是相对还是绝对的 还可以结合特殊符

号使用

cd ./

cd /

cd ../

cd ~

创建、删除

mkdir （make directory）命令：用于创建目录。

-p 确保父目录名称存在，不存在的就建一个。

touch 命令：创建一个空文件，无任何内容。

rm （remove）命令：用于删除一个文件或者目录。

-f 强制直接删除，无需用户确认。

-r 将目录及以下所有递归逐一删除。

[root@node1 ~] # mkdir /a/b/c

mkdir: cannot create directory ‘ /a/b/c ’ : No such file or directory

[root@node1 ~] # mkdir -p /a/b/c

[root@node1 ~] # rm -rf /a/b/c

[root@node1 ~] # rm -rf /a

-f # 强制删除 不给与提示

-r # 递归删除 针对文件夹

-rf # 杀伤力极大 问问自己在干什么

坐牢眼： rm -rf /\*

复制、移动

cp （copy file）命令：用于复制文件或目录。

-r ：若给出的源文件是一个目录文件，此时将复制该目录下所有的子目录和文件。

mv （move file）命令：用来为文件或目录改名、或将文件或目录移入其它位置。

cp [options] source... directory

mv source_file ( 文件 ) dest_file ( 文件 ) # 将源文件名 source_file 改为目标文件名 dest_file

mv source_file ( 文件 ) dest_directory ( 目录 ) # 将文件 source_file 移动到目标目录 dest_directory 中

mv source_directory ( 目录 ) dest_directory ( 目录 ) # 目录名 dest_directory 已存在，将

source_directory 移动到目录名 dest_directory 中；目录名 dest_directory 不存在则

source_directory 改名为目录名 dest_directory

mv source_directory ( 目录 ) dest_file ( 文件 ) # 出错

# 文件内容查看

cat （concatenate）命令：用于连接文件并打印到标准输出设备如 console 控制台上。适合小文件

内容查看。

more 命令：类似 cat，不过会以一页一页的形式显示，更方便使用者逐页阅读，翻页结束自动退

出。适合大文件

查看。按 space 键翻下一页，按 b 往回（back）上一页

tail 命令：用于查看文件的结尾部分的内容。

-n 用于显示行数，默认为 10，即显示 10 行的内容。

-f 用于 实时显示文件动态追加的内容。会把文件里的最尾部的内容显示在屏幕上，并且不断刷新，

只要 文件有更新，就可以看到最新的文件内容。

其他

| 管道命令：将前一个命令执行的结果作为内容交给下一个命令处理。可以形成多级管道操作。

命令 1|命令 2 可以将命令 1 的结果通过命令 2 作进一步的处理

echo 命令：用于内容的输出，将 内容输出到 console 控制台 上。 echo string

[root@node1 ~] # ls

1.txt anaconda-ks.cfg hello lrzsz-0.12.20.tar.gz test test.file

[root@node1 ~] # ls | grep ^t

test

test.file

# 相当于 print 将内容输出 console 控制台

[root@node1 test] # echo 111

111

[root@node1 test] # echo "hello "

hello

解压压缩命令

tar （tape archive ）命令：常用于备份文件。是用来建立，还原备份文件的工具程序，它可以加

入，解开备份文件内 的文件。

-c 或--create 建立新的备份文件。

-x 或--extract 或--get 从备份文件中还原文件。

-v 或--verbose 显示指令执行过程。

-f <备份文件>或--file=<备份文件> 指定备份文件。

# tar cvf 打包名 .tar 文件或者目录

[root@node1 test] # ll

-rw-r--r-- 1 root root 0 Aug 10 19:27 1.txt

-rw-r--r-- 1 root root 0 Aug 10 19:27 2.txt

[root@node1 test] # tar -cvf test.tar 1.txt 2.txt

1.txt

2.txt

[root@node1 test] # ll

-rw-r--r-- 1 root root 10240 Aug 10 19:28 1.txt

-rw-r--r-- 1 root root 0 Aug 10 19:27 2.txt

-rw-r--r-- 1 root root 20480 Aug 10 19:28 test.tar

# tar xvf 打包名 .tar

# tar xvf 打包名 .tar -C 指定解包目录

[root@node1 test] # ll

-rw-r--r-- 1 root root 20480 Aug 10 19:28 test.tar

[root@node1 test] # tar xvf test.tar

1.txt

2.txt

[root@node1 test] # ll

-rw-r--r-- 1 root root 10240 Aug 10 19:28 1.txt

-rw-r--r-- 1 root root 0 Aug 10 19:27 2.txt

-rw-r--r-- 1 root root 20480 Aug 10 19:28 test.tar

在打包备份或者解包的过程中，可以通过 指定压缩算法 ，对打包的文件进行压缩，解压的时候也需

要指定相应的算法。

-z 或--gzip 或--ungzip 通过 gzip 指令处理备份文件。

最重要的搭配： tar -zxvf xxxxx.tar.gz

[root@node1 test] # ll

-rw-r--r-- 1 root root 10240 Aug 10 19:28 1.txt

-rw-r--r-- 1 root root 0 Aug 10 19:27 2.txt

[root@node1 test] # tar zcvf test.tar.gz 1.txt 2.txt

[root@node1 test] # tar zcvf test.tgz 1.txt 2.txt

[root@node1 test] # ll

-rw-r--r-- 1 root root 10240 Aug 10 19:28 1.txt

-rw-r--r-- 1 root root 0 Aug 10 19:27 2.txt

-rw-r--r-- 1 root root 142 Aug 10 19:35 test.tar.gz

-rw-r--r-- 1 root root 142 Aug 10 19:35 test.tgz

[root@node1 test] # tar zxvf test.tar.gz # 解压到当前目录

1.txt

2.txt

[root@node1 test] # tar zxvf test.tar.gz -C /root/ #-C 参数

可以设定解压到指定目录

1.txt

2.txt

# 时间、日期查看

date 命令：用来显示或设定系统的日期与时间，在显示方面，使用者可以设定欲显示的格式，格式

设定为一个加号

后接数个标记。

cal （calendar）命令：用于用于显示当前或者指定日期的公历。

[root@node1 linux02] # date

Tue May 18 14:44:13 CST 2021

[root@node1 linux02] # date +"%Y-%m-%d %H:%M:%S"

2021-05-18 14:44:53

[root@node1 linux02] # cal

May 2021

Su Mo Tu We Th Fr Sa

1

2 3 4 5 6 7 8

9 10 11 12 13 14 15

16 17 18 19 20 21 22

23 24 25 26 27 28 29

30 31

# 内存、磁盘用率查看

free 命令：用于显示内存状态。会显示内存的使用情况，包括实体内存，虚拟的交换文件内存，共

享内存区段，以 及系统核心使用的缓冲区等。

df （英文全拼：disk free）命令：用于显示目前在 Linux 系统上的文件系统磁盘使用情况统计。

[root@node1 linux02] # df -h

Filesystem Size Used Avail Use% Mounted on

devtmpfs 1.9G 0 1.9G 0% /dev

tmpfs 1.9G 0 1.9G 0% /dev/shm

tmpfs 1.9G 12M 1.9G 1% /run

tmpfs 1.9G 0 1.9G 0% /sys/fs/cgroup

/dev/mapper/centos-root 38G 1.5G 36G 5% / # 重点关注这一行

/dev/sda1 1014M 152M 863M 15% /boot

/dev/mapper/centos-home 19G 33M 19G 1% /home

tmpfs 378M 0 378M 0% /run/user/0

tmpfs 378M 0 378M 0% /run/user/1000

# 内存使用情况

[root@node1 linux02] # free -h

total used free shared buff/cache available

Mem: 3.7G 257M 3.0G 11M 467M 3.2G

Swap: 3.9G 0B 3.9G

进程查看

ps （英文全拼：process status）命令：用于显示当前进程的状态，类似于 windows 的任务管理器。

jps 命令：这是 JDK 自带的命令，专门用于查看本机运行的 java 进程情况。
