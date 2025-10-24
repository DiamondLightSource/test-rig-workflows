from argparse import ArgumentParser

import h5py
from visr_reconstruction import visr_reconstruction
from typing import Optional
import fsspec


def _main(args: Optional[list[str]] = None):
    parser = ArgumentParser()
    parser.add_argument("--output-file", "-o", type=str, default="")
    parser.add_argument("input-file", "-o", type=str, default="")
    parsed_args = parser.parse_args(args)
    input_file_path = parsed_args.input_file
    output_file_path = parsed_args.output_file
    with h5py.File(input_file_path, "r") as input_file:
        reconstructed_data = visr_reconstruction(input_file)
        with fsspec.open(output_file_path, "wb") as output_file:
            output_file.write(reconstructed_data.reconstructed_image)
    return


if __name__ == "__main__":
    _main()
