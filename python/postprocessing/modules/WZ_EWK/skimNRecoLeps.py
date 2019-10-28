import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

import os
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
import itertools

class SkimRecoLeps(Module):
    def __init__(self, dataFlag):
        self.dataFlag = dataFlag

    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.wrappedOutputTree = wrappedOutputTree
        self.wrappedOutputTree.branch('isData','B')

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    def analyze(self, event):
        leps = Collection(event, 'LepGood')
        taus = Collection(event, 'TauGood') 
        nlepgood = len(leps)
        ntaugood = len(taus)

        self.wrappedOutputTree.fillBranch('isData', self.dataFlag)

        if nlepgood >= 2 or ((ntaugood) >= 2 and nlepgood >= 1): return True

        #self.wrappedOutputTree.fillBranch('prescaleFromSkim', 1)
        return False


            
            


# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

 
