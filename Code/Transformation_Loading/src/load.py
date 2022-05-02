



def load(rdd, bucket_name:str, project_id:str, dataset:str, table:str):
    destination = f'{project_id}.{dataset}.{table}'
    rdd.write.format('bigquery').option('temporaryGcsBucket',
            bucket_name).option('table', destination
                                ).save()
