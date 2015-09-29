Postman Dump Processor
----------------------

This is a simple Python script to extract collections from `Postman's Dump files
<https://www.getpostman.com/docs/settings>`_. (Check the "Dump" section in the docs.)

Usage is self-explanatory:

.. code-block:: shell

    $ python process.py -h
    usage: process.py [-h] -f DUMP_FILE -o OUTPUT_FOLDER

    optional arguments:
      -h, --help            show this help message and exit
      -f DUMP_FILE, --dump-file DUMP_FILE
                            Path to Postman Dump file.
      -o OUTPUT_FOLDER, --output-folder OUTPUT_FOLDER
                            Path to output folder where collections will go. (Make
                            sure this exists)
