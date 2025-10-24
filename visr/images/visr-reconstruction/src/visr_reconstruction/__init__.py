import h5py
from dataclasses import dataclass

__version__ = "0.1.0"


@dataclass(frozen=True)
class VisrReconstructionOutput:
    reconstructed_image: bytes


def visr_reconstruction(input_raw_data: h5py.Group) -> VisrReconstructionOutput:
    return VisrReconstructionOutput(b"")
