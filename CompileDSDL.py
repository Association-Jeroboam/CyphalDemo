#!/usr/bin/env python

import distutils.command.build_py
from pathlib import Path

OUTPATH = "./"
SUBDIR = ""
OUTDIR =".dsdl_compiled"


# noinspection PyUnresolvedReferences

import pycyphal

pycyphal.dsdl.compile_all(
    [
        "public_regulated_data_types/uavcan",  # All Cyphal applications need the standard namespace, always.
        "public_regulated_data_types/reg",  # Many applications also need the non-standard regulated DSDL.
        "jeroboam_datatypes",
    ],
    output_directory=Path(OUTPATH, SUBDIR, OUTDIR),  # Store in the build output archive.
)
