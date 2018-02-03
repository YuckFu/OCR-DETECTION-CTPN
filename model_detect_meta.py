# -*- coding: utf-8 -*-
"""
@author: limingfan

"""


# data for train
dir_data_train = './data_generated'
#
dir_images_train = dir_data_train + '/images'
dir_contents_train = dir_data_train + '/contents'

# data for validation
dir_data_valid = './data_test'
#
dir_images_valid = dir_data_valid + '/images'
dir_contents_valid = dir_data_valid + '/contents'
#
dir_results_valid = dir_data_valid + '/results'
#
str_dot_img_ext = '.png'
#
model_dir = './model_detect'
model_name = 'model_detect'
model_pb_file = 'model_detect.pb'
#
anchor_heights = [18, 27, 36, 45, 54, 72]
#
threshold = 0.5
#

#
TRAINING_STEPS = 2**20
#
LEARNING_RATE_BASE = 1e-5
DECAY_RATE = 0.9
DECAY_STAIRCASE = True
DECAY_STEPS = 2**9
MOMENTUM = 0.9
#


