import os

nums = 0
dirs = os.listdir()    # 获取当前目录下所有的文件夹
cwd = os.path.abspath('.')      # 获取当前目录的绝对路径


def remove_blank_folder():

    for i in dirs:
        global nums
        dirs2 = os.walk(i)    # 获取文件夹下所有的子目录
        dirs2 = list(dirs2)[::-1]    # 倒叙
        for j in dirs2:
            dirs3 = os.path.join(cwd, j[0])    # 获取子目录的绝对路径
            try:
                os.removedirs(dirs3)    # 删除空白子目录
                print('删除空文件夹{}'.format(dirs3))
                nums += 1
            except OSError:
                pass
    print('执行完毕,删除了{}个空文件夹'.format(nums))


if __name__ == '__main__':
    remove_blank_folder()
