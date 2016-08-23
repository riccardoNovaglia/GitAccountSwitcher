from unittest import TestCase

import mock
from gitSwitch.helpers.git_config import GitConfig
from mock import patch, MagicMock
from util import files_IO


class TestGithubHelper(TestCase):
    @patch('ConfigParser.ConfigParser')
    def test_should_read_the_given_config_path_when_built(self, mock_parser):
        files_IO.get_file_object_like = mock.Mock(return_value="")
        mock_parser.side_effect = MagicMock()
        config_parser_mock = mock_parser.return_value

        # when
        GitConfig('')

        self.assertTrue(config_parser_mock.called)
