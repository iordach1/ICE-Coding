# Configuration that is used through all HEC Python/Jython scripts

def setme1(self):
    # General model settings
    # *only the below options should be changed*
    # --scriptPath is the location of the scripts in the AutoHEC package;
    #   it should end with "AutoHEC/src"
    # --modelPath is the location of the model run files
    # --modelVersion is the directory name of the model version
    self.scriptPath="C:/Users/nschiff2/Documents/AutoHECexp/src"
    self.hmsDir="HEC-HMS"
    self.modelPath = "G:/PROJECTS_non-FEMA/MWRD_ReleaseRate_PhaseII/H&H/Poplar_models/"
    #self.modelPath = "C:/Users/nschiff2/Documents/MWRD/Poplar_models/"
    self.modelVersion = self.modelPath + "v005/"
    self.hmsCommand="HEC-HMS.cmd"
    self.dssDir="HEC-DSSVue"
    self.dssCommand="HEC-DSSVue.cmd"

    # Use these options only when you need a different model version to build the
    # storage-outflow curves
    # **does not apply for USC**
    #self.osModelVersion = self.modelVersion #self.modelPath + "USC_V11.0optim"
    #self.osHmsVersion = self.osModelVersion

    return self

def setme2hms(self):
    # HMS precipitation settings
    # --hmsRunName is the name of the compute option you would choose in HEC-HMS
    # --hmsMetFile is the location of the relevant *.met file for hmsRunName
    # --hmsGageName is the name of the gage shown in the hmsMetFile
    self.hmsRunName = "EX100yr24hr" #"HuffQII_100yr12hrISWS" #"HuffQIII_100yr24hrISWS"
    self.hmsMetFile = self.hmsProjectPath + "/100yr_24hr" #"/HuffQII_100yr12hrISWS" #"/HuffQIII_100yr24hrISWS"
    self.hmsGageName = "100yr-24hr" #"HuffQII_100yr12hrISWS" #"HuffQIII_100yr24hrISWS"

    # Future parameters
    # --redevelopment is the proportion of the subbasin that is routed
    #   through the new reservoir
    # --curvenumber is the curve number for all subbasins
    # --releaserate is the release rate for all subbasins; this can
    #   be adjusted by subbasin if you run InitHMS.py separate from
    #   the model runs, manually edit subbasin_records.json, and then
    #   run HEC-HMS and HEC-RAS.
    # --the "alt" and "alt2" suffixed are the redevelopment and release rates
    #   pertaining to the lists of subbasins in alt_RD_basins.txt, alt_RD_basins2.txt,
    #   alt_RR_basins.txt, and alt_RR_basins2.txt
    self.redevelopment = 40
    self.redevelopmentalt = 20
    self.redevelopmentalt2 = 0.01
    self.curvenumber = 88
    self.releaserate = 0.15
    self.releaseratealt = 0.1  #stays the same because it is for a different county with a set RR
    self.releaseratealt2 = 0.1
    self.canopyrate = 0.52
    self.canopyalt = 0.39

    # HMS project configuration data
    # --numHmsModels is the number of HMS model runs needed for a single RAS run
    # --interval is the output time interval of FLOW in the RAS DSS file
    # --intervalNum is a plain integer version of interval
    # --basinin, basinout, pdatafile, dssfile, osDssFile, and inputFileName
    #   specify file names for files used in the model run. osDssFile is used
    #   only if you want to use a different DSS file to build the storage-outflow
    #   curves. inputFileName is automatically generated and should not be changed.
    self.numHmsModels = 6
    self.interval = "6MIN"
    self.intervalNum = 6
    self.pdatafile = self.hmsProjectPath + "/" + self.hmsProjectName + ".pdata"
    self.dssfile = self.hmsProjectPath + "/" + self.hmsProjectName + ".dss"
    #self.osDssFile = self.osHmsProjectPath + "/" + self.hmsProjectName + ".dss"
    # Do not change inputFileName
    self.inputFileName = self.hmsProjectPath + "/" + self.hmsProjectName + "_input.json"

def setme2ras(self):
    # HEC-RAS project configuration data
    # --rasProjectName is the name of the RAS *.dss file
    # --rasPlanName is the plan name that shows up in DSSVue when you look
    #   at the DSS file
    # --rasProjectPath is the location of the RAS project files
    # --stationFileName is the location of a text file that lists all the
    #   station names, one per line (usually the home directory of a watershed)
    #self.rasProjectName = "Base_and_Calibration"
    self.rasPlanName = "EX100yr24hr"
    self.stationFileName = self.modelPath + self.rasProjectName + "_StationList.txt"

    return self