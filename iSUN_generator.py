import os
from scipy import io
import numpy as np
import scipy.io as scio
import shutil
mat_path = '/data/03-scanpath/datasets/iSUN/training.mat'
imgs_path = '/data/03-scanpath/datasets/iSUN/images'

gt_save = "/data/03-scanpath/datasets_new/iSUN/gts/train"
if not os.path.exists(gt_save):
    os.mkdir(gt_save)

val_gt_save = "/data/03-scanpath/datasets_new/iSUN/gts/val"
if not os.path.exists(val_gt_save):
    os.mkdir(val_gt_save)

imgspath_save = "/data/03-scanpath/datasets_new/iSUN/images/train/"
if not os.path.exists(imgspath_save):
    os.mkdir(imgspath_save)


val_imgspath_save = "/data/03-scanpath/datasets_new/iSUN/images/val/"
if not os.path.exists(val_imgspath_save):
    os.mkdir(val_imgspath_save)


mat = scio.loadmat(mat_path)
mat = mat['training']
num = 0
train_gt_num = 0
val_gt_num = 0
for index in range(6000):
    print(index)
    gt_name = mat[index][0][0][0] + '.mat'
    img_name = mat[index][0][0][0] + '.jpg'
    img_name_path = os.path.join(imgs_path, img_name)
    img_size = mat[index][0][1][0]

    gt_fixations = []
    for n in range(len(mat[index][0][3][0])):
        gt_fixation = mat[index][0][3][0][n][2]
        gt_fixation = np.array([gt_fixation[:, 1], gt_fixation[:, 0]])
        gt_fixation = gt_fixation.T - 1

        if any(gt_fixation[:, 0] > img_size[0]) or any(gt_fixation[:, 0] < 0) \
                or any(gt_fixation[:, 1] > img_size[1]) or any(gt_fixation[:, 1] < 0):
            # print("img_size", img_size)
            # print(gt_fixation)
            num += 1
        else:
            gt_fixations.append(gt_fixation)
            if index < 5000:
                train_gt_num += 1
            else:
                val_gt_num += 1

    gt_fixations = np.array(gt_fixations)
    # print(gt_fixations.shape)
    if index < 5000:
        img_save_path = os.path.join(imgspath_save, img_name)
        gt_save_path = os.path.join(gt_save, gt_name)
    else:
        img_save_path = os.path.join(val_imgspath_save, img_name)
        gt_save_path = os.path.join(val_gt_save, gt_name)

    # io.savemat(gt_save_path, {'gt_fixations': gt_fixations, 'image_size': img_size})
    # shutil.copy(img_name_path, img_save_path)
print(num)
print(train_gt_num, 'train_gt_num')
print(val_gt_num, 'val_gt_num')
