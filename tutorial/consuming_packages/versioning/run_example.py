from test.examples_tools import chdir, run


cmd_out = run('conan remove "zlib/*" -f')
cmd_out = run("conan install . --build=missing")
assert "zlib/[~1.2]: zlib/1.2.12" in cmd_out
