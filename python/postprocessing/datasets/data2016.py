from PhysicsTools.NanoAODTools.postprocessing.datasets.componentContainer import  ComponentContainer


SingleMuon = [
    ComponentContainer('SingleMuon_Run2016B', '/SingleMuon/Run2016B_ver2-Nano14Dec2018_ver2-v1/NANOAOD'),
    ComponentContainer('SingleMuon_Run2016C', '/SingleMuon/Run2016C-Nano14Dec2018-v1/NANOAOD'),
    ComponentContainer('SingleMuon_Run2016D', '/SingleMuon/Run2016D-Nano14Dec2018-v1/NANOAOD'),
    ComponentContainer('SingleMuon_Run2016E', '/SingleMuon/Run2016E-Nano14Dec2018-v1/NANOAOD'),
    ComponentContainer('SingleMuon_Run2016F', '/SingleMuon/Run2016F-Nano14Dec2018-v1/NANOAOD'),
    ComponentContainer('SingleMuon_Run2016G', '/SingleMuon/Run2016G-Nano14Dec2018-v1/NANOAOD'),
    ComponentContainer('SingleMuon_Run2016H', '/SingleMuon/Run2016H-Nano14Dec2018-v1/NANOAOD'),
    ]
SingleElectron = [
    ComponentContainer('SingleElectron_Run2016B', '/SingleElectron/Run2016B_ver2-Nano14Dec2018_ver2-v1/NANOAOD'),
    ComponentContainer('SingleElectron_Run2016C', '/SingleElectron/Run2016C-Nano14Dec2018-v1/NANOAOD'),
    ComponentContainer('SingleElectron_Run2016D', '/SingleElectron/Run2016D-Nano14Dec2018-v1/NANOAOD'),
    ComponentContainer('SingleElectron_Run2016E', '/SingleElectron/Run2016E-Nano14Dec2018-v1/NANOAOD'),
    ComponentContainer('SingleElectron_Run2016F', '/SingleElectron/Run2016F-Nano14Dec2018-v1/NANOAOD'),
    ComponentContainer('SingleElectron_Run2016G', '/SingleElectron/Run2016G-Nano14Dec2018-v1/NANOAOD'),
    ComponentContainer('SingleElectron_Run2016H', '/SingleElectron/Run2016H-Nano14Dec2018-v1/NANOAOD'),
    ]


MuonEG = [
    ComponentContainer('MuonEG_Run2016B', '/MuonEG/Run2016B_ver2-Nano14Dec2018_ver2-v1/NANOAOD'),
    ComponentContainer('MuonEG_Run2016C', '/MuonEG/Run2016C-Nano14Dec2018-v1/NANOAOD'),
    ComponentContainer('MuonEG_Run2016D', '/MuonEG/Run2016D-Nano14Dec2018-v1/NANOAOD'),
    ComponentContainer('MuonEG_Run2016E', '/MuonEG/Run2016E-Nano14Dec2018-v1/NANOAOD'),
    ComponentContainer('MuonEG_Run2016F', '/MuonEG/Run2016F-Nano14Dec2018-v1/NANOAOD'),
    ComponentContainer('MuonEG_Run2016G', '/MuonEG/Run2016G-Nano14Dec2018-v1/NANOAOD'),
    ComponentContainer('MuonEG_Run2016H', '/MuonEG/Run2016H-Nano14Dec2018-v1/NANOAOD'),
    ]

DoubleMuon = [
    ComponentContainer('DoubleMuon_Run2016B', '/DoubleMuon/Run2016B_ver2-Nano14Dec2018_ver2-v1/NANOAOD'),
    ComponentContainer('DoubleMuon_Run2016C', '/DoubleMuon/Run2016C-Nano14Dec2018-v1/NANOAOD'),
    ComponentContainer('DoubleMuon_Run2016D', '/DoubleMuon/Run2016D-Nano14Dec2018-v1/NANOAOD'),
    ComponentContainer('DoubleMuon_Run2016E', '/DoubleMuon/Run2016E-Nano14Dec2018-v1/NANOAOD'),
    ComponentContainer('DoubleMuon_Run2016F', '/DoubleMuon/Run2016F-Nano14Dec2018-v1/NANOAOD'),
    ComponentContainer('DoubleMuon_Run2016G', '/DoubleMuon/Run2016G-Nano14Dec2018-v1/NANOAOD'),
    ComponentContainer('DoubleMuon_Run2016H', '/DoubleMuon/Run2016H-Nano14Dec2018-v1/NANOAOD'),
    ]

DoubleElectron = [
    ComponentContainer('DoubleEG_Run2016B', '/DoubleEG/Run2016B_ver2-Nano14Dec2018_ver2-v1/NANOAOD'),
    ComponentContainer('DoubleEG_Run2016C', '/DoubleEG/Run2016C-Nano14Dec2018-v1/NANOAOD'),
    ComponentContainer('DoubleEG_Run2016D', '/DoubleEG/Run2016D-Nano14Dec2018-v1/NANOAOD'),
    ComponentContainer('DoubleEG_Run2016E', '/DoubleEG/Run2016E-Nano14Dec2018-v1/NANOAOD'),
    ComponentContainer('DoubleEG_Run2016F', '/DoubleEG/Run2016F-Nano14Dec2018-v1/NANOAOD'),
    ComponentContainer('DoubleEG_Run2016G', '/DoubleEG/Run2016G-Nano14Dec2018-v1/NANOAOD'),
    ComponentContainer('DoubleEG_Run2016H', '/DoubleEG/Run2016H-Nano14Dec2018-v1/NANOAOD'),
    ]

MET = [
    ComponentContainer('MET_Run2016B', '/MET/Run2016B_ver2-Nano14Dec2018_ver2-v1/NANOAOD'),
    ComponentContainer('MET_Run2016C', '/MET/Run2016C-Nano14Dec2018-v1/NANOAOD'),
    ComponentContainer('MET_Run2016D', '/MET/Run2016D-Nano14Dec2018-v1/NANOAOD'),
    ComponentContainer('MET_Run2016E', '/MET/Run2016E-Nano14Dec2018-v1/NANOAOD'),
    ComponentContainer('MET_Run2016F', '/MET/Run2016F-Nano14Dec2018-v1/NANOAOD'),
    ComponentContainer('MET_Run2016G', '/MET/Run2016G-Nano14Dec2018-v1/NANOAOD'),
    ComponentContainer('MET_Run2016H', '/MET/Run2016H-Nano14Dec2018-v1/NANOAOD'),
    ]



samples = SingleMuon #+SingleElectron+MuonEG+DoubleMuon+DoubleElectron+MET

for sample in samples:
    sample.options['isData'] = True
