project ('nautilus-python', 'c',
         version: '1.2',
         meson_version: '>=0.40.0',
         license: 'GPL2')

python2_ver = '>=2.7'
python3_ver = '>=3.4'

conf = configuration_data ()
conf.set_quoted('g_log_domain', 'Nautilus-Python')

python_version = get_option('python_version').to_int()
if python_version == 2
    python = dependency ('python', version: python2_ver, method: 'pkg-config')
elif python_version == 3
    python = dependency ('python3', version: python3_ver, method: 'pkg-config')
else
    error('Illegal python version')
endif

conf.set_quoted('python_version', python.version())
conf.set('python_major_version', python.version().split('.')[0])
python_lib_dir = python.get_pkgconfig_variable('libdir')
conf.set_quoted('python_lib_dir', python_lib_dir)

pygobject_version = get_option('pygobject_version').to_int()
if pygobject_version == 2
    pygobject = dependency ('pygobject-2.0')
    conf.set_quoted()
elif pygobject_version == 3
    pygobject = dependency ('pygobject-3.0')
else
    error('Illegal pygobject version')
endif

pygobject_version = pygobject.version().split('.')
conf.set('pygobject_major_version', pygobject_version[0].to_int())
conf.set('pygobject_minor_version', pygobject_version[1].to_int())
conf.set('pygobject_micro_version', pygobject_version[2].to_int())

pygobject_data_dir = pygobject.get_pkgconfig_variable('datadir')
conf.set_quoted('pygobject_data_dir', pygobject_data_dir)

nautilus_extension = dependency ('libnautilus-extension', version: '>3.24')

config_file = configure_file(input: 'config.h.meson',
    output: 'config.h',
    configuration: conf)

nautilus_python_include_dirs = include_directories ('.')

subdir ('src')

if get_option ('enable-gtk-doc')
    subdir ('docs')
endif
