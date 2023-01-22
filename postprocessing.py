import json

import config
import pandas as pd
from data_model import jobs_by_uid, Jobs, DeepDungeons
from support import extract_job_uid_from_url


def all_clears_by_job(input_filepath=config.spider_output_filepath):
    with open(input_filepath, 'r') as all_leaders:
        all_leaders = json.load(all_leaders)
        for leader in all_leaders:
            if config.dungeon.value.name is DeepDungeons.POTD.value.name:
                if '200' in leader['floor']:
                    job = jobs_by_uid[extract_job_uid_from_url(leader['url'])]
                    job.value.clears += 1
            else:
                if '100' in leader['floor']:
                    job = jobs_by_uid[extract_job_uid_from_url(leader['url'])]
                    job.value.clears += 1

    clears = list()
    for job in Jobs:
        clears.append((job.name, job.value.clears))

    return clears


def json_to_csv(input_filepath=config.spider_output_filepath):
    columns = (
        'job',
        'datacenter',
        'url',
        'rank',
        'name',
        'world',
        'score',
        'floor',
        'utc-time',
    )

    dfs = list()
    print(input_filepath)
    dfs.append(pd.read_json(input_filepath))
    pd.concat(dfs).to_csv(input_filepath + '.csv', columns=columns)
