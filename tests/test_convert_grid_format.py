import os

import xtgeo
from xtgeo.common import XTGeoDialog

import xtgeoapp_convgrd3dfmt.cg3f as xx

xtg = XTGeoDialog()
logger = xtg.basiclogger(__name__)

TDX = xtg.tmpdir
if not os.path.exists(TDX):
    os.makedirs(TDX)

rfile1 = "tests/data/REEK.EGRID"
rfile2 = "tests/data/REEK.UNRST"


def test_convert_grid_format_egrid():
    """Convert an ECLIPSE egrid to roff"""

    outfile = os.path.join(TDX, "reek_grid.roff")

    xx.main(["--file", rfile1, "--output", outfile, "--mode", "grid", "--standardfmu"])

    gg = xtgeo.grid3d.Grid(outfile)
    assert gg.nactive == 35838


def test_convert_grid_format_restart():
    """Convert an ECLIPSE SOIL from restart to roff"""

    outfile = os.path.join(TDX, "reek_grid.roff")

    xx.main(
        [
            "--file",
            rfile2,
            "--output",
            outfile,
            "--mode",
            "restart",
            "--propnames",
            "SOIL",
            "--dates",
            "19991201",
            "--standardfmu",
        ]
    )

    assert 1 == 1
