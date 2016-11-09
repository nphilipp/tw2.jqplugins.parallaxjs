import os
from distutils import log
from shutil import copyfile, rmtree

from setuptools import find_packages, setup
from setuptools.command.build_py import build_py
from setuptools.command.develop import develop


_extra_genshi = ["Genshi >= 0.3.5"]
_extra_kajiki = ["kajiki >= 0.5.0"]


install_requires = [
    "tw2.core >= 2.0",
    "tw2.jquery >= 2.0",
]

tests_require = [
    "nose",
    "sieve",
    "coverage",
    "WebTest",
] + (
    _extra_genshi +
    _extra_kajiki
)


class generate_files_mixin(object):

    here = os.path.abspath(os.path.dirname(__file__))

    pxdir = os.path.join(here, "parallax.js")

    pymodroot = os.path.join("tw2", "jqplugins", "parallaxjs")
    staticdir = os.path.join(pymodroot, "static")

    def generate_distribution(self):
        log.info("Copying static files")

        if os.path.exists(self.staticdir):
            rmtree(self.staticdir)
        os.makedirs(self.staticdir)

        for fname in ("parallax.js", "parallax.min.js"):
            copyfile(os.path.join(self.pxdir, fname),
                     os.path.join(self.staticdir, fname))


class my_build_py(build_py, generate_files_mixin):

    def run(self):
        if not self.dry_run:
            self.generate_distribution()
        build_py.run(self)


class my_develop(develop, generate_files_mixin):

    def install_for_development(self):
        self.generate_distribution()
        develop.install_for_development(self)

    def uninstall_link(self):
        develop.uninstall_link(self)

        log.info("removing generated files: {}".format(self.staticdir))
        rmtree(self.staticdir)


setup(
    name="tw2.jqplugins.parallaxjs",
    version="1.4.2",
    description="ToscaWidgets 2 wrapper for parallax.js",
    author="Nils Philippsen",
    author_email="nils@tiptoe.de",
    #url=
    #download_url=
    install_requires=install_requires,
    tests_require=tests_require,
    test_suite="nose.collector",
    packages=find_packages(),
    namespace_packages=['tw2', 'tw2.jqplugins'],
    zip_safe=False,
    include_package_data=True,
    package_data={"tw2.jqplugins.parallaxjs": ["static/*"]},
    entry_points="""
        [tw2.widgets]
        widgets = tw2.jqplugins.parallaxjs
    """,
    keywords=["tw2.widgets"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Environment :: Web Environment :: ToscaWidgets",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Widget Sets",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    cmdclass={
        'build_py': my_build_py,
        'develop': my_develop,
    },
)
