import os
import shutil

gts_paths = ['/data/03-scanpath/datasets_new/SALICON/gts/train',
             '/data/03-scanpath/datasets_new/iSUN/gts/train',
             '/data/03-scanpath/datasets_new/MIT/gts/train',
             '/data/03-scanpath/datasets_new/OSIE/gts/train']
gtspath_save = "/data/03-scanpath/datasets_new/Fusion/gts/train"
if not os.path.exists(gtspath_save):
    os.mkdir(gtspath_save)

val_gts_paths = ['/data/03-scanpath/datasets_new/SALICON/gts/val',
                 '/data/03-scanpath/datasets_new/iSUN/gts/val',
                 '/data/03-scanpath/datasets_new/MIT/gts/val',
                 '/data/03-scanpath/datasets_new/OSIE/gts/val']

val_gtspath_save = "/data/03-scanpath/datasets_new/Fusion/gts/val"
if not os.path.exists(val_gtspath_save):
    os.mkdir(val_gtspath_save)

imgs_paths = ['/data/03-scanpath/datasets_new/SALICON/images/train',
              '/data/03-scanpath/datasets_new/iSUN/images/train',
              '/data/03-scanpath/datasets_new/MIT/images/train',
              '/data/03-scanpath/datasets_new/OSIE/images/train']

imgspath_save = "/data/03-scanpath/datasets_new/Fusion/images/train/"
if not os.path.exists(imgspath_save):
    os.mkdir(imgspath_save)

val_imgs_paths = ['/data/03-scanpath/datasets_new/SALICON/images/val',
                  '/data/03-scanpath/datasets_new/iSUN/images/val',
                  '/data/03-scanpath/datasets_new/MIT/images/val',
                  '/data/03-scanpath/datasets_new/OSIE/images/val']

val_imgspath_save = "/data/03-scanpath/datasets_new/Fusion/images/val/"
if not os.path.exists(val_imgspath_save):
    os.mkdir(val_imgspath_save)

for gts_path in gts_paths:
    gtspathdir = os.listdir(gts_path)
    for index in range(len(gtspathdir)):
        print(index)
        gt_name = gtspathdir[index]
        gt_path = os.path.join(gts_path, gt_name)
        gt_save_path = os.path.join(gtspath_save, gt_name)
        shutil.copy(gt_path, gt_save_path)

for val_gts_path in val_gts_paths:
    val_gtspathdir = os.listdir(val_gts_path)
    for index in range(len(val_gtspathdir)):
        print(index)
        val_gt_name = val_gtspathdir[index]
        val_gt_path = os.path.join(val_gts_path, val_gt_name)
        val_gt_save_path = os.path.join(val_gtspath_save, val_gt_name)
        shutil.copy(val_gt_path, val_gt_save_path)

for imgs_path in imgs_paths:
    imgspathdir = os.listdir(imgs_path)
    for index in range(len(imgspathdir)):
        print(index)
        img_name = imgspathdir[index]
        img_path = os.path.join(imgs_path, img_name)
        img_save_path = os.path.join(imgspath_save, img_name)
        shutil.copy(img_path, img_save_path)


for val_imgs_path in val_imgs_paths:
    val_imgspathdir = os.listdir(val_imgs_path)
    for index in range(len(val_imgspathdir)):
        print(index)
        val_img_name = val_imgspathdir[index]
        val_img_path = os.path.join(val_imgs_path, val_img_name)
        val_img_save_path = os.path.join(val_imgspath_save, val_img_name)
        shutil.copy(val_img_path, val_img_save_path)
