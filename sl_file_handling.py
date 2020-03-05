import os
import shutil
from os.path import join


def func(src, dst):
    print("当前平台下文件路径分隔符: %s ." % os.sep)  # 显示当前平台下文件路径分隔符
    # fileDir = "E:" + os.sep + "test"
    # fileDir = os.sep.join(["E:", "test"])  # 以分隔符连接路径名
    total_count = 0
    total_count_nocopy = 0

    for root, dirs, files in os.walk(src):
        # print('the path is ...')
        # print(root)
        # print(root, "####")
        # print('the current directories under current directory :')
        # print(dirs)
        print("the files in current directory %s :" % root)
        # print(files)

        # 计数
        count = 0
        count_nocopy = 0

        for name in files:
            # print(join(root, name))
            # 获取文件名，后缀
            filename, fileType = os.path.splitext(join(root, name))
            # print(type)

            # 只处理ＪＰＧ文件
            if fileType != '.jpg' and fileType != '.JPG':
                print("文件　%s　已跳过！" % join(root, name))
                count_nocopy += 1
                continue

            # shutil.copy(join(root, name), dst)
            if os.path.exists(join(dst, name)):
                count_nocopy += 1
                print("文件　%s　已存在,复制跳过！" % join(dst, name))
            else:
                shutil.move(join(root, name), dst)
                print("文件　%s　已复制到目录　%s ！" % (join(root, name), dst))
                count = count + 1

        print("复制文件数： %s " % str(count))
        print("跳过文件数： %s " % str(count_nocopy))
        print(" ")
        total_count = total_count + count
        total_count_nocopy += count_nocopy

    print("总复制文件数： %s " % str(total_count))
    print("总跳过文件数： %s " % str(total_count_nocopy))
    return



if __name__ == "__main__":
    srcFileDir = '/media/shane/My_Database/相册/'
    # trgFileDir = '/tmp/mi8_u/'  # type: str
    trgFileDir = '/media/shane/My_Database/MI8BK/'

    if not os.path.exists(trgFileDir):
        os.mkdir(trgFileDir)

    func(srcFileDir, trgFileDir)
