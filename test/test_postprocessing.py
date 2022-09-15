from postprocessing import all_clears_by_job


def test_all_clears_by_job():
    expected = sorted([
        ("AST", 1),
        ("BRDARC", 0),
        ("BLMTHM", 1),
        ("DNC", 3),
        ("DRK", 1),
        ("DRGLNC", 0),
        ("GNB", 0),
        ("MCH", 0),
        ("MNKPGL", 0),
        ("NINROG", 0),
        ("PLDGLA", 0),
        ("RPR", 0),
        ("RDM", 0),
        ("SGE", 0),
        ("SAM", 0),
        ("SCH", 0),
        ("SMNACN", 0),
        ("WARMRD", 0),
        ("WHMCNJ", 2),
    ])

    assert expected == sorted(all_clears_by_job('test/data/all_clears_by_job.json'))
