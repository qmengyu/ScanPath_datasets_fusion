import os
from scipy import io
import numpy as np
import scipy.io as scio
image_size = np.array([480, 640])
gtspath_save = "/data/03-scanpath/datasets_new/SALICON/gt_fixations/"
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
    gt_fixations = np.array([gt_fixations[:, 1], gt_fixations[:, 0]])
    gt_fixations = gt_fixations.T - 1  # begin
    gt_fixations = np.array(gt_fixations)
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
    gt_fixations = gt_fixations['gt_fixations']
    gt_fixations = np.array([gt_fixations[:, 1], gt_fixations[:, 0]])
    gt_fixations = gt_fixations.T - 1  # begin
    gt_fixations = np.array(gt_fixations)
    print(index, gt_fixations.shape)
    save_path = os.path.join(gtspath_save, gt_name)
    io.savemat(save_path, {'gt_fixations': gt_fixations, 'image_size': image_size})
