from unittest import TestCase

import os
from gitSwitch.util.files_IO import get_file_object_like


class TestFilesIO(TestCase):
    def test_should_get_a_file_like_object_from_a_file(self):
        cwd = os.getcwd()

        object_like = get_file_object_like(cwd)
