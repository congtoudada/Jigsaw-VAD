# 文件: clean_dataset
# 作者: 聪头
# 时间: 2023/3/28 23:39
# 描述:

import os
import platform

plat = platform.system().lower()

datasetDir = ""

if plat == 'windows':
    print('windows系统')
    datasetDir = "./dataset/ped2/"
elif plat == 'linux':
    print('linux系统')
    datasetDir = "/root/data1/lzc/dataset/VAD/ped2/"

for phase in ['testing', 'training']:
    datasetDir2 = os.path.join(datasetDir, phase)
    for phaseDirName in os.listdir(datasetDir):
        # 删除杂项
        for videoDirName in os.listdir(os.path.join(datasetDir, phaseDirName)):
            # 重命名文件
            if (phase == 'testing' and videoDirName.__len__() > 2):
                pwd = os.path.join(datasetDir, phaseDirName)
                oldName = videoDirName
                newName = videoDirName[5:]
                os.rename(os.path.join(pwd, oldName), os.path.join(pwd, newName))
            # 清理杂项
            if (videoDirName.startswith(".")):
                os.remove(os.path.join(datasetDir, phaseDirName, videoDirName))

print("数据清理完毕!")