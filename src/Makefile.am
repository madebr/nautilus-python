INCLUDES =						\
	-DG_LOG_DOMAIN=\"Nautilus-Python\"	        \
	-DDATADIR=\"$(datadir)\"			\
	-DLIBDIR=\"$(libdir)\"				\
	-I$(top_srcdir)					\
	-I$(top_builddir)				\
	$(DISABLE_DEPRECATED_CFLAGS)			\
	$(NAUTILUS_PYTHON_CFLAGS)			\
	-DPYTHON_VERSION=\"$(PYTHON_VERSION)\"		\
	-DPY_LIB_LOC="\"$(PYTHON_LIB_LOC)\""		\
	$(PYTHON_INCLUDES)

nautilus_extensiondir=$(NAUTILUS_EXTENSION_DIR)

nautilus_extension_LTLIBRARIES = libnautilus-python.la

libnautilus_python_la_SOURCES =     	\
	nautilus-python.c		\
	nautilus-python.h		\
	nautilus-python-object.c	\
	nautilus-python-object.h

libnautilus_python_la_LDFLAGS = -module -avoid-version
libnautilus_python_la_LIBADD  = $(NAUTILUS_PYTHON_LIBS) $(PYTHON_LIBS)

pyexec_LTLIBRARIES = nautilus.la
pyexecdir = $(NAUTILUS_LIBDIR)/nautilus-python

nautilus_la_LDFLAGS = -module -avoid-version -export-symbols-regex initnautilus
nautilus_la_LIBADD = $(NAUTILUS_PYTHON_LIBS)
nautilus_la_SOURCES = nautilusmodule.c
nodist_nautilus_la_SOURCES = nautilus.c
nautilus.c: nautilus.defs nautilus.override
CLEANFILES = nautilus.c
EXTRA_DIST = nautilus.override nautilus.defs

.defs.c:
	(cd $(srcdir)\
         && $(PYGTK_CODEGEN) \
	    --register $(PYGTK_DEFSDIR)/pango-types.defs \
            --register $(PYGTK_DEFSDIR)/gdk-types.defs \
            --register $(PYGTK_DEFSDIR)/gtk-types.defs \
            --register $(PYGOBJECT_DEFSDIR)/gio-types.defs \
            --register $(PYGOBJECT_DEFSDIR)/unix-types.defs \
            --override $*.override \
            --prefix py$* $*.defs) > gen-$*.c \
        && cp gen-$*.c $*.c \
        && rm -f gen-$*.c
