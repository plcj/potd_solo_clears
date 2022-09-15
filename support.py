from data_model import DataCenters, Jobs


def build_url(job_uid, dc_name):
    baseurl = 'https://na.finalfantasyxiv.com/lodestone/ranking/deepdungeon/?'

    return baseurl + "subtype=" + job_uid + "&solo_party=solo&dcgroup=" + dc_name


def build_urls():
    urls = list()
    for dc in DataCenters:
        for job in Jobs:
            urls.append(build_url(job.value.uid, dc.value))

    return urls


def extract_job_uid_from_url(url):
    return url.split("subtype=")[1].split("&solo")[0]


def extract_datacenter_from_url(url):
    return url.split("&dcgroup=")[1]


# Times on the leaderboard are populated by a script. The result cannot be selected directly.
def extract_epoch_from_time_script(script):
    return int(script.split("ldst_strftime(")[1].split(",")[0])
