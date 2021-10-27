## Table in Bigquery
```
https://console.cloud.google.com/bigquery?project=ninth-potion-327504&d=foodpanda_home_test

## q1
top5_neareast_port_jurong

## q2
largest_country_ports_with_cargo

## q3
neareast_port_for_call
```


## How to recreate
Output table is already shared in Bigquery, scripts are attached in the zipped folder.

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

