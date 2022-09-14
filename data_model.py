from enum import Enum


class Job:
    def __init__(self, shortname, uid, clears=0):
        self.shortname = shortname
        self.uid = uid
        self.clears = clears


class Jobs(Enum):
    AST = Job('ast', 'eb7fb1a2664ede39d2d921e0171a20fa7e57eb2b')
    BLMTHM = Job('blmthm', 'f28896f2b4a22b014e3bb85a7f20041452319ff2')
    BRDARC = Job('brdarc', 'f50dbaf7512c54b426b991445ff06a6697f45d2a')
    DNC = Job('dnc', 'baa255d6ec667f5a88920d8968e86a41261d8576')
    DRGLNC = Job('drglnc', 'b16807bd2ef49bd57893c56727a8f61cbaeae008')
    DRK = Job('drk', 'c31f30f41ab1562461262daa74b4d374e633a790')
    GNB = Job('gnb', '1c29ab32bcd60f4ac37827066709fa17c872edca')
    MCH = Job('mch', '773aae6e524e9a497fe3b09c7084af165bef434d')
    MNKPGL = Job('mnkpgl', '46fcce8b2166c8afb1d76f9e1fa3400427c73203')
    NINROG = Job('ninrog', 'e8f417ab2afdd9a1e608cb08f4c7a1ae3fe4a441')
    PLDGLA = Job('pldgla', '125bf9c1198a3a148377efea9c167726d58fa1a5')
    RDM = Job('rdm', '55a98ea6cf180332222184e9fb788a7941a03ec3')
    RPR = Job('rpr', 'c3c6557ad8cc33a73a392f68e45926710496eb13')
    SAM = Job('sam', '7c3485028121b84720df20de7772371d279d097d')
    SCH = Job('sch', '56f91364620add6b8e53c80f0d5d315a246c3b94')
    SGE = Job('sge', '3516b2b3881af781dba74a70f7d3e5d01bb73434')
    SMNACN = Job('smnacn', '9ef51b0f36842b9566f40c5e3de2c55a672e4607')
    WARMRD = Job('warmrd', '741ae8622fa496b4f98b040ff03f623bf46d790f')
    WHMCNJ = Job('whmcnj', '56d60f8dbf527ab9a4f96f2906f044b33e7bd349')


jobs_by_uid = {
    Jobs.AST.value.uid: Jobs.AST,
    Jobs.BRDARC.value.uid: Jobs.BRDARC,
    Jobs.BLMTHM.value.uid: Jobs.BLMTHM,
    Jobs.DNC.value.uid: Jobs.DNC,
    Jobs.DRK.value.uid: Jobs.DRK,
    Jobs.DRGLNC.value.uid: Jobs.DRGLNC,
    Jobs.GNB.value.uid: Jobs.GNB,
    Jobs.MCH.value.uid: Jobs.MCH,
    Jobs.MNKPGL.value.uid: Jobs.MNKPGL,
    Jobs.NINROG.value.uid: Jobs.NINROG,
    Jobs.PLDGLA.value.uid: Jobs.PLDGLA,
    Jobs.RPR.value.uid: Jobs.RPR,
    Jobs.RDM.value.uid: Jobs.RDM,
    Jobs.SGE.value.uid: Jobs.SGE,
    Jobs.SAM.value.uid: Jobs.SAM,
    Jobs.SCH.value.uid: Jobs.SCH,
    Jobs.SMNACN.value.uid: Jobs.SMNACN,
    Jobs.WARMRD.value.uid: Jobs.WARMRD,
    Jobs.WHMCNJ.value.uid: Jobs.WHMCNJ,
}


class DataCenters(Enum):
    AETHER = "Aether"
    CHAOS = "Chaos"
    CRYSTAL = "Crystal"
    ELEMENT = "Elemental"
    GAIA = "Gaia"
    LIGHT = "Light"
    MANA = "Mana"
    MATERIA = "Materia"
    METEOR = "Meteor"
    PRIMAL = "Primal"
