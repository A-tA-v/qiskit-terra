# This code is part of Qiskit.
#
# (C) Copyright IBM 2021.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""
Fake Washington device (127 qubit).
"""

import os
from qiskit.test.mock import fake_qasm_backend


class FakeWashington(fake_qasm_backend.FakeQasmBackend):
    """A fake 127 qubit backend."""

    dirname = os.path.dirname(__file__)
    conf_filename = "conf_washington.json"
    props_filename = "props_washington.json"
    backend_name = "fake_washington"
