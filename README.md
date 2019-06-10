# Locking Dance Style Classification
The five video classification methods:

## Requirements

This code requires you have Keras 2 and TensorFlow 1 or greater installed. Please see the `requirements.txt` file. To ensure you're up to date, run:

`pip install -r requirements.txt`

You must also have `ffmpeg` installed in order to extract the video files. If `ffmpeg` isn't in your system path (ie. `which ffmpeg` doesn't return its path, or you're on an OS other than *nix), you'll need to update the path to `ffmpeg` in `data/2_extract_files.py`.

## Getting the data

First, download the dataset from *insert link here.*
Then extract it.
Next, create folders (still in the data folder) with `mkdir train && mkdir test && mkdir sequences && mkdir checkpoints`.

Now you can run the scripts in the data folder to move the videos to the appropriate place, extract their frames and make the CSV file the rest of the code references. You need to run these in order. Example:

`python 1_move_files.py`

`python 2_extract_files.py`

## Extracting features

Before you can run the `lstm`, you need to extract features from the images with the CNN. This is done by running `extract_features.py`. 

## Training models

The CNN-only method (method #1 in the blog post) is run from `train_cnn.py`.

The rest of the models are run from `train.py`. There are configuration options you can set in that file to choose which model you want to run.

The models are all defined in `models.py`. Reference that file to see which models you are able to run in `train.py`.

Training logs are saved to CSV and also to TensorBoard files. To see progress while training, run `tensorboard --logdir=data/logs` from the project root folder.

## Validate
Run validate_rnn.py for validation

## Prediction/Demo
Run demo.py to predict one video input. 
(Note: Video must be in the test folder and must also be preprocessed similar to the train dataset.)

## Methodology Citation
Harvey, M. (2017). Five video classification methods implemented in Keras and TensorFlow [Blog Post]. Retrieved from https://blog.coast.ai/five-video-classification -methods-implemented-in-keras-and-tensorflow-99cad29cc0b5
