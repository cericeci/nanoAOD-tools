import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

import os
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
import itertools

class splitSMSmasses(Module):
    def __init__(self, pdg1, pdg2):
        self.p1 = pdg1
        self.p2 = pdg2

    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.wrappedOutputTree = wrappedOutputTree
        self.wrappedOutputTree.branch('SMSMassLSP','F')        
        self.wrappedOutputTree.branch('SMSMassNLSP','F')

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    def analyze(self, event):
        parts  = Collection(event, 'GenPart')
        nparts = len(parts)
	m1 = -1
	m2 = -1
	for p in parts:
		if getattr(p, "pdgId") == self.p1: m1 = getattr(p,"mass")
		if getattr(p, "pdgId") == self.p2: m2 = getattr(p,"mass")
 
        self.wrappedOutputTree.fillBranch('SMSMassLSP', m1)
        self.wrappedOutputTree.fillBranch('SMSMassNLSP', m2)
        return True


            
            


# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

 
