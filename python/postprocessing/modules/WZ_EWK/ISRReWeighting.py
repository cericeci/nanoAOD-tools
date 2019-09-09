import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

import os
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
import itertools

class ISRReWeighting(Module):
    def __init__(self, isrCorrs, gpdgId1, gpdgId2):
        self.isrCorrs = isrCorrs
        self.gpdgId1 = gpdgId1
        self.gpdgId2 = gpdgId2
    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.wrappedOutputTree = wrappedOutputTree
        self.wrappedOutputTree.branch('ISR_pt','F')
        self.wrappedOutputTree.branch('ISR_weight','F')


    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    def analyze(self, event):
        gens = Collection(event, 'GenPart')
	g1 = None
        g2 = None
        for g in gens:
            if abs(g.pdgId) == self.gpdgId1 and g.status == 22:
                g1 = g
            if abs(g.pdgId) == self.gpdgId2 and g.status == 22:
                g2 = g
        ISR_pt = (g1.p4() + g2.p4()).Pt()
        self.wrappedOutputTree.fillBranch('ISR_pt', ISR_pt)
        for k in self.isrCorrs.keys():
            if ISR_pt > k[0] and ISR_pt < k[1]:
                self.wrappedOutputTree.fillBranch('ISR_weight', self.isrCorrs[k])
        return True


            
            


# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

 
