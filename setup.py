# Template by setupmobans
import os
import sys
import codecs
from shutil import rmtree
from setuptools import setup, find_packages, Command
PY2 = sys.version_info[0] == 2
PY26 = PY2 and sys.version_info[1] < 7

NAME = 'django-excel'
AUTHOR = 'C.W.'
VERSION = '0.0.9'
EMAIL = 'wangc_2011@hotmail.com'
LICENSE = 'New BSD'
DESCRIPTION = (
    'A django middleware that provides one application programming interfac' +
    'e to read and write data in different excel file formats' +
    ''
)
URL = 'https://github.com/pyexcel/django-excel'
DOWNLOAD_URL = '%s/archive/0.0.9.tar.gz' % URL
FILES = ['README.rst',  'CHANGELOG.rst']
KEYWORDS = [
    'API',
    'Django',
    'python'
]

CLASSIFIERS = [
    'Topic :: Office/Business',
    'Topic :: Utilities',
    'Topic :: Software Development :: Libraries',
    'Programming Language :: Python',
    'Intended Audience :: Developers',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'License :: OSI Approved :: BSD License',
    'Development Status :: 3 - Alpha',
    'Environment :: Web Environment',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Framework :: Django :: 1.7',
    'Framework :: Django :: 1.8',
    'Framework :: Django :: 1.9',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5'
]

INSTALL_REQUIRES = [
    'pyexcel-webio>=0.1.2',
    'Django>=1.6.1',
]


PACKAGES = find_packages(exclude=['ez_setup', 'examples', 'tests'])
EXTRAS_REQUIRE = {
    'xls': ['pyexcel-xls>=0.4.0'],
    'xlsx': ['pyexcel-xlsx>=0.4.0'],
    'ods': ['pyexcel-ods3>=0.4.0'],
}
PUBLISH_COMMAND = '{0} setup.py sdist bdist_wheel upload -r pypi'.format(
    sys.executable)
GS_COMMAND = ('gs django-excel v0.0.9 ' +
              "Find 0.0.9 in changelog for more details")
here = os.path.abspath(os.path.dirname(__file__))


class PublishCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package on github and pypi'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds...')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution...')
        if os.system(GS_COMMAND) == 0:
            os.system(PUBLISH_COMMAND)

        sys.exit()


def read_files(*files):
    """Read files into setup"""
    text = ""
    for single_file in files:
        content = read(single_file)
        text = text + content + "\n"
    return text


def read(afile):
    """Read a file into setup"""
    with codecs.open(afile, 'r', 'utf-8') as opened_file:
        content = filter_out_test_code(opened_file)
        content = "".join(list(content))
        return content


def filter_out_test_code(file_handle):
    found_test_code = False
    for line in file_handle.readlines():
        if line.startswith('.. testcode:'):
            found_test_code = True
            continue
        if found_test_code is True:
            if line.startswith('  '):
                continue
            else:
                empty_line = line.strip()
                if len(empty_line) == 0:
                    continue
                else:
                    found_test_code = False
                    yield line
        else:
            for keyword in ['|version|', '|today|']:
                if keyword in line:
                    break
            else:
                yield line


if __name__ == '__main__':
    setup(
        name=NAME,
        author=AUTHOR,
        version=VERSION,
        author_email=EMAIL,
        description=DESCRIPTION,
        url=URL,
        download_url=DOWNLOAD_URL,
        long_description=read_files(*FILES),
        license=LICENSE,
        keywords=KEYWORDS,
        extras_require=EXTRAS_REQUIRE,
        tests_require=['nose'],
        install_requires=INSTALL_REQUIRES,
        packages=PACKAGES,
        include_package_data=True,
        zip_safe=False,
        classifiers=CLASSIFIERS,
        setup_requires=['gease'],
        cmdclass={
            'publish': PublishCommand,
        }
    )
