class CompareConfig:
    """

    """
    def __init__(self):
        ## USC options (phase 1)
        # self.scriptPath = "C:/Users/nschiff2/IdeaProjects/AutoHEC/src/Analysis/"
        # self.filePath = "G:/PROJECTS_non-FEMA/MWRD_ReleaseRate_Phase1/H&H/USC/"
        # self.versionPath = self.filePath + "USC_V"
        # self.dssRasFileName = "/Base_and_Calibration.dss"
        # self.dssHmsFilePath = "/"
        # self.dssHmsFileName = [self.dssHmsFilePath + "USC.dss"]
        # self.bankFileName = "G:/PROJECTS_non-FEMA/MWRD_ReleaseRate_Phase1/H&H/USC/USC_banks2.csv" #CSV file
        # self.inundOutFileName = self.filePath + "OOB_USC_V"
        # self.rasRunName = "ILREVEXIMP040512"
        # self.hmsRunName = "100-24"
        # self.startDate = "01DEC2007"
        # self.watershed = "USC"
        # self.timestep = 6.0
        ## USC options (phase 2)
        # self.scriptPath = "C:/Users/nschiff2/Documents/AutoHECexp/src/Analysis/"
        # self.filePath = "G:/PROJECTS_non-FEMA/MWRD_ReleaseRate_PhaseII/H&H/USC_models/"
        # self.versionPath = self.filePath + "v"
        # self.dssRasFileName = "/Base_and_Calibration.dss"
        # self.dssHmsFilePath = "/"
        # self.dssHmsFileName = [self.dssHmsFilePath + "USC.dss"]
        # self.bankFileName = "G:/PROJECTS_non-FEMA/MWRD_ReleaseRate_Phase1/H&H/USC/USC_banks2.csv" #CSV file
        # self.inundOutFileName = self.filePath + "OOB_USC_V"
        # self.rasRunName = "ILREVEXIMP040512"
        # self.hmsRunName = "50-24"
        # self.startDate = "01DEC2007"
        # self.watershed = "USC"
        # self.timestep = 6.0

        # TICR options
        # self.scriptPath = "C:/Users/nschiff2/Documents/AutoHECexp/src/Analysis/"
        # self.filePath = "G:/PROJECTS_non-FEMA/MWRD_ReleaseRate_PhaseII/H&H/CalSag_models/"
        # #self.filePath = "C:/Users/nschiff2/Documents/MWRD/CalSag_models/"
        # self.versionPath = self.filePath + "v"
        # # for hydrographs, max WSEL (GIS maps)
        # self.dssRasFileName = "/TICR_Baseline.dss"
        # # for max WSEL (GIS maps)
        # self.XSfile = "TICR_noculvert.csv"
        # self.dssHmsFilePath = "/"
        # # for SO curves
        # self.dssHmsFileName = [self.dssHmsFilePath + "TICR_Design.dss"]
        # #self.bankFileName = "G:/PROJECTS_non-FEMA/MWRD_ReleaseRate_Phase1/H&H/USC/USC_banks2.csv" #CSV file
        # #self.inundOutFileName = self.filePath + "OOB_EastBranch_Poplar_V"
        # self.rasRunName = "TICR3_BASE"
        # self.hmsRunName = "HuffQII_100yr12Hr"
        # self.startDate = "01DEC2006"
        # self.watershed = "CalSag"
        # self.timestep = 30.0

        # PC options
        self.scriptPath = "C:/Users/nschiff2/Documents/AutoHECexp/src/Analysis/"
        self.filePath = "G:/PROJECTS_non-FEMA/MWRD_ReleaseRate_PhaseII/H&H/Poplar_models/"
        #self.filePath = "C:/Users/nschiff2/Documents/MWRD/Poplar_models/"
        self.versionPath = self.filePath + "v"
        # for hydrographs, max WSEL (GIS maps)
        self.branch = "EB" #EB, RR, SB, SH, TA, MS
        self.dssRasFileName = "/RAS/PC" + self.branch + "/PC" + self.branch + ".dss"
                            # "/RAS/PCEB/PCEB.dss"
                            # "/RAS/PCRR/PCRR.dss"
                            # "/RAS/PCSB/PCSB.dss"
                            # "/RAS/PCSH/PCSH.dss"
                            # "/RAS/PCTA/PCTA.dss"
                            # "/RAS/PCMS/PCMS.dss"
        # for max WSEL (GIS maps)
        self.XSfile = "PC" + self.branch + "_noculvert.csv"
                    # "PCEB_noculvert.csv"
                    # "PCRR_noculvert.csv"
                    # "PCSB_noculvert.csv"
                    # "PCSH_noculvert.csv"
                    # "PCTA_noculvert.csv"
                    # "PCMS_noculvert.csv"
        self.dssHmsFilePath = "/HEC-HMS/"
        # for SO curves
        self.dssHmsFileName = [self.dssHmsFilePath + "PC_EastBranchHMS/EastBranch_Poplar.dss"]
                                                   # "PC_EastBranchHMS/EastBranch_Poplar.dss"]
                                                   # "PC_LordsPark/PC_LordsPark.dss"]
                                                   # "PC_Mainstem/Poplar_Creek_Main.dss"]
                                                   # "PC_Railroad/PC_Railroad.dss"]
                                                   # "PC_Schaumburg/PC_Schaumburg.dss"]
                                                   # "PC_SouthBranchHMS/SouthBranch_Poplar.dss"]
                                                   # "PC_TribA/PC_TribA.dss"]
        #self.bankFileName = "G:/PROJECTS_non-FEMA/MWRD_ReleaseRate_Phase1/H&H/USC/USC_banks2.csv" #CSV file
        #self.inundOutFileName = self.filePath + "OOB_EastBranch_Poplar_V"
        self.rasRunName = "EX100yr24hr"
        self.hmsRunName = "EX100yr24hr"
        self.startDate = "31DEC2000" # 31DEC2000, 01DEC2000 (MS)
        self.watershed = "Poplar"
        self.timestep = 6.0  # 6.0, 15.0 (MS)

        ## STCR options
        # self.scriptPath = "C:/Users/nschiff2/IdeaProjects/AutoHEC/src/Analysis/"
        # self.filePath = "G:/PROJECTS_non-FEMA/MWRD_ReleaseRate_Phase1/H&H/StonyCreek/"
        # self.versionPath = self.filePath + "Stony_V"
        # self.dssRasFileName = "/HydraulicModels/ExistingConditions/STCR/STCR_DesignRuns/STCR_Design2.dss"
        # self.dssHmsFilePath = "/HydrologicModels/ExistingConditions/"
        # self.dssHmsFileName = [self.dssHmsFilePath + "LucasDitch/LUDT_DesignRuns/LUDT_Design.dss",
        #             self.dssHmsFilePath + "LucasDiversionDitch/LDDT_DesignRuns/LDDT_HMS.dss",
        #             self.dssHmsFilePath + "MelvinaDitch/MEDT_DesignRuns/MEDT_HMS.dss",
        #             self.dssHmsFilePath + "MPDT/MPDT_DesignRuns/MPDT_revised.dss",
        #             self.dssHmsFilePath + "OakLawn/OLCR_DesignRuns/OLCRHMS.dss",
        #             self.dssHmsFilePath + "StonyCreek/HMS/STCR_DesignRuns/STCR_combined.dss"]
        # self.bankFileName = "G:/PROJECTS_non-FEMA/MWRD_ReleaseRate_Phase1/H&H/StonyCreek/StonyCreek_banks2.csv" #CSV file
        # self.inundOutFileName = self.filePath + "OOB_StonyCreek_V"
        # self.rasRunName = "HUFFQII_100YR12H" #"100YR24HRISWS" #
        # self.startDate = "01DEC2006"
        # self.watershed = "StonyCreek"
        # self.timestep = 5.0

        ## Global options
        # Model versions to analyze
        # --first item is considered the base model
        # --max of 5 for now
        # --cannot use a non-redeveloped model as the first model when plotting rating curves
        self.versions = ["000","001","002","003","004"]
                        # ["000","001","002","003","004","005","006","007","008"]
                        # ["33.15_forest","33.40_forest","34.15_forest","34.40_forest","35.15_forest","35.40_forest","36.15_forest","36.40_forest"]
                        # ["2.0","36.15_forest","36.40_forest"] # USC 0.15 cfs/acre forested
                        # ["2.0","35.15_forest","35.40_forest"] # USC 0.2 cfs/acre forested
                        # ["2.0","34.15_forest","34.40_forest"] # USC 0.25 cfs/acre forested
                        # ["2.0","33.15_forest","33.40_forest"] # USC 0.3 cfs/acre forested
                        # ["2.0","3.0optim","5.0optim"] # USC 0.15 cfs/acre
                        # ["2.0","9.0optim","19.0optim"] # USC 0.2 cfs/acre
                        # ["2.0","10.0optim","21.0optim"] # USC 0.25 cfs/acre
                        # ["2.0","4.0optim","6.0optim"] # USC 0.3 cfs/acre
                        # ["2.0","22.0optim","23.0optim"] # USC RR scenario 1
                        # ["2.0","16.1optim","17.1optim"] # USC RR scenario 2
                        # ["2.0","26.15","26.40"] # USC RR scenario 3
                        # ["1.0","19","22"] # STCR 0.15 cfs/acre, 0.5" retention
                        # ["1.0","17","21"] # STCR 0.3 cfs/acre, 0.5" retention
                        # ["1.0","6.1optim","13.0optim"] # STCR 0.3 cfs/acre, 1.0" retention

                        # ["26.15","26.15_LowDis","26.40","26.40_LowDis","27.15","27.40"]
                        # ["4.0optim","6.0","7.0optim","13.0optim"]
                        # ["2.0","3.0optim","4.0optim","5.0optim","6.0optim","7.0","8.0","9.0optim",
                        # "10.0optim","11.0optim","11.1optim","12.0optim","12.1optim","13.0optim",
                        # "14.0optim","15.0optim","16.0optim","17.0optim","19.0optim","21.0optim",
                        # "22.0optim","23.0optim","24.0optim"]
        # Description of each plotted/analyzed model version, used for figure legends
        self.vDescription = ["Base model","40% Development, 0.15 cfs/acre", "40% Development, 0.2 cfs/acre", "40% Development, 0.25 cfs/acre", "40% Development, 0.3 cfs/acre"]
                             #["Base model", "15% Development, 0.15 cfs/acre", "15% Development, 0.2 cfs/acre", "15% Development, 0.25 cfs/acre", "15% Development, 0.3 cfs/acre",
                             # "40% Development, 0.15 cfs/acre", "40% Development, 0.2 cfs/acre", "40% Development, 0.25 cfs/acre", "40% Development, 0.3 cfs/acre"]
                             #["DWP Base Model (v2)",
                             # "40% Development; WB/MS34-MS40/MS42 0.25, AH01-AH12 0.2, rest 0.3 cfs/acre (v17)",
                             # "40% Development; WB/MS34-MS40/MS42 0.2, AH01-AH12 0.15, rest 0.3 cfs/acre (v23)"]
                             # "15% Development; WB/MS34-MS40/MS42 0.25, AH01-AH12 0.2, rest 0.3 cfs/acre (v16)",
                             # "15% Development; WB/MS34-MS40/MS42 0.2, AH01-AH12 0.15, rest 0.3 cfs/acre (v22)"]
