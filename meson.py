#!/usr/bin/env python3

# Copyright 2016 The Meson development team

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from mesonbuild import mesonmain
import sys, os

def main():
    thisfile = __file__
    if not os.path.isabs(thisfile):
        thisfile = os.path.normpath(os.path.join(os.getcwd(), thisfile))
    if __package__ == '':
        thisfile = os.path.dirname(thisfile)

    # The first argument *must* be an absolute path because
    # the user may have launched the program from a dir
    # that is not in path.
    sys.exit(mesonmain.run(thisfile, sys.argv[1:]))

if __name__ == '__main__':
    main()

