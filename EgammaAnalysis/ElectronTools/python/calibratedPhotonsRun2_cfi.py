import FWCore.ParameterSet.Config as cms

from EgammaAnalysis.ElectronTools.calibrationTablesRun2 import correctionType
from EgammaAnalysis.ElectronTools.calibrationTablesRun2 import files

calibratedPhotons = cms.EDProducer("CalibratedPhotonProducerRun2",

                                   # input collections
                                   photons = cms.InputTag('gedPhotons'),
                                   
                                   # data or MC corrections
                                   # if isMC is false, data corrections are applied
                                   isMC = cms.bool(False),
                                   autoDataType = cms.bool(True),
                                   
                                   # set to True to get special "fake" smearing for synchronization. Use JUST in case of synchronization
                                   isSynchronization = cms.bool(False),
                                   minEtToCalibrate = cms.double(5.0),
                                   produceCalibratedPhos = cms.bool(True),
                                   semiDeterministic = cms.bool(True),

                                   correctionFile = cms.string(files[correctionType]),
                                   recHitCollectionEB = cms.InputTag('reducedEcalRecHitsEB'),
                                   recHitCollectionEE = cms.InputTag('reducedEcalRecHitsEE')
                                     
                                   )


