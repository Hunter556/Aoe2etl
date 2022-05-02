
from src import transform as t
from src import load as l

config_filename = '1650931200.json'
bucket_name = 'aoe2spark'
rdd = t.transform(bucket_name, config_filename)
project_id = ""
dataset = ""
table = ""
l.load(rdd,
       bucket_name,
       project_id,
       dataset,
       table)