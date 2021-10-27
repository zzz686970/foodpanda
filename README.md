## How to run

```py
## install python packages
pip3 install -r requirements.txt

## install gcloud sdk and authenticate
curl https://sdk.cloud.google.com > install.sh
bash install.sh --disable-prompts
gcloud auth login 

## set project
gcloud config set project ninth-potion-327504

## execute sql query
python3 process_data.py
```

