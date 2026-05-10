"""Shared pytest setup for Programmatic-PID tests.

Environment variables that affect C-extension behavior must be set before
importing modules that may pull those libraries in transitively.
"""

from __future__ import annotations

import os

# Keep native math libraries single-threaded under pytest for reproducibility.
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")

# Keep optional rendering imports headless when ezdxf draw helpers are present.
os.environ.setdefault("MPLBACKEND", "Agg")
os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
