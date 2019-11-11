import os
import copy
import imp, os, sys, json
from optparse import OptionParser,OptionGroup
import re
import ROOT

parser = OptionParser()
g1 = OptionGroup(parser,"Analysis options")
g1.add_option("-c", "--cfg-file", dest="cfg_file", help="Config file containing PostProcessor instance", default="")
g1.add_option("-s", "--sample-file", dest="sample_file", default="SMS2016.py", help="Config file for sample configuration")
g1.add_option("-d", "--dataset", dest="dataset", default=[], action="append", help="Run only over this dataset")
g1.add_option("-f", "--file", dest="filename", default=None, help="Run this specific file")
parser.add_option_group(g1)
g1.add_option("-q", "--queue", dest="queue", type="string", default="local", help="Queue to send the job to. Local to run locally")
g1.add_option("-n", dest="new", action="store_true", default=False, help="If active, will check if output files exist and skip the job if they do.")
g1.add_option("--check", dest="check", action="store_true", default=False, help="If active, will check if input files are ok (i.e. hjhave a non-empty Events tree). Also does the check for skipable output files if -n is activated")

(options,args) = parser.parse_args()


# Deal with sample and file selection

# First load the sample config file
sampleFile = __import__(options.sample_file)

# Create preliminar joblists
joblist = []

for s in sampleFile.sampleList:
  for sels in options.dataset:
    if not(re.search(sels,s["name"])): continue
    if "inputFile" in s:
      #Run only over one file
      theFiles.append(s["inputFile"])
    elif "inputDir" in s:
      #Search for all files in the directory
      lists = os.listdir(s["inputDir"])
      theFiles = [i for i in filter(lambda x: ".root" in x, lists)]
      if options.filename:
        theFiles = [i for i in filter(lambda x: options.filename in x, theFiles)]
    # Now create a job for each sample file
    print "Loading input files for dataset %s"%s["name"]
    iF = 0
    for f in theFiles:
      skipMe = False
      sf = copy.copy(s)
      sf["inputFile"]  = sf["inputDir"]  + "/" + f
      sf["outputFile"] = sf["outputDir"] + "/" + f.replace(".root","_Skim.root")
      # Check validity of input file
      if os.path.isfile(sf["inputFile"]) and options.check:
        # Check if the file is already there and has the "Events" tree
        tf = ROOT.TFile(sf["inputFile"], "READ")
        evs = tf.Get("Events")
        fake = tf.Get("Estonoexisteasiquedeberiafallaralcogerlo")
        if type(evs) == type(fake):
          # If it is here then the Events tree is a TTree or we ****ed up big in the postprocessing before
          print "[WARNING] Skipping file %s which doesn't contain an Events TTree..."%(sf["inputFile"])
          skipMe = True
        tf.Close()
      if os.path.isfile(sf["outputFile"]) and options.new:
        skipMe = True
        if options.check: 
          skipMe = False
          # Check if the file is already there and has the "Events" tree
          tf = ROOT.TFile(sf["outputFile"], "READ")
          evs = tf.Get("Events")
          fake = tf.Get("Estonoexisteasiquedeberiafallaralcogerlo")
          if type(evs) != type(fake):
            # If it is here then the Events tree is not a TTree or we ****ed up big in the postprocessing before
            if evs.GetEntries() > 0:
              # Check if we have at least one entry (might have been postprocessed and not saved)
              print "Skipping one file..."
              skipMe = True
          tf.Close()

      if not(skipMe):
        iF += 1
        joblist.append(sf)

    if not(os.path.isdir(sf["outputDir"])): 
      print "Creating output directory %s ..."%sf["outputDir"]
      os.mkdir(sf["outputDir"])
    print "... %i jobs created for dataset %s"%(iF, s["name"])

#Job executioner
def runJob(jobDict):
  # create sample json to run locally
  os.environ['OPTIONS_SAMPLE_JSON']='options_%s.json'%(jobDict["inputFile"].replace("/","_"))
  options_sample = open('options_%s.json'%(jobDict["inputFile"].replace("/","_")),'w')
  options_sample.write(json.dumps(jobDict))
  options_sample.close()
  # And then configure the postprocessor running
  os.environ['IS_RUN']="true"
  handle = open(options.cfg_file,'r')
  cfo= imp.load_source(options.cfg_file.split('/')[-1].rstrip('.py'), options.cfg_file, handle)
  cfo.POSTPROCESSOR.inputFiles = [jobDict["inputFile"]]
  cfo.POSTPROCESSOR.outputDir = jobDict["outputDir"]
  cfo.POSTPROCESSOR.run()
  # clean up environ and delete temporary options file
  del os.environ['IS_RUN']
  del os.environ['OPTIONS_SAMPLE_JSON']
  os.remove('options_%s.json'%(jobDict["inputFile"].replace("/","_")))
 
if options.queue == "local":
  print "Running in local mode..."
  for j in joblist:
    runJob(j)

else:
  print "Running in queued mode..."
  print "Will send %i jobs to queue %s"%(len(joblist), options.queue)
  basecmd = "{dir}/lxbatch_runner.sh {dir} {cmssw} python {self} -c {cfgfile} -s {samplefile} ".format(
                dir = os.getcwd(), cmssw = os.environ['CMSSW_BASE'], cfgfile = options.cfg_file,
                self=sys.argv[0], samplefile = options.sample_file)
  for j in joblist:
    os.system("qsub -q %s -N %s "%(options.queue,j["name"]) +  basecmd + " -f %s -d %s"%(j["inputFile"].split("/")[-1], j["name"]))
