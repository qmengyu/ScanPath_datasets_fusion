import os
from scipy import io
import numpy as np
import scipy.io as scio
import shutil
image_size = np.array([480, 640])
gtspath_save = "/data/03-scanpath/datasets_new/SALICON/gts/"
if not os.path.exists(gtspath_save):
    os.mkdir(gtspath_save)


val_gtspath = '/data/03-scanpath/datasets/SALICON/SALICON/fixations/val_gt_ScanMatch'


val_gtspathdir = os.listdir(val_gtspath)
val_gtspathdir.sort()

for index in range(len(val_gtspathdir)):
    print(index)
    gt_name = val_gtspathdir[index]
    gt_path = os.path.join(val_gtspath, gt_name)
    gt_fixations = scio.loadmat(gt_path)
    gt_fixations = gt_fixations['gt_final']
    # gt_fixations = gt_fixations['gt_fixations']
    gt_fixations = np.array([gt_fixations[:, 1], gt_fixations[:, 0]])
    gt_fixations = gt_fixations.T - 1  # begin
    gt_fixations = np.array([gt_fixations])
    print(gt_fixations.shape)

    save_path = os.path.join(gtspath_save, gt_name)

    io.savemat(save_path, {'gt_fixations': gt_fixations, 'image_size': image_size})


gtspath = '/data/03-scanpath/datasets/SALICON/SALICON/fixations/train_gt_ScanMatch'

gtspathdir = os.listdir(gtspath)
gtspathdir.sort()

for index in range(len(gtspathdir)):
    gt_name = gtspathdir[index]
    gt_path = os.path.join(gtspath, gt_name)
    gt_fixations = scio.loadmat(gt_path)
    # gt_fixations = gt_fixations['gt_final']
    gt_fixations = gt_fixations['gt_fixations']
    gt_fixations = np.array([gt_fixations[:, 1], gt_fixations[:, 0]])
    gt_fixations = gt_fixations.T - 1  # begin
    gt_fixations = np.array([gt_fixations])
    print(index, gt_fixations.shape)
    save_path = os.path.join(gtspath_save, gt_name)
    io.savemat(save_path, {'gt_fixations': gt_fixations, 'image_size': image_size})


imgspath = '/data/03-scanpath/datasets/SALICON/SALICON/images/train/'
imgspath_save = "/data/03-scanpath/datasets_new/SALICON/images/train/"
if not os.path.exists(imgspath_save):
    os.mkdir(imgspath_save)

imgspathdir = os.listdir(imgspath)
imgspathdir.sort()
for index in range(len(imgspathdir)):
    img_name = imgspathdir[index]
    print(index, img_name)
    img_path = os.path.join(imgspath, img_name)
    save_path = os.path.join(imgspath_save, img_name)
    shutil.copy(img_path, save_path)


val_imgspath = '/data/03-scanpath/datasets/SALICON/SALICON/images/val/'
val_imgspath_save = "/data/03-scanpath/datasets_new/SALICON/images/val/"
if not os.path.exists(val_imgspath_save):
    os.mkdir(val_imgspath_save)

val_imgspathdir = os.listdir(val_imgspath)
val_imgspathdir.sort()
for index in range(len(val_imgspathdir)):
    img_name = val_imgspathdir[index]
    print(index, img_name)
    img_path = os.path.join(val_imgspath, img_name)
    if index < 4000:
        save_path = os.path.join(imgspath_save, img_name)
    else:
        save_path = os.path.join(val_imgspath_save, img_name)
    shutil.copy(img_path, save_path)
