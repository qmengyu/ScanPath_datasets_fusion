import os
from scipy import io
import numpy as np
import scipy.io as scio
import shutil
from PIL import Image
gtspath = '/data/03-scanpath/datasets/OSIE/gt'
gtspath_save = "/data/03-scanpath/datasets_new/OSIE/gts/train"
if not os.path.exists(gtspath_save):
    os.mkdir(gtspath_save)

val_gtspath_save = "/data/03-scanpath/datasets_new/OSIE/gts/val"
if not os.path.exists(val_gtspath_save):
    os.mkdir(val_gtspath_save)

imgs_path = '/data/03-scanpath/datasets/OSIE/images'

imgspath_save = "/data/03-scanpath/datasets_new/OSIE/images/train/"
if not os.path.exists(imgspath_save):
    os.mkdir(imgspath_save)

val_imgspath_save = "/data/03-scanpath/datasets_new/OSIE/images/val/"
if not os.path.exists(val_imgspath_save):
    os.mkdir(val_imgspath_save)
num = 0
train_gt_num = 0
val_gt_num = 0
gtspathdir = os.listdir(gtspath)
gtspathdir.sort()
for index in range(len(gtspathdir)):
    print(index)
    gt_name = gtspathdir[index]
    img_name = gt_name[:-4] + '.jpg'

    gt_path = os.path.join(gtspath, gt_name)
    img_name_path = os.path.join(imgs_path, img_name)

    img = Image.open(img_name_path)
    imgSize = img.size  # 大小/尺寸
    print(imgSize)

    fixations_all = scio.loadmat(gt_path)
    fixations_all = fixations_all['fixations_all']

    gt_fixations = []
    for n in range(len(fixations_all)):
        gt_fixation = fixations_all[n][0]
        gt_fixation = np.array([gt_fixation[:, 1], gt_fixation[:, 0]])
        gt_fixation = gt_fixation.T - 1

        if any(gt_fixation[:, 0] >= imgSize[1]) or any(gt_fixation[:, 0] < 0) \
                or any(gt_fixation[:, 1] >= imgSize[0]) or any(gt_fixation[:, 1] < 0):
            # print("img_size", img_size)
            # print(gt_fixation)
            num += 1

        gt_fixations.append(gt_fixation)
        if index < 560:
            train_gt_num += 1
        else:
            val_gt_num += 1

    gt_fixations = np.array(gt_fixations)
    # print(gt_fixations[0].shape)

    if index < 560:
        img_save_path = os.path.join(imgspath_save, img_name)
        gt_save_path = os.path.join(gtspath_save, gt_name)
    else:
        img_save_path = os.path.join(val_imgspath_save, img_name)
        gt_save_path = os.path.join(val_gtspath_save, gt_name)

    # io.savemat(gt_save_path, {'gt_fixations': gt_fixations})
    # shutil.copy(img_name_path, img_save_path)
print(train_gt_num, 'train_gt_num')
print(val_gt_num, 'val_gt_num')
print(num)