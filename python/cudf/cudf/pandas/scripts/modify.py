# SPDX-FileCopyrightText: Copyright (c) 2025, NVIDIA CORPORATION. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pathlib

FN = (
    pathlib.Path(__file__).parent.parent.parent.parent.parent.parent
    / "pandas-testing/pandas-tests/tests/indexes/categorical/test_category.py"
)

with open(FN) as f:
    lines = f.readlines()

with open(FN, "w") as f:
    for line in lines:
        f.write(line)
        if "test_has_duplicates" in line:
            f.write(
                "        print(f\"In cudf: {pd._fsproxy_fast.get_option('copy_on_write')}\")\n"
            )
            f.write(
                "        print(f\"In pandas: {pd._fsproxy_slow.get_option('mode.copy_on_write')}\")\n"
            )
