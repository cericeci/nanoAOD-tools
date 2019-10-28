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
from PhysicsTools.NanoAODTools.postprocessing.modules.WZ_EWK.splitSMSmasses import splitSMSmasses
from PhysicsTools.NanoAODTools.postprocessing.modules.WZ_EWK.ISRReWeighting import ISRReWeighting
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
jsonFile   = os.environ['CMSSW_BASE']+"/python/PhysicsTools/NanoAODTools/postprocessing/modules/WZ_EWK/Cert_271036-284044_13TeV_ReReco_07Aug2017_Collisions16_JSON.txt"




if True:    
  print '[WZpostProcessor]: Submission step'
  from PhysicsTools.NanoAODTools.postprocessing.datasets.triggers_13TeV_DATA2016 import * 
  from PhysicsTools.NanoAODTools.postprocessing.datasets.mc2016    import samples as mcSamples
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
    print "is data", sample.options['isData']
    print sample.options
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


    skimRecoLeps     = SkimRecoLeps(sample.options['isData'] == True)
    splitMass        = splitSMSmasses(1000022,1000023) #N1/N2
    ISRReweight      = ISRReWeighting({(0,50):1, (50,100):1.052, (100,150):1.179, (150,200):1.150, (200,300): 1.057, (300,400): 1.000, (400,600):0.912, (600,30000): 0.783},1000024,1000023)
    mod = [goodLepProducer, goodTauProducer, skimRecoLeps, splitMass, ISRReweight]
    
    if not sample.options['isData']:
        # add pile-up weight before any skim
        mod = [puWeight()] + mod
        
        ## add jet met uncertainties
        from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetUncertainties import *
        jmeUncert = jetmetUncertaintiesFast2016()
        jmeUncert.metBranchName = 'MET'
        mod.extend([jmeUncert])

        ## add xsec branch
        addFlags = AddFlags([ (('xsec','F'), lambda ev : 1 ) ])
        mod.extend([addFlags])
 
        
    
    
    if 'triggers' in sampOpt:
        if not 'vetotriggers' in sampOpt:
            raise RuntimeError('[%s]: You have specified trigger requirements, but not veto triggers. Please include them (can be an empty list)')
        triggerBitFilter = TriggerBitFilter( triggers = sampOpt['triggers'],
                                             vetotriggers = sampOpt['vetotriggers'])
        mod = [triggerBitFilter] + mod
    
    
    jsonInput = sampOpt['json'] if 'json' in sampOpt else runsAndLumis() 
    POSTPROCESSOR=PostProcessor(".",inputFiles() if 'IS_CRAB' in os.environ else [],cut,inputSlim,mod,provenance=True,fwkJobReport=True,jsonInput=jsonInput, outputbranchsel=outputSlim, SMSMasses=[1000022,1000023], doISR=[1000024,1000023])
