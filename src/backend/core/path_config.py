#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Path config module for the fastapi backend."""

from __future__ import annotations

import os
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[2]

VERSIONS = os.path.join(ROOT_DIR, 'app', 'alembic', 'versions')

LOGPATH = os.path.join(ROOT_DIR, 'app', 'logs')

DATA_PATH = os.path.join(ROOT_DIR, 'app', 'data')

DB_PATH = os.path.join(ROOT_DIR, 'app', 'db')


