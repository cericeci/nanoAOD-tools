from PhysicsTools.NanoAODTools.postprocessing.datasets.componentContainer import  ComponentContainer


SingleMuon = [
    ComponentContainer('SingleMuon_Run2018B', '/SingleMuon/Run2018B-Nano14Dec2018-v1/NANOAOD'),
    ComponentContainer('SingleMuon_Run2018C', '/SingleMuon/Run2018C-Nano14Dec2018-v1/NANOAOD'),
    ComponentContainer('SingleMuon_Run2018D', '/SingleMuon/Run2018D-Nano14Dec2018_ver2-v1/NANOAOD'),
    ComponentContainer('SingleMuon_Run2018A', '/SingleMuon/Run2018A-Nano14Dec2018-v1/NANOAOD'),
    ]

EGamma=[
    ComponentContainer('EGamma_Run2018B', '/EGamma/Run2018B-Nano14Dec2018-v1/NANOAOD'),
    ComponentContainer('EGamma_Run2018C', '/EGamma/Run2018C-Nano14Dec2018-v1/NANOAOD'),
    ComponentContainer('EGamma_Run2018D', '/EGamma/Run2018D-Nano14Dec2018_ver2-v1/NANOAOD'),
    ComponentContainer('EGamma_Run2018A', '/EGamma/Run2018A-Nano14Dec2018-v1/NANOAOD'),
    ]

MuonEG=[
    ComponentContainer('MuonEG_Run2018B', '/MuonEG/Run2018B-Nano14Dec2018-v1/NANOAOD'),
    ComponentContainer('MuonEG_Run2018C', '/MuonEG/Run2018C-Nano14Dec2018-v1/NANOAOD'),
    ComponentContainer('MuonEG_Run2018D', '/MuonEG/Run2018D-Nano14Dec2018_ver2-v1/NANOAOD'),
    ComponentContainer('MuonEG_Run2018A', '/MuonEG/Run2018A-Nano14Dec2018-v1/NANOAOD'),
    ]

DoubleMuon=[
    ComponentContainer('DoubleMuon_Run2018B', '/DoubleMuon/Run2018B-Nano14Dec2018-v1/NANOAOD'),
    ComponentContainer('DoubleMuon_Run2018C', '/DoubleMuon/Run2018C-Nano14Dec2018-v1/NANOAOD'),
    ComponentContainer('DoubleMuon_Run2018D', '/DoubleMuon/Run2018D-Nano14Dec2018_ver2-v1/NANOAOD'),
    ComponentContainer('DoubleMuon_Run2018A', '/DoubleMuon/Run2018A-Nano14Dec2018-v1/NANOAOD'),
    ]
""" #No longer in 2018!
DoubleElectron=[
    ComponentContainer('DoubleEG_Run2018B', '/DoubleEG/Run2018B-Nano14Dec2018-v1/NANOAOD'), 
    ComponentContainer('DoubleEG_Run2018C', '/DoubleEG/Run2018C-Nano14Dec2018-v1/NANOAOD'), 
    ComponentContainer('DoubleEG_Run2018D', '/DoubleEG/Run2018D-Nano14Dec2018_ver2-v1/NANOAOD'), 
    ComponentContainer('DoubleEG_Run2018A', '/DoubleEG/Run2018A-Nano14Dec2018-v1/NANOAOD'), 
]"""

MET=[
    ComponentContainer('MET_Run2018B', '/MET/Run2018B-Nano14Dec2018-v1/NANOAOD'), 
    ComponentContainer('MET_Run2018C', '/MET/Run2018C-Nano14Dec2018-v1/NANOAOD'), 
    ComponentContainer('MET_Run2018D', '/MET/Run2018D-Nano14Dec2018_ver2-v1/NANOAOD'), 
    ComponentContainer('MET_Run2018A', '/MET/Run2018A-Nano14Dec2018-v1/NANOAOD'), 
]


samples = SingleMuon+EGamma+MuonEG+DoubleMuon+MET #DoubleElectron

for sample in samples:
    sample.options['isData'] = True
