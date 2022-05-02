#!/usr/bin/python
# -*- coding: utf-8 -*-
from pyspark.sql import SparkSession
import os


def transform(bucket_name:str, filename:str, project_id:str, dataset:str, table:str):
    """
            A function that transfoms our json file to a flat csv file.

    Args:
            bucket_name (str): name of the destination bucket 
            filename (str): json filename 
            project_id (str): project id
            dataset (str): name of bigquery dataset
            table (str): name of bigquery table
    """
    spark = SparkSession.builder.master('local[1]'
            ).appName('Ao2SparkTransform').getOrCreate()
    path = os.path.join('gs://', bucket_name, filename)
    dummy = spark.read.option('multiline', 'true').format('json'
            ).load(path)

    qualify = dummy.select(
        'match_id',
        'lobby_id',
        'match_uuid',
        'version',
        'name',
        'num_players',
        'num_slots',
        'average_rating',
        'cheats',
        'full_tech_tree',
        'ending_age',
        'expansion',
        'game_type',
        'has_custom_content',
        'has_password',
        'lock_speed',
        'lock_teams',
        'map_size',
        'map_type',
        'pop',
        'ranked',
        'leaderboard_id',
        'rating_type',
        'resources',
        'rms',
        'scenario',
        'server',
        'shared_exploration',
        'speed',
        'starting_age',
        'team_together',
        'team_positions',
        'treaty_length',
        'turbo',
        'victory',
        'victory_time',
        'visibility',
        'opened',
        'started',
        'finished',
        )
    return qualify
    
