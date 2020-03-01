import os
import shutil

def gen_voc_data(voc_root):
    if not os.path.isdir('data'):
        os.makedirs('data/train/images')
        os.makedirs('data/train/labels')
        os.makedirs('data/val/images')
        os.makedirs('data/val/labels')
    images_path=voc_root+'JPEGImages/'
    labels_path=voc_root+'SegmentationClass/'
    
    f_train=open(voc_root+'ImageSets/Segmentation/train.txt')
    f_val=open(voc_root+'ImagesSets/Segmentation/val.txt')
    
    for train_name in f_train.readlines():
        image_name=train_name.strip('\n')+'.jpg'
        label_name=train_name.strip('\n')+'.png'
        shutil.copyfile(images_path+image_name,'data/train/images')
        shutil.copyfile(labels_path+label_name,'data/train/labels')
    
    for val_name in f_val.readlines():
        image_name=val_name.strip('\n')+'.jpg'
        label_name=val_name.strip('\n')+'.png'
        shutil.copyfile(images_path+image_name,'data/val/images')
        shutil.copyfile(labels_path+label_name,'data/val/labels')

    shutil.copyfile(voc_root+"ImageSets/Segmentation/train.txt",'data/train.txt')
    shutil.copyfile(voc_root+"ImageSets/Segmentation/val.txt",'data/val.txt')
    shutil.copyfile(voc_root+"ImageSets/Segmentation/trainval.txt",'data/trainval.txt')
    print('success!!')

