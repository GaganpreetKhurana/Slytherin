import cx_Freeze
executables=[cx_Freeze.Executable("pygame1.py",icon="snake2.ico")]
cx_Freeze.setup(
    name="Slytherin",
    options={"build_exe":{"packages":["pygame"],"include_files":["apple2.png","snake2.png"]}},
    description="Slytherin Game",
    executables=executables
)
#setup.py bdist_msi
#setup.py build
