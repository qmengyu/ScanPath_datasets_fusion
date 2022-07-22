import os
import shutil

#  # SalGAN  ##  ##
imgspath = '/data/03-scanpath/saliency_maps/SALICON/SalGAN/train/'
imgspath_save = "/data/03-scanpath/datasets_new/SALICON/saliency_maps/SalGAN/"
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

val_imgspath = '/data/03-scanpath/saliency_maps/SALICON/SalGAN/val/'

val_imgspathdir = os.listdir(val_imgspath)
val_imgspathdir.sort()
for index in range(len(val_imgspathdir)):
    img_name = val_imgspathdir[index]
    print(index, img_name)
    img_path = os.path.join(val_imgspath, img_name)
    save_path = os.path.join(imgspath_save, img_name)
    shutil.copy(img_path, save_path)


#  # iSEEL  ##  ##
imgspath = '/data/03-scanpath/saliency_maps/SALICON/iSEEL/SALICON_train/'
imgspath_save = "/data/03-scanpath/datasets_new/SALICON/saliency_maps/iSEEL/"
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

val_imgspath = '/data/03-scanpath/saliency_maps/SALICON/iSEEL/SALICON_val/'

val_imgspathdir = os.listdir(val_imgspath)
val_imgspathdir.sort()
for index in range(len(val_imgspathdir)):
    img_name = val_imgspathdir[index]
    print(index, img_name)
    img_path = os.path.join(val_imgspath, img_name)
    save_path = os.path.join(imgspath_save, img_name)
    shutil.copy(img_path, save_path)


#  # MLNet  ##  ##
imgspath = '/data/03-scanpath/saliency_maps/SALICON/MLNet/SALICON_train/'
imgspath_save = "/data/03-scanpath/datasets_new/SALICON/saliency_maps/MLNet/"
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

val_imgspath = '/data/03-scanpath/saliency_maps/SALICON/MLNet/SALICON-MLNET-val/'

val_imgspathdir = os.listdir(val_imgspath)
val_imgspathdir.sort()
for index in range(len(val_imgspathdir)):
    img_name = val_imgspathdir[index]
    print(index, img_name)
    img_path = os.path.join(val_imgspath, img_name)
    save_path = os.path.join(imgspath_save, img_name)
    shutil.copy(img_path, save_path)

