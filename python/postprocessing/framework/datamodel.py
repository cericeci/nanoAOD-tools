import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
from PhysicsTools.NanoAODTools.postprocessing.framework.treeReaderArrayTools import InputTree 

class Event:
    """Class that allows seeing an entry of a PyROOT TTree as an Event"""
    def __init__(self,tree,entry):
        self._tree = tree
        self._entry = entry
        self._tree.gotoEntry(entry)
    def __getattr__(self,name):
        if name in self.__dict__: return self.__dict__[name]
        return self._tree.readBranch(name)
    def __getitem__(self,attr):
        return self.__getattr__(attr)
    def eval(self,expr):
        """Evaluate an expression, as TTree::Draw would do. 

           This is added for convenience, but it may perform poorly and the implementation is not bulletproof,
           so it's better to rely on reading values, collections or objects directly
        """ 
        if not hasattr(self._tree, '_exprs'):
            self._tree._exprs = {}
            # remove useless warning about EvalInstance()
            import warnings
            warnings.filterwarnings(action='ignore', category=RuntimeWarning, 
                                    message='creating converter for unknown type "const char\*\*"$')
            warnings.filterwarnings(action='ignore', category=RuntimeWarning, 
                                    message='creating converter for unknown type "const char\*\[\]"$')
        if expr not in self._tree._exprs:
            formula = ROOT.TTreeFormula(expr,expr,self._tree)
            if formula.IsInteger():
                formula.go = formula.EvalInstance64
            else:
                formula.go = formula.EvalInstance
            self._tree._exprs[expr] = formula
            # force sync, to be safe
            self._tree.GetEntry(self._entry)
            self._tree.entry = self._entry
            #self._tree._exprs[expr].SetQuickLoad(False)
        else:
            self._tree.gotoEntry(entry)
            formula = self._tree._exprs[expr]
        if "[" in expr: # unclear why this is needed, but otherwise for some arrays x[i] == 0 for all i > 0
            formula.GetNdata()
        return formula.go()

class Object:
    """Class that allows seeing a set branches plus possibly an index as an Object"""
    def __init__(self,event,prefix,index=None):
        self._event = event
        self._prefix = prefix+"_"
        self._index = index
    def __getattr__(self,name):
        if self._prefix == "SoftActivityJet_" and (name == "mass"):
            return 0
        if name in self.__dict__: return self.__dict__[name]
        if name[:2] == "__" and name[-2:] == "__":
            raise AttributeError
        val = getattr(self._event,self._prefix+name)
        if self._index != None:
            val = val[self._index]
        val = ord(val) if type(val)==str else val # convert char to integer number
        self.__dict__[name] = val ## cache
        return val
    def __getitem__(self,attr):
        return self.__getattr__(attr)
    def p4(self):
        ret = ROOT.TLorentzVector()
        ret.SetPtEtaPhiM(self.pt,self.eta,self.phi,self.mass)
        return ret
    def subObj(self,prefix):
        return Object(self._event,self._prefix+prefix)
    def __repr__(self):
        return ("<%s[%s]>" % (self._prefix[:-1],self._index)) if self._index != None else ("<%s>" % self._prefix[:-1])
    def __str__(self):
        return self.__repr__()

class Collection:
    def __init__(self,event,prefix,lenVar=None):
        self._event = event
        self._prefix = prefix
        if lenVar != None and type(prefix) != list:
            self._len = getattr(event,lenVar)
        elif type(prefix) != list:
            self._len = getattr(event,"n"+prefix)
        self._cumuls = []
        self._cache = {}
    def __getitem__(self,index):
        if type(self._prefix) != list:
            if type(index) == int and index in self._cache: return self._cache[index]
            if index >= self._len: raise IndexError, "Invalid index %r (len is %r) at %s" % (index,self._len,self._prefix)
            ret = Object(self._event,self._prefix,index=index)
            if type(index) == int: self._cache[index] = ret
            return ret
        else:
            if index >= self._cumuls[-1]: 
                #print self._prefix, self._cumuls
                raise IndexError, "Invalid index %r (len is %r) at %s" % (index,self._cumuls[-1],self._prefix[-1])
            if type(index) == int and index in self._cache: return self._cache[index]
            if type(index) == int:
                idtag = -1
                subid = -1
                for i in range(len(self._cumuls)-1):
                    if index >= self._cumuls[i] and index < self._cumuls[i+1]:
                        idtag = i
                        subid = self._cumuls[i]
                ret = Object(self._event, self._prefix[idtag], index-subid)
                self._cache[index] = ret
                return ret

    def __len__(self):
        return self._len
    def __add__(self,other):
        ret = Collection(self._event, [self._prefix, other._prefix])
        ret._len = [self._len, other._len]
        ret._cumuls = [0]
        for l in ret._len:
            ret._cumuls.append(ret._cumuls[-1] + l)
        ret._len = ret._cumuls[-1]
        return ret

