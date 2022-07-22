import os
import shutil

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
