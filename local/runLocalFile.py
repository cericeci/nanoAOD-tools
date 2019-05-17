import getpass
import os
import sys

import imp, os, json
from optparse import OptionParser,OptionGroup

parser = OptionParser()
g1 = OptionGroup(parser,"Analysis options")
g1.add_option("-c", "--cfg-file", dest="cfg_file", help="Config file containing PostProcessor instance", default="")
parser.add_option_group(g1)
g1.add_option("-o", "--option", dest="extraOptions", type="string", action="append", default=[], help="options to use for task preparation and in remote jobs")

(options,args) = parser.parse_args()


# global options 
from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import _crabGlobalOptions
os.environ['IS_RUN']="true"
for opt in options.extraOptions:
    if "=" in opt:
        (key,val) = opt.split("=",1)
        _crabGlobalOptions[key] = val
    else:
        _crabGlobalOptions[opt] = True
_crabGlobalOptions["isCrab"] = True
optjsonfile = open('options.json','w')
optjsonfile.write(json.dumps(_crabGlobalOptions))
optjsonfile.close()

## create dummy sample json to run locally
options_sample = open('options_sample.json','w')

sampOpt = { 'isData' : True,
            'triggers' : [ 'HLT_IsoMu24', 'HLT_IsoMu24_eta2p1', 'HLT_IsoMu27'], #[triggers_mumu_iso + triggers_3mu] , # [],#triggers_ee + triggers_3e+triggers_ee_noniso,
            'vetotriggers' : [],#triggers_mumu_iso + triggers_3mu,
            'json':   "/afs/cern.ch/work/c/cericeci/private/nanoAOD/CMSSW_10_2_0/src/PhysicsTools/NanoAODTools/python/postprocessing/modules/WZ_EWK/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt", 
            'era': 'A'                                                                                             
            }                                                                                                          


options_sample.write(json.dumps( sampOpt))
options_sample.close()



handle = open(options.cfg_file,'r')
cfo = imp.load_source(options.cfg_file.split('/')[-1].rstrip('.py'), options.cfg_file, handle)
#cfo.POSTPROCESSOR.inputFiles =   ['/afs/cern.ch/work/s/sesanche/public/forEdge/test_forsynch_v4.root'] # #
#cfo.POSTPROCESSOR.inputFiles =   ['E9FF967E-2341-9D48-99B1-37F7F6E01606.root'] #ZZZ file
#cfo.POSTPROCESSOR.inputFiles =   ['E9FF967E-2341-9D48-99B1-37F7F6E01606.root'] #SingleMuon2018A file
cfo.POSTPROCESSOR.inputFiles =   ['349FAAC5-419F-D64D-A5B7-1EE4FFB33703.root'] #DoubleMuon2018D file
#cfo.POSTPROCESSOR.inputFiles = ['95EEB251-3893-134B-A1DC-AB8FCB6120A8.root']
cfo.POSTPROCESSOR.run()


# clean up environ
del os.environ['IS_RUN']
