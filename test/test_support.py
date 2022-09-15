import data_model as d
import support


def test_build_url():
    assert support.build_url(d.Jobs.AST.value.uid, d.DataCenters.AETHER.value) == "https://na.finalfantasyxiv.com/lodestone/ranking/deepdungeon/?subtype=eb7fb1a2664ede39d2d921e0171a20fa7e57eb2b&solo_party=solo&dcgroup=Aether"


def test_build_urls():
    # 10 datacenters, 19 jobs
    assert len(support.build_urls()) == 190


def test_extract_job_uid_from_url():
    assert d.Jobs.SMNACN.value.uid == support.extract_job_uid_from_url("https://na.finalfantasyxiv.com/lodestone/ranking/deepdungeon/?subtype=9ef51b0f36842b9566f40c5e3de2c55a672e4607&solo_party=solo&dcgroup=Primal")


def test_extract_datacenter_from_url():
    assert d.DataCenters.METEOR.value == support.extract_datacenter_from_url("https://na.finalfantasyxiv.com/lodestone/ranking/deepdungeon/?subtype=56d60f8dbf527ab9a4f96f2906f044b33e7bd349&solo_party=solo&dcgroup=Meteor")


def test_extract_epoch_from_time_script():
    script = "<script>document.getElementById('datetime-3116d661713').innerHTML = ldst_strftime(1652568559, 'YMDHM');</script>"
    assert 1652568559 == support.extract_epoch_from_time_script(script)


