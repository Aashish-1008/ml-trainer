
# google-cloud-ml-engine
This repo will train the model on google cloud ml engine & host the model in ml engine.

### Installation
Ludwig has been developed and tested with Python 3 in mind. If you don’t have Python 3 installed, install it by running:

```
# on ubuntu
sudo apt install python3 

# on mac 
brew install python3 
    
```



## Using local python
You can run the code locally

```
JOB_DIR=jobDir
TRAIN_FILE=./data/train/*
EVAL_FILE=./data/eval/*
TRAIN_STEPS=2000

cd  tf-ludwig-google-cloud-ml-engine/

python3.6 -m trainer.task --train-files $TRAIN_FILE \
                       --eval-files $EVAL_FILE \
                       --job-dir $JOB_DIR \
                       --train-steps $TRAIN_STEPS.
'''


```
gsutil cp remote-train local-train

'''
## Using local python
You can run the Keras code locally

```
JOB_DIR=job_dir
TRAIN_FILE=./data/train/*
EVAL_FILE=./data/eval/*
TRAIN_STEPS=2000
python -m trainer.task --train-files $TRAIN_FILE \
                       --eval-files $EVAL_FILE \
                       --job-dir $JOB_DIR \
                       --train-steps $TRAIN_STEPS
```

## Training using gcloud local

You can run Keras training using gcloud locally

```
JOB_DIR=job_dir
TRAIN_STEPS=200
gcloud ml-engine local train --package-path trainer \
                             --module-name trainer.task \
                             -- \
                             --train-files $TRAIN_FILE \
                             --eval-files $EVAL_FILE \
                             --job-dir $JOB_DIR \
                             --train-steps $TRAIN_STEPS \
                             --python-version 3.6 \
                             --runtime-version 1.10 
```

## Prediction using gcloud local
You can run prediction on the SavedModel created from Keras HDF5 model


```
gcloud ml-engine local predict --model-dir=./models/h5/export/1544372069/  --json-instances request.json
```

## Training using Cloud ML Engine

You can train the model on Cloud ML Engine

```
JOB_NAME=flowerv15
REGION=us-east1
JOB_DIR=gs://skyl-dev-ml/aashishdahiya/flowers_aashishdahiya_testV3_20181205_134432/$JOB_NAME

GCS_TRAIN_FILE=gs://skyl-dev-ml/aashishdahiya/flowers_aashishdahiya_testV3_20181205_134432/preproc/train*
GCS_EVAL_FILE=gs://skyl-dev-ml/aashishdahiya/flowers_aashishdahiya_testV3_20181205_134432/preproc/eval*

gcloud ml-engine jobs submit training $JOB_NAME \
                                    --stream-logs \
                                    --runtime-version 1.10 \
                                    --python-version 3.5 \
                                    --job-dir $JOB_DIR \
                                    --package-path trainer \
                                    --module-name trainer.task \
                                    --region $REGION \
                                    -- \
                                    --train-files $GCS_TRAIN_FILE \
                                    --eval-files $GCS_EVAL_FILE \
                                    --train-steps $TRAIN_STEPS
```

## Prediction using Cloud ML Engine
You can perform prediction on Cloud ML Engine by following the steps below.
Create a model on Cloud ML Engine
Export the model binaries
Deploy the model to the prediction service
Run the online prediction

```
MODEL_NAME=skyl_flower
REGION=us-east1
VERSION=v1
MODEL_BINARIES=gs://skyl-dev-ml/aashishdahiya/flowers_aashishdahiya_testV3_20181205_134432/flowerv15/export/1544433235/

gcloud ml-engine models create $MODEL_NAME --regions $REGION
gcloud ml-engine versions create $VERSION --model $MODEL_NAME --origin $MODEL_BINARIES --runtime-version 1.10

gcloud ml-engine predict --model $MODEL_NAME --version v1 --json-instances ./request.json
```