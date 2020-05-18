import os
from scrapy.cmdline import execute

os.chdir(os.path.dirname(os.path.realpath(__file__)))

try:
    execute(
        [
            'scrapy',
            'crawl',
            'uic_spidey',
            '-o',
            'uic_docs.csv',
        ]
    )
except SystemExit:
    pass