AUTOMAKE_OPTIONS = gnu

highscoredir = $(DESTDIR)/$(EM_BUILD_ROOT)/$(EM_HIGHSCORE_DIR)/professor2

professor2libdir = $(EM_LIBDIR)
professor2datadir = $(datadir)/pinball/professor2

professor2lib_LTLIBRARIES = libModuleProfessor2.la

AM_CPPFLAGS = -I../../base -I.../../addon -I../../src

libModuleProfessor2_la_LDFLAGS = -module
libModuleProfessor2_la_SOURCES = ModuleProfessor.cpp

professor2data_DATA = \
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

EXTRA_DIST = $(professor2data_DATA)
