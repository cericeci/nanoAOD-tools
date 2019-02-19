#!/usr/bin/env python

# Config file defines two things: POSTPROCESSOR and selectedSamples. 
# selectedSamples is read by the submitter to configure the different samples. The submiter should produce a json file with all the sample options. 
# POSTPROCESSOR is read at running time, and configures the modules to run using the json file produced.

import os
import sys
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import * 

import json


from PhysicsTools.NanoAODTools.postprocessing.modules.common.puWeightProducer import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.collectionMerger import collectionMerger
from PhysicsTools.NanoAODTools.postprocessing.modules.ttH.skimNRecoLeps import SkimRecoLeps
from PhysicsTools.NanoAODTools.postprocessing.modules.common.TriggerBitFilter import TriggerBitFilter
from PhysicsTools.NanoAODTools.postprocessing.modules.common.addFlags import AddFlags
from PhysicsTools.NanoAODTools.postprocessing.modules.ttH.objectCleaning import ObjectCleaning

# get the options
from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import getCrabOption


# definition of output (additional skim may be applied in the modules) 
### SKIM 
cut = None

### SLIM FILE
outputSlim = os.environ['CMSSW_BASE']+"/python/PhysicsTools/NanoAODTools/postprocessing/modules/ttH/OutputSlim.txt"
inputSlim  = os.environ['CMSSW_BASE']+"/python/PhysicsTools/NanoAODTools/postprocessing/modules/ttH/InputSlim.txt"


doData=getCrabOption("doData",False)


if 'IS_CRAB' in os.environ or 'IS_RUN' in os.environ:

    from PhysicsTools.NanoAODTools.postprocessing.datasets.triggers_13TeV_DATA2017 import * 


    print '[TTHpostProcessor]: Submission step'
    from PhysicsTools.NanoAODTools.postprocessing.datasets.mc2017    import samples as mcSamples
    from PhysicsTools.NanoAODTools.postprocessing.datasets.data2017  import samples as dataSamples

    
    if doData:
        jsonFile='/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt'
        
        selectedSamples = dataSamples

        DatasetsAndTriggersMap = {}; DatasetsAndVetosMap = {} 
        DatasetsAndTriggersMap["DoubleMuon"     ] = triggers_mumu_iso + triggers_3mu
        DatasetsAndTriggersMap["DoubleEG"       ] = triggers_ee + triggers_3e + triggers_ee_noniso
        DatasetsAndTriggersMap["MuonEG"         ] = triggers_mue + triggers_2mu1e + triggers_2e1mu + triggers_mue_noiso
        DatasetsAndTriggersMap["SingleMuon"     ] = triggers_1mu_iso
        DatasetsAndTriggersMap["SingleElectron" ] = triggers_1e_iso
        DatasetsAndTriggersMap["MET" ] = []
        DatasetsAndTriggersMap["Electron_noOverlapRemov"] = [] 
        
        DatasetsAndVetosMap["DoubleMuon"    ] = []
        DatasetsAndVetosMap["DoubleEG"      ] = DatasetsAndTriggersMap["DoubleMuon"] + DatasetsAndVetosMap["DoubleMuon"] 
        DatasetsAndVetosMap["MuonEG"        ] = DatasetsAndTriggersMap["DoubleEG"  ] + DatasetsAndVetosMap["DoubleEG"  ] 
        DatasetsAndVetosMap["SingleMuon"    ] = DatasetsAndTriggersMap["MuonEG"    ] + DatasetsAndVetosMap["MuonEG"    ] 
        DatasetsAndVetosMap["SingleElectron"] = DatasetsAndTriggersMap["SingleMuon"] + DatasetsAndVetosMap["SingleMuon"] 
        DatasetsAndVetosMap["MET"] = [] 
        DatasetsAndVetosMap["Electron_noOverlapRemov"] = [] 
    
        for sample in selectedSamples:
            jsn = open( jsonFile ,'r')
            sample.options['json'] = json.loads ( jsn.read())
            sample.options['isData'] = True
            jsn.close()
            for smp, trig in DatasetsAndTriggersMap.iteritems():
                if smp in sample.name:
                    sample.options['triggers']     = trig
                    sample.options['vetotriggers'] = DatasetsAndVetosMap[smp]
                    
                    break

    else:
        selectedSamples=mcSamples
        for sample in selectedSamples: sample.options['isData'] = False



## definition of postprocessor 

# postprocessor is only read when we are in running mode 

if 'IS_CRAB' in os.environ or 'IS_RUN' in os.environ:
    try:
        with open('options_sample.json','r') as sampoptjson: 
            sampOpt = json.loads(sampoptjson.read())
            sampoptjson.close()
    except: 
        raise RuntimeError("No options_sample.json found")

    #1) definition of leptons and skim 
    
    # minelpt  = 5
    # minmupt  = 5
    # maxeleta = 2.5
    # maxmueta = 2.4
    
    # isoAndIPCuts = lambda  x : x.miniPFRelIso_all < 0.4  and abs(x.dxy) < 0.05 and abs(x.dz) < 0.1 and x.sip3d < 8 
    
    # susy_ttH_el  = lambda x  : x.pt > minelpt and abs(x.eta) < maxeleta and x.mvaFall17V1noIso_WPL and isoAndIPCuts(x)
    # susy_ttH_mu  = lambda x : x.pt > minmupt and abs(x.eta) < maxmueta  and isoAndIPCuts(x)
    
    # top_el       = lambda x : x.pt > 20 and x.lostHits < 2 and x.cutBased == 4 and x.pfRelIso03_all < 0.0588 # (pf iso larger than the cuts used)
    # top_mu       = lambda x : x.pt > 20 and x.tightId  and x.pfRelIso04_all < 0.4
    
    # goodElec =  lambda x : susy_ttH_el(x) or top_el(x)
    # goodMuon =  lambda x : susy_ttH_mu(x) or top_mu(x)
    
    # goodLepProducer = collectionMerger(input=["Electron","Muon"], output="LepGood",
    #                                    maxObjects=10,
    #                                    selector=dict([("Electron", goodElec),
    #                                                   ("Muon", goodMuon)
    #                                                   ]))

    def _ttH_idEmu_cuts_E3(lep):
        if (abs(lep.pdgId)!=11): return True
        if (lep.hoe>=(0.10-0.00*(abs(lep.deltaEtaSC+lep.eta)>1.479))): return False
        if (lep.eInvMinusPInv<=-0.04): return False
        if (lep.sieie>=(0.011+0.019*(abs(lep.deltaEtaSC+lep.eta)>1.479))): return False
        return True

    def preselectMuon(lep):
        return lep.pt > 5 and abs(lep.eta) < 2.4 and abs(lep.dxy) < 0.05 and abs(lep.dz) < 0.1 and lep.miniPFRelIso_all < 0.4 and lep.sip3d < 8

    def preselectElectron(lep):
        return lep.pt > 7 and abs(lep.eta) < 2.5 and abs(lep.dxy) < 0.05 and abs(lep.dz) < 0.1 and lep.miniPFRelIso_all < 0.4  and lep.sip3d < 8 and lep.mvaFall17V1noIso_WPL and lep.lostHits <=1

    def preselectLepton(lep):
        return preselectElectron(lep) if abs(lep.pdgId) == 11 else preselectMuon(lep)
    
    def clean_and_FO_selection_TTH(lep):
        return lep.conept>10 and lep.jetBTagDeepCSV<0.4941 and (abs(lep.pdgId)!=11 or (_ttH_idEmu_cuts_E3(lep) and lep.convVeto and lep.lostHits==0)\
                                                                    ) \
                                                                    and (lep.mvaTTH>0.90 or \
                                                                             (abs(lep.pdgId)==13 and lep.jetBTagDeepCSV<0.07 and lep.segmentComp>0.3 and 1/(1+lep.jetRelIso)>0.60) or \
                                                                             (abs(lep.pdgId)==11 and lep.jetBTagDeepCSV<0.07 and lep.mvaFall17V1noIso>0.5 and 1/(1+lep.jetRelIso)>0.60) \
                                                                             )

    def _bitFromInt(num, idx):
        # returns the bit in the idx's position of num
        bitMap = "{0:b}".format(num)
        if idx > len(bitMap): return False
        return bool(int(bitMap[-idx]))

    def _FOTauSel(tau):
        return tau.pt > 20 and abs(tau.eta)<2.3 and abs(tau.dxy) < 1000 and abs(tau.dz) < 0.2 and _bitFromInt(tau.idMVAoldDMdR032017v2,2) and tau.idDecayMode

    def conept_TTH(lep):
        if (abs(lep.pdgId)!=11 and abs(lep.pdgId)!=13): return lep.pt
        if (abs(lep.pdgId)!=13 or lep.mediumId>0) and lep.mvaTTH > 0.90: return lep.pt
        else: return 0.90 * lep.pt * (1+lep.jetRelIso)

    objCleaning = ObjectCleaning( looseLeptonSelection = lambda x : preselectLepton(x),
                                  FOLeptonSelection    = lambda x : clean_and_FO_selection_TTH(x),
                                  FOTauSelection       = lambda x : _FOTauSel(x),
                                  jetSelection         = lambda jet: abs(jet.eta)<2.4 and _bitFromInt(jet.jetId,2) and (jet.pt) > 15,
                                  conePt               = lambda x : conept_TTH(x),
                                  )
                                  
    puAutoWeight     = puAutoWeight()
    
    from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles,runsAndLumis


    skimRecoLeps     = SkimRecoLeps(sample.options['isData'] == True, nMinLeps=2)
    mod = [objCleaning ] # goodLepProducer, skimRecoLeps]
    
    if not sample.options['isData']:
        # add pile-up weight before any skim
        mod = [puAutoWeight] + mod
        
        ## add jet met uncertainties
        from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetUncertainties import jetmetUncertainties2017All, jetmetUncertainties2017
        jmeUncert = jetmetUncertainties2017()
        jmeUncert.metBranchName = 'METFixEE2017'
        mod.extend([jmeUncert]) # jetmetUncertainties2017All()
    
        ## add xsec branch
        addFlags = AddFlags([ (('xsec','F'), lambda ev : sampOpt['xsec'] ) ])
        mod.extend([addFlags])
    
    
    if 'triggers' in sampOpt:
        if not 'vetotriggers' in sampOpt:
            raise RuntimeError('[%s]: You have specified trigger requierments, but not veto triggers. Please include them (can be an empty list)')
        triggerBitFilter = TriggerBitFilter( triggers = sampOpt['triggers'],
                                             vetotriggers = sampOpt['vetotriggers'])
        mod = [triggerBitFilter] + mod
    
    
    jsonInput = sampOpt['json'] if 'json' in sampOpt else runsAndLumis()     
    POSTPROCESSOR=PostProcessor(".",inputFiles() if 'IS_CRAB' in os.environ else [],cut,inputSlim,mod,provenance=True,fwkJobReport=True,jsonInput=jsonInput, outputbranchsel=outputSlim)







# def BuildJsonForTesting():

 
#     sampOpt = { 'isData' : True,
#                 'triggers' : [], #triggers_mumu_iso + triggers_3mu , # [],#triggers_ee + triggers_3e+triggers_ee_noniso,
#                 'vetotriggers' : [],#triggers_mumu_iso + triggers_3mu,
#                 'json':   None, # '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt'
#                 'xsec' : 88.,
#                 }

#     optjsonfile = open('options_sample.json','w')
#     optjsonfile.write(json.dumps(sampOpt))
#     optjsonfile.close()

    

    

# def LoadCfgForSubmission():


#     return selectedSamples

#def LoadCfgToRun(inputFile=None):

 #this takes care of converting the input files from CRAB
        
#    return POSTPROCESSOR





# if not __name__ == "__main__": # this is only done when importing

#     if 'IS_CRAB' in os.environ:
#         POSTPROCESSOR = LoadCfgToRun()
#     else:
#         selectedSamples = LoadCfgForSubmission()


# else:


#     BuildJsonForTesting()
#     filepath  = [
#         #'/pool/ciencias/userstorage/sscruz/NanoAOD_test/Run2017C_MuonEG_Nano14Dec2018-v1_F7055783-BE3F-BF4B-83A2-64A73E13EA85.root',
#         #'/pool/ciencias/userstorage/sscruz/NanoAOD_test/SingleMuon_612BB142-CD08-B14D-BA60-2311FA0F2BD2.root',
#         #'/pool/ciencias/userstorage/sscruz/NanoAOD_test/TTbar_4B84BCC5-FE7C-714B-81AD-5A76C3B511FF.root',
#         #'/afs/cern.ch/work/s/sesanche/public/forEdge/test_forsynch_v4.root'
#         'evt_1_70455_65628129.root'
#                   ]


#     outdir = '.'



#     POSTPROCESSOR = LoadCfgToRun(filepath)
#     POSTPROCESSOR.run()
