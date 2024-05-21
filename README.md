# GCP-deploy

## deploy Google Cloud


### tutorial

https://cloud.google.com/sdk/docs/install-sdk?hl=pt-br

https://www.youtube.com/watch?v=7-s5ugThckY


### To download the Linux file, run the following command:

    curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-473.0.0-linux-x86_64.tar.gz

### To extract the contents of the file to the file system (preferably to the main directory), run the following command: 

    tar -xf google-cloud-cli-473.0.0-linux-x86_64.tar.gz

### Add the gcloud CLI to the path. Run the installation script in the root of the folder you extracted using the following command: 

    ./google-cloud-sdk/install.sh

### This can also be done non-interactively (e.g. with a script) and by providing preferences as flags. To see the available flags, run

    ./google-cloud-sdk/install.sh --help

###  To initialize the gcloud CLI, run the gcloud init command: 

    ./google-cloud-sdk/bin/gcloud init

----------

### How to initialize the gcloud CLI

    gcloud init

## Deploy

    gcloud run deploy --source .





    
