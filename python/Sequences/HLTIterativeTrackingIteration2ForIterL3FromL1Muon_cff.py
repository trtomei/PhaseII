import FWCore.ParameterSet.Config as cms

process.load('HLTrigger.PhaseII.Producers.hltIter2IterL3FromL1MuonClustersRefRemoval_cfi')
process.load('HLTrigger.PhaseII.Producers.hltIter2IterL3FromL1MuonMaskedMeasurementTrackerEvent_cfi')
process.load('HLTrigger.PhaseII.Producers.hltIter2IterL3FromL1MuonPixelLayerTriplets_cfi')
process.load('HLTrigger.PhaseII.Producers.hltIter2IterL3FromL1MuonPixelClusterCheck_cfi')
process.load('HLTrigger.PhaseII.Producers.hltIter2IterL3FromL1MuonPixelHitDoublets_cfi')
process.load('HLTrigger.PhaseII.Producers.hltIter2IterL3FromL1MuonPixelHitTriplets_cfi')
process.load('HLTrigger.PhaseII.Producers.hltIter2IterL3FromL1MuonPixelSeeds_cfi')
process.load('HLTrigger.PhaseII.Producers.hltIter2IterL3FromL1MuonCkfTrackCandidates_cfi')
process.load('HLTrigger.PhaseII.Producers.hltIter2IterL3FromL1MuonCtfWithMaterialTracks_cfi')
process.load('HLTrigger.PhaseII.Producers.hltIter2IterL3FromL1MuonTrackCutClassifier_cfi')
process.load('HLTrigger.PhaseII.Producers.hltIter2IterL3FromL1MuonTrackSelectionHighPurity_cfi')

HLTIterativeTrackingIteration2ForIterL3FromL1Muon = cms.Sequence(process.hltIter2IterL3FromL1MuonClustersRefRemoval+process.hltIter2IterL3FromL1MuonMaskedMeasurementTrackerEvent+process.hltIter2IterL3FromL1MuonPixelLayerTriplets+process.hltIter2IterL3FromL1MuonPixelClusterCheck+process.hltIter2IterL3FromL1MuonPixelHitDoublets+process.hltIter2IterL3FromL1MuonPixelHitTriplets+process.hltIter2IterL3FromL1MuonPixelSeeds+process.hltIter2IterL3FromL1MuonCkfTrackCandidates+process.hltIter2IterL3FromL1MuonCtfWithMaterialTracks+process.hltIter2IterL3FromL1MuonTrackCutClassifier+process.hltIter2IterL3FromL1MuonTrackSelectionHighPurity)