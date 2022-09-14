import json

import config
from data_model import jobs_by_uid, Jobs
from support import extract_job_uid_from_url


def post():
    with open(config.spider_output_filepath, 'r') as all_leaderboards:
        all_leaderboards = json.load(all_leaderboards)
        for lb in all_leaderboards:
            job = jobs_by_uid[extract_job_uid_from_url(lb['url'])]
            for floor in lb['floorsReached']:
                if '200' in floor:
                    job.value.clears += 1

        print("Palace of the Dead Clear Count by Job (All NA Data Centers)")
        print("-----------------------------------------------------------")
        print()
        print("Job,Clears")
        for job in Jobs:
            print(job.name + "," + str(job.value.clears))


if __name__ == '__main__':
    post()
