AUTOMAKE_OPTIONS = gnu

highscoredir = $(DESTDIR)/$(EM_BUILD_ROOT)/$(EM_HIGHSCORE_DIR)/professor2

professorlibdir = $(EM_LIBDIR)
professordatadir = $(datadir)/pinball/professor2

professorlib_LTLIBRARIES = libModuleProfessor2.la

INCLUDES = -I../../base -I.../../addon -I../../src

libModuleProfessor2_la_LDFLAGS = -module
libModuleProfessor2_la_SOURCES = ModuleProfessor.cpp

professordata_DATA = \
 $(wildcard *.pbl) \
 $(wildcard *.pcx) \
 $(wildcard *.png) \
 $(wildcard *.jpg) \
 $(wildcard *.wav) \
 $(wildcard *.ogg) \
 $(wildcard *.mid) \
 #

# This will create a new empty highscores file
# NOTE! The user games must exist!
install-data-hook:
	-mkdir -p $(highscoredir) # - if not root #!rzr
	-touch $(highscoredir)/highscores
	-if test `whoami` = root; then chown games $(highscoredir)/highscores; fi
	-if test `whoami` = root; then chgrp games $(highscoredir)/highscores; fi
	-chmod 666 $(highscoredir)/highscores

EXTRA_DIST = $(professordata_DATA)
