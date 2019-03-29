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
from PhysicsTools.NanoAODTools.postprocessing.modules.WZ_EWK.skimNRecoLeps import SkimRecoLeps
from PhysicsTools.NanoAODTools.postprocessing.modules.common.TriggerBitFilter import TriggerBitFilter
from PhysicsTools.NanoAODTools.postprocessing.modules.common.addFlags import AddFlags

# get the options
from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import getCrabOption


# definition of output (additional skim may be applied in the modules) 
### SKIM 
cut = None

### SLIM FILE
outputSlim = os.environ['CMSSW_BASE']+"/python/PhysicsTools/NanoAODTools/postprocessing/modules/WZ_EWK/OutputSlim.txt"
inputSlim  = os.environ['CMSSW_BASE']+"/python/PhysicsTools/NanoAODTools/postprocessing/modules/WZ_EWK/InputSlim.txt"
jsonFile   = os.environ['CMSSW_BASE']+"/python/PhysicsTools/NanoAODTools/postprocessing/modules/WZ_EWK/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt"

doData=getCrabOption("doData",False)



if True:    
  from PhysicsTools.NanoAODTools.postprocessing.datasets.triggers_13TeV_DATA2018 import * 
  print '[WZpostProcessor]: Submission step'
  from PhysicsTools.NanoAODTools.postprocessing.datasets.mc2018    import samples as mcSamples
  from PhysicsTools.NanoAODTools.postprocessing.datasets.data2018  import samples as dataSamples

  if doData:        
    selectedSamples = dataSamples

    DatasetsAndTriggersMap = {}; DatasetsAndVetosMap = {} 
    DatasetsAndTriggersMap["DoubleMuon"     ] = triggers_mumu_iso + triggers_3mu
    DatasetsAndTriggersMap["MuonEG"         ] = triggers_mue + triggers_2mu1e + triggers_2e1mu + triggers_mue_noiso
    DatasetsAndTriggersMap["EGamma"         ] = triggers_ee + triggers_3e + triggers_ee_noniso +  triggers_1e_iso + triggers_etau
    DatasetsAndTriggersMap["SingleMuon"     ] = triggers_1mu_iso + triggers_mutau
    DatasetsAndTriggersMap["MET" ] = []
    
    DatasetsAndVetosMap["DoubleMuon"    ] = []
    DatasetsAndVetosMap["MuonEG"        ] = DatasetsAndTriggersMap["DoubleMuon"] + DatasetsAndVetosMap["DoubleMuon"] 
    DatasetsAndVetosMap["EGamma"        ] = DatasetsAndTriggersMap["MuonEG"] + DatasetsAndVetosMap["MuonEG"] 
    DatasetsAndVetosMap["SingleMuon"    ] = DatasetsAndTriggersMap["EGamma"] + DatasetsAndVetosMap["EGamma"] 
    DatasetsAndVetosMap["MET"] = [] 
    
    for sample in selectedSamples:
        jsn = open( jsonFile ,'r')
        sample.options['json'] = json.loads ( jsn.read())
        sample.options['isData'] = True
        jsn.close()
        for smp, trig in DatasetsAndTriggersMap.iteritems():
            if smp in sample.name:
                sample.options['triggers']     = trig
                sample.options['vetotriggers'] = DatasetsAndVetosMap[smp]
                if "2018A" in sample.name:
                      sample.options['era'] = 'A'
                if "2018B" in sample.name:
                      sample.options['era'] = 'B'
                if "2018C" in sample.name:
                      sample.options['era'] = 'C'
                if "2018D" in sample.name:
                      sample.options['era'] = 'D'

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

    minelpt  = 5
    minmupt  = 5
    maxeleta = 2.5
    maxmueta = 2.4
    mintaupt = 18
    maxtaueta = 2.3
    
    isoAndIPCuts = lambda  x : x.miniPFRelIso_all < 0.4  and abs(x.dxy) < 0.05 and abs(x.dz) < 0.1 and x.sip3d < 8 
    
    susy_ttH_el  = lambda x  : x.pt > minelpt and abs(x.eta) < maxeleta and x.mvaFall17V1noIso_WPL and isoAndIPCuts(x)
    susy_ttH_mu  = lambda x : x.pt > minmupt and abs(x.eta) < maxmueta  and isoAndIPCuts(x)
    susy_tau_extraloose = lambda x : x.pt > mintaupt and abs(x.eta) < maxtaueta and abs(x.dz) < 0.4

    goodElec =  lambda x : susy_ttH_el(x)
    goodMuon =  lambda x : susy_ttH_mu(x)
    goodTau  =  lambda x : susy_tau_extraloose(x)    

    goodLepProducer = collectionMerger(input=["Electron","Muon"], output="LepGood",
                                       maxObjects=10,
                                       selector=dict([("Electron", goodElec),
                                                      ("Muon", goodMuon)
                                                      ]))

    goodTauProducer = collectionMerger(input=["Tau"], output="TauGood",
                                       maxObjects=10,
                                       selector=dict([("Tau", goodTau)
                                                      ]))

    
    
    from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles,runsAndLumis


    skimRecoLeps     = SkimRecoLeps(sample.options['isData'] == True, nMinLeps=2)
    mod = [goodLepProducer, goodTauProducer, skimRecoLeps]
    
    if not sample.options['isData']:
        # add pile-up weight before any skim
        mod = [puAutoWeight2018()] + mod
        
        ## add jet met uncertainties
        from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetUncertainties import jetmetUncertainties2018All, jetmetUncertainties2018
        jmeUncert = jetmetUncertainties2018()
        jmeUncert.metBranchName = 'MET'
        mod.extend([jmeUncert])
    
        ## add xsec branch
        addFlags = AddFlags([ (('xsec','F'), lambda ev : sampOpt['xsec'] ) ])
        mod.extend([addFlags])
 
    if sample.options['isData']:
        print "ERA:", sample.options['era']
        ## just in case...
        from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetRecalib import jetRecalib2018A, jetRecalib2018B, jetRecalib2018C, jetRecalib2018D
        if sample.options['era'] == 'A':
            jmeUncert = jetRecalib2018A()
        if sample.options['era'] == 'B':
            jmeUncert = jetRecalib2018B()
        if sample.options['era'] == 'C':
            jmeUncert = jetRecalib2018C()
        if sample.options['era'] == 'D':
            jmeUncert = jetRecalib2018D()

        mod.extend([jmeUncert])
        
    
    
    if 'triggers' in sampOpt:
        if not 'vetotriggers' in sampOpt:
            raise RuntimeError('[%s]: You have specified trigger requirements, but not veto triggers. Please include them (can be an empty list)')
        triggerBitFilter = TriggerBitFilter( triggers = sampOpt['triggers'],
                                             vetotriggers = sampOpt['vetotriggers'])
        mod = [triggerBitFilter] + mod
    
    
    jsonInput = sampOpt['json'] if 'json' in sampOpt else runsAndLumis() 
    POSTPROCESSOR=PostProcessor(".",inputFiles() if 'IS_CRAB' in os.environ else [],cut,inputSlim,mod,provenance=True,fwkJobReport=True,jsonInput=jsonInput, outputbranchsel=outputSlim)
