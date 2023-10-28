#!/usr/bin/env python3
# MIT No Attribution
# 
# Copyright 2022 (c) Ilya Sotkov
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this
# software and associated documentation files (the "Software"), to deal in the Software
# without restriction, including without limitation the rights to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import os
import re
import sys


def main():
    workspace_path = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
    devcontainer_config_file_path = find_devcontainer_config_file_path(workspace_path)
    remote_workspace_folder = get_remote_workspace_folder(devcontainer_config_file_path)
    workspace_path_hex = workspace_path.encode().hex()
    folder_uri = "vscode-remote://dev-container+" + workspace_path_hex + remote_workspace_folder
    print(folder_uri)


def find_devcontainer_config_file_path(workspace_path):
    paths = [
        os.path.join(workspace_path, ".devcontainer.json"),
        os.path.join(workspace_path, ".devcontainer", "devcontainer.json"),
    ]
    for path in paths:
        if os.path.isfile(path):
            return path
    raise OSError("Could not find dev container config file in any of: " + ", ".join(paths))


def get_remote_workspace_folder(config_path):
    config = open(config_path).read()
    pattern = r'"workspaceFolder"\s*:\s*"(.+)"'
    found = re.search(pattern, config)
    if not found:
        raise KeyError(
            "Could not find 'workspaceFolder' setting in your dev container config file!"
        )
    return found.group(1)


if __name__ == "__main__":
    main()
