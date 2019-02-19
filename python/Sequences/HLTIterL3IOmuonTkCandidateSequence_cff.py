import FWCore.ParameterSet.Config as cms

from HLTrigger.PhaseII.Sequences.HLTIterL3MuonRecopixelvertexingSequence_cff import *
from HLTrigger.PhaseII.Sequences.HLTIterativeTrackingIter023ForIterL3Muon_cff import *
from HLTrigger.PhaseII.Producers.hltL3MuonsIterL3IO_cfi import *

HLTIterL3IOmuonTkCandidateSequence = cms.Sequence(HLTIterL3MuonRecopixelvertexingSequence+HLTIterativeTrackingIter023ForIterL3Muon+hltL3MuonsIterL3IO)
