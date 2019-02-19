import FWCore.ParameterSet.Config as cms

from HLTrigger.PhaseII.Producers.hltIter2IterL3FromL1MuonClustersRefRemoval_cfi import *
from HLTrigger.PhaseII.Producers.hltIter2IterL3FromL1MuonMaskedMeasurementTrackerEvent_cfi import *
from HLTrigger.PhaseII.Producers.hltIter2IterL3FromL1MuonPixelLayerTriplets_cfi import *
from HLTrigger.PhaseII.Producers.hltIter2IterL3FromL1MuonPixelClusterCheck_cfi import *
from HLTrigger.PhaseII.Producers.hltIter2IterL3FromL1MuonPixelHitDoublets_cfi import *
from HLTrigger.PhaseII.Producers.hltIter2IterL3FromL1MuonPixelHitTriplets_cfi import *
from HLTrigger.PhaseII.Producers.hltIter2IterL3FromL1MuonPixelSeeds_cfi import *
from HLTrigger.PhaseII.Producers.hltIter2IterL3FromL1MuonCkfTrackCandidates_cfi import *
from HLTrigger.PhaseII.Producers.hltIter2IterL3FromL1MuonCtfWithMaterialTracks_cfi import *
from HLTrigger.PhaseII.Producers.hltIter2IterL3FromL1MuonTrackCutClassifier_cfi import *
from HLTrigger.PhaseII.Producers.hltIter2IterL3FromL1MuonTrackSelectionHighPurity_cfi import *

HLTIterativeTrackingIteration2ForIterL3FromL1Muon = cms.Sequence(hltIter2IterL3FromL1MuonClustersRefRemoval+hltIter2IterL3FromL1MuonMaskedMeasurementTrackerEvent+hltIter2IterL3FromL1MuonPixelLayerTriplets+hltIter2IterL3FromL1MuonPixelClusterCheck+hltIter2IterL3FromL1MuonPixelHitDoublets+hltIter2IterL3FromL1MuonPixelHitTriplets+hltIter2IterL3FromL1MuonPixelSeeds+hltIter2IterL3FromL1MuonCkfTrackCandidates+hltIter2IterL3FromL1MuonCtfWithMaterialTracks+hltIter2IterL3FromL1MuonTrackCutClassifier+hltIter2IterL3FromL1MuonTrackSelectionHighPurity)
