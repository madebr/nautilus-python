nautiluspython_sources = files(
	'nautilus-python.c',
	'nautilus-python.h',
	'nautilus-python-object.c',
	'nautilus-python-object.h'
)

nautiluspython_deps = [
    nautilus_extension,
    pygobject,
    python,
]

nautiluspython = shared_module('nautilus-python',
    nautiluspython_sources,
    dependencies: nautiluspython_deps,
    include_directories: nautilus_python_include_dirs,
)
