#!/usr/bin/env python
#
# The MIT License (MIT)
#
# Copyright (c) 2015 Aniket Panse <aniket@getpostman.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


import argparse
import json
import os

def main(options):
    with open(options.dump_file, 'r') as dump_file:
        dump = json.load(dump_file)
        for collection in dump['collections']:
            print('Found collection: ' + collection['name'])
            stripped_name = ''.join(e for e in collection['name'] if e.isalnum()) + '.postman_collection'
            collection_file_path = os.path.join(options.output_folder, stripped_name)
            with open(collection_file_path, 'w') as collection_file:
                json.dump(collection, collection_file, indent=4)
                print('Created collection file: ' + collection_file_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--dump-file', required=True, help='Path to Postman Dump file.')
    parser.add_argument('-o', '--output-folder', required=True, help='Path to output folder where collections will go. (Make sure this exists)')
    args = parser.parse_args()

    main(args)
    print('All done!')
