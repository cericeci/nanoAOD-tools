## Triggers for 2016 DATA 
triggers2016=dict(
    triggers_mumu_iso    = [ "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL", 
                             "HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL",
                             "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ",
                             "HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ",
                             "HLT_Mu23_TrkIsoVVL_Mu8_TrkIsoVVL", 
                             "HLT_Mu23_TrkIsoVVL_TkMu8_TrkIsoVVL",
                             "HLT_Mu23_TrkIsoVVL_Mu8_TrkIsoVVL_DZ",
                             "HLT_Mu23_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ" ],
    triggers_mumu_noniso = [ "HLT_Mu30_TkMu11" ],
    triggers_mumu_ss = [ "HLT_Mu17_Mu8_SameSign",
                         "HLT_Mu17_Mu8_SameSign_DZ", 
                         "HLT_Mu20_Mu10_SameSign", 
                         "HLT_Mu20_Mu10_SameSign_DZ" ],
    triggers_mumu    = [ "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL", 
                         "HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL",
                         "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ",
                         "HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ",
                         "HLT_Mu23_TrkIsoVVL_Mu8_TrkIsoVVL", 
                         "HLT_Mu23_TrkIsoVVL_TkMu8_TrkIsoVVL",
                         "HLT_Mu23_TrkIsoVVL_Mu8_TrkIsoVVL_DZ",
                         "HLT_Mu23_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ" ],
    triggers_ee = [ "HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ", 
                    "HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ" ], # 17/12 prescaled in column 0
    triggers_ee_noniso = ["HLT_DoubleEle33_CaloIdL", 
                          "HLT_DoubleEle37_Ele27_CaloIdL_GsfTrkIdVL", 
                          "HLT_DoubleEle33_CaloIdL_GsfTrkIdVL" ],

    # warning: ee trigger without DZ is prescaled
    triggers_ee_nodz = [ "HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL" ],

    triggers_mue_run1   = [ "HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL", 
                            "HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL" ],
    triggers_mue   = [ "HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL", # warning, check prescales depending on run range 
                       "HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL",
                       "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL", 
                       "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ", 
                       "HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL",
                       "HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_DZ",
                       "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL",
                       "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ" ],
    triggers_mue_noiso = [ 
        'HLT_Mu33_Ele33_CaloIdL_GsfTrkIdVL',
        'HLT_Mu30_Ele30_CaloIdL_GsfTrkIdVL', 
        ],
    triggers_mumu_ht =  [ "HLT_DoubleMu8_Mass8_PFHT300" ],
    triggers_ee_ht =  [ "HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT300" ],
    triggers_mue_ht = [ "HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT300" ],

    triggers_mutau  = ["HLT_IsoMu19_eta2p1_LooseIsoPFTau20"],

    triggers_eltau  = ["HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau30",
                       "HLT_Ele36_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1",
                      ],



    triggers_3e = [ "HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL" ],
    triggers_3mu = [ "HLT_TripleMu_12_10_5", 
                     "HLT_TripleMu_5_3_3" ], # 533 only in part of the dataset
    triggers_3mu_alt = [ "HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtx" ],
    triggers_2mu1e = [ "HLT_DiMu9_Ele9_CaloIdL_TrackIdL" ],
    triggers_2e1mu = [ "HLT_Mu8_DiEle12_CaloIdL_TrackIdL" ],
    
    triggers_1mu_iso = [ 'HLT_IsoMu20', 
                         'HLT_IsoTkMu20', 
                         'HLT_IsoMu22', 
                         'HLT_IsoTkMu22',
                         'HLT_IsoMu24', # Mu20's prescaled in column 0
                         'HLT_IsoTkMu24',
                         'HLT_IsoMu22_eta2p1',
                         'HLT_IsoTkMu22_eta2p1'],
    triggers_1mu_noniso = [ 'HLT_Mu45_eta2p1', 
                            'HLT_Mu50', 
                            'HLT_TkMu50' ],

# note: here the WP75 is th name in MC, WPLoose and WPTight should be in data
    triggers_1e_iso      = [ 
        #"HLT_Ele23_WPLoose_Gsf", # only up to 5E33
        #"HLT_Ele27_WPLoose_Gsf", # only up to 5E33
        "HLT_Ele25_WPTight_Gsf",        # not in column 0
        "HLT_Ele25_eta2p1_WPLoose_Gsf", # not in column 0 
        "HLT_Ele25_eta2p1_WPTight_Gsf", 
        "HLT_Ele27_WPTight_Gsf", 
        "HLT_Ele27_eta2p1_WPLoose_Gsf",
        "HLT_Ele45_WPLoose_Gsf" ],
    triggers_1e_noniso      = [ "HLT_Ele105_CaloIdVT_GsfTrkIdT","HLT_Ele115_CaloIdVT_GsfTrkIdT"],

# Lepton fake rate triggers (prescaled)
    triggers_FR_1mu_iso = [ "HLT_Mu%d_TrkIsoVVL" % pt for pt in (8,17) ], # DoubleMu PD
    triggers_FR_1mu_noiso = [ "HLT_Mu%d" % pt for pt in (8,17) ] + ["HLT_Mu3_PFJet40"], # DoubleMu PD
    triggers_FR_1e_noiso = [ "HLT_Ele%d_CaloIdM_TrackIdM_PFJet30" % pt for pt in (8,12,17,23,33) ] + [ "HLT_Ele10_CaloIdM_TrackIdM_CentralPFJet30_BTagCSV_p13" ],# DoubleEG
    triggers_FR_1e_iso   = [ "HLT_Ele%d_CaloIdL_TrackIdL_IsoVL_PFJet30" % pt for pt in (8,12,17,23,33) ], # DoubleEG
    triggers_FR_1e_b2g = [ "HLT_Ele17_CaloIdL_TrkIdL_IsoVL", "HLT_Ele12_CaloIdL_TrackIdL_IsoVL" ],
    triggers_FR_jet  =  [ "HLT_PFJet40", "HLT_PFJet60", "HLT_PFJet80" ],
    triggers_FR_muNoIso = [ "HLT_Mu%d" % pt for pt in (20,27,50) ], #+ [ "HLT_Mu%d_eta2p1" % pt for pt in (24,45,) ] + [ "HLT_L2Mu%d" % pt for pt in (10,) ] # SingleMu PD

### GP: did not look at anything below this

    triggers_SOS_doublemulowMET = ["HLT_DoubleMu3_PFMET50"],
    triggers_SOS_highMET = ["HLT_PFMET90_PFMHT90_IDTight","HLT_PFMETNoMu90_PFMHTNoMu90_IDTight","HLT_PFMET100_PFMHT100_IDTight","HLT_PFMETNoMu100_PFMHTNoMu100_IDTight", "HLT_PFMET110_PFMHT110_IDTight", "HLT_PFMETNoMu110_PFMHTNoMu110_IDTight", "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight", "HLT_PFMET120_PFMHT120_IDTight"],
    triggers_SOS_tripleMu = ["HLT_TripleMu_5_3_3","HLT_TripleMu_5_3_3_DZ_Mass3p8"],


    ### Mike ---> for the VV analysis 
    triggers_dijet_fat=["HLT_PFHT650_WideJetMJJ900DEtaJJ1p5","HLT_PFHT650_WideJetMJJ950DEtaJJ1p5"],
    # triggers to recover HT trigger inefficiency in late 2016
    triggers_jet_recoverHT=["HLT_PFJet450", "HLT_PFJet500", "HLT_AK8PFJet450", "HLT_AK8PFJet500", "HLT_CaloJet500_NoJetID"],
    ### ----> for the MT2 analysis

    triggers_MT2_mumu = ["HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ", "HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ"],
    triggers_MT2_ee = ["HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ","HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ"],
    triggers_MT2_emu = ["HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL", "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL"],
    triggers_MT2_mue = ["HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL", "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL"],
    
    #triggers_MT2_mue = triggers_mue + ["HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL", "HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL"]
    
    triggers_MT2_mu = ["HLT_IsoMu17_eta2p1","HLT_IsoMu20_eta2p1", "HLT_IsoMu20", "HLT_IsoTkMu20"],
    triggers_MT2_e = ["HLT_Ele23_WPLoose_Gsf", "HLT_Ele22_eta2p1_WPLoose_Gsf","HLT_Ele22_eta2p1_WP75_Gsf", "HLT_Ele23_WP75_Gsf"],

    triggers_HT900 = ["HLT_PFHT900"],
    triggers_HT800 = ["HLT_PFHT800"],
#triggers_MET170 = ["HLT_PFMET170_NoiseCleaned"] #removed from menu
#other paths added in data:
    triggers_MET170_NotCleaned = ["HLT_PFMET170_NotCleaned"],
    triggers_MET170_HBHECleaned = ["HLT_PFMET170_HBHECleaned"],
    triggers_MET170_BeamHaloCleaned = ["HLT_PFMET170_BeamHaloCleaned"], # removed from the menu
    triggers_AllMET170 = ["HLT_PFMET170_NotCleaned"] + ["HLT_PFMET170_HBHECleaned"],

    triggers_MET300 = ["HLT_PFMET300"], #not in 2016 menu anymore
    #triggers_MET300_NotCleaned = ["HLT_PFMET300"]
    #triggers_MET300_JetIdCleaned = ["HLT_PFMET300_JetIdCleaned"] #not in 2016 menu anymore
    triggers_AllMET300 = ["HLT_PFMET300"],

    #triggers_HT350_MET120 = ["HLT_PFHT350_PFMET120_NoiseCleaned"] # not in 2016 menu anymore
    #triggers_HTMET100 = ["HLT_PFHT350_PFMET100_NoiseCleaned"]
    triggers_HT350_MET100 = ["HLT_PFHT350_PFMET100"],

    triggers_HT350 = ["HLT_PFHT350"], # prescaled
    triggers_HT475 = ["HLT_PFHT475"], # prescaled
    triggers_HT600 = ["HLT_PFHT600"], # prescaled

    triggers_dijet = ["HLT_DiPFJetAve40", "HLT_DiPFJetAve60"],

    triggers_jet = ["HLT_PFJet40", "HLT_PFJet60", "HLT_PFJet80", "HLT_PFJet140", "HLT_PFJet200", "HLT_PFJet260", "HLT_PFJet320", "HLT_PFJet400", "HLT_PFJet450", "HLT_PFJet500"],

    triggers_dijet70met120 = [ "HLT_DiCentralPFJet70_PFMET120" ],
    triggers_dijet55met110 = [ "HLT_DiCentralPFJet55_PFMET110" ],

    triggers_photon75ps = ["HLT_Photon75"],
    triggers_photon90ps = ["HLT_Photon90"],
    triggers_photon120ps = ["HLT_Photon120"],
    triggers_photon30 = ["HLT_Photon30_R9Id90_HE10_IsoM"],
    triggers_photon50 = ["HLT_Photon50_R9Id90_HE10_IsoM"],
    triggers_photon75 = ["HLT_Photon75_R9Id90_HE10_IsoM"],
    triggers_photon90 = ["HLT_Photon90_R9Id90_HE10_IsoM"],
    triggers_photon120 = ["HLT_Photon120_R9Id90_HE10_IsoM"],
    triggers_photon155 = ["HLT_Photon155"],
    triggers_photon175 = ["HLT_Photon175"],
    triggers_photon165_HE10 = ["HLT_Photon165_HE10"],

    # there is no jetId or Noise Cleaned path in 2016 menu  all met, met cross paths by defult have HBHE cleaning applied
    # monojets triggers
    triggers_met90_mht90 = ["HLT_PFMET90_PFMHT90_IDTight","HLT_PFMET90_PFMHT90_IDLoose"],
    triggers_met100_mht100 = ["HLT_PFMET100_PFMHT100_IDTight","HLT_PFMET100_PFMHT100_IDLoose"],
    triggers_met120_mht120 = ["HLT_PFMET120_PFMHT120_IDTight"],
    #triggers_metNoMu90_mhtNoMu90 = ["HLT_PFMETNoMu90_NoiseCleaned_PFMHTNoMu90_IDTight","HLT_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight","HLT_PFMETNoMu90_PFMHTNoMu90_IDTight"]
    triggers_metNoMu90_mhtNoMu90 = ["HLT_PFMETNoMu90_PFMHTNoMu90_IDTight"],
    triggers_metNoMu120_mhtNoMu120 = ["HLT_PFMETNoMu120_PFMHTNoMu120_IDTight"],
    triggers_Jet80MET90 = ["HLT_MonoCentralPFJet80_PFMETNoMu90_PFMHTNoMu90_IDTight"],
    triggers_Jet80MET120 = ["HLT_MonoCentralPFJet80_PFMETNoMu120_PFMHTNoMu120_IDTight"],
    triggers_MET120Mu5 = ["HLT_PFMET120_Mu5"],

### ----> for the edgeZ analysis. 
### we want them separately for detailed trigger efficiency studies
###---- Muons
    # Isolated triggers:
    triggers_mu17mu8_dz      = ['HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ'],
    triggers_mu17tkmu8       = ['HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL'],
    triggers_mu17tkmu8_dz    = ['HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ'],
    # Non-Isolated triggers:
    triggers_mu27tkmu8       = ['HLT_Mu27_TkMu8'],
    triggers_mu30tkmu11      = ['HLT_Mu30_TkMu11'],
    ###---- Electrons
    # Isolated triggers:
    triggers_el23el12_dz     = ['HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'],
    # Non-Isolated triggers:
    triggers_doubleele33     = ['HLT_DoubleEle33_CaloIdL_GsfTrkIdVL'],
    triggers_doubleele33_MW  = ['HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_MW'],
###---- Electron-Muon
    triggers_mu23el12        = ['HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL'],
    triggers_mu8el23         = ['HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL'],
    ###---- HT:
    triggers_pfht200      = ['HLT_PFHT200'],
    triggers_pfht250      = ['HLT_PFHT250'],
    triggers_pfht300      = ['HLT_PFHT300'],
    triggers_pfht350      = ['HLT_PFHT350'],
    triggers_pfht400      = ['HLT_PFHT400'],
    triggers_pfht475      = ['HLT_PFHT475'],
    triggers_pfht600      = ['HLT_PFHT600'],
    triggers_pfht650      = ['HLT_PFHT650'],
    triggers_pfht800      = ['HLT_PFHT800'],
    triggers_pfht900      = ['HLT_PFHT900'],
    triggers_at57         = ['HLT_PFHT200_DiPFJet90_PFAlphaT0p57'],
    triggers_at55         = ['HLT_PFHT250_DiPFJet90_PFAlphaT0p55'],
    triggers_at53         = ['HLT_PFHT300_DiPFJet90_PFAlphaT0p53'],
    triggers_at52         = ['HLT_PFHT350_DiPFJet90_PFAlphaT0p52'],
    triggers_at51         = ['HLT_PFHT400_DiPFJet90_PFAlphaT0p51'],
    triggers_htjet        = ['HLT_PFHT550_4Jet', 'HLT_PFHT650_4Jet', 'HLT_PFHT750_4Jet'],
    triggers_mu30ele30    = ['HLT_Mu30_Ele30_CaloIdL_GsfTrkIdVL'],
    triggers_pfht = ['HLT_PFHT%d'%x for x in [200,250,300,350,400,475,600,650,800,900]],
    ###---- MET:
    triggers_htmet = ['HLT_PFHT300_PFMET110'],
)


