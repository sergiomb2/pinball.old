Name:           pinball
Version:        0.3.2
Release:        1%{?dist}
Summary:        Emilia arcade game
Group:          Amusements/Games
License:        GPL+
URL:            http://pinball.sourceforge.net
# git archive --prefix="pinball-0.3.2/" --format=tar master | gzip - > ../pinball-0.3.2.tar.gz
Source0:        http://downloads.sourceforge.net/pinball/%{name}-%{version}.tar.gz
BuildRequires:  libXt-devel freeglut-devel SDL_image-devel SDL_mixer-devel
BuildRequires:  libpng-devel libvorbis-devel libtool-ltdl-devel
BuildRequires:  desktop-file-utils
BuildRequires:  autoconf automake libtool
Requires:       hicolor-icon-theme opengl-games-utils

%description
The Emilia Pinball project is an open source pinball simulator for linux
and other unix systems. The current release is a stable and mature alpha.
There is only one level to play with but it is however very addictive.


%prep
%setup -q
# cleanup a bit
chmod -x data/*/Module*.cpp
autoreconf -fiv


%build
%configure --without-included-ltdl --disable-static
make


%install
make DESTDIR=$RPM_BUILD_ROOT INSTALL="%{__install} -p" install
ln -s opengl-game-wrapper.sh $RPM_BUILD_ROOT%{_bindir}/%{name}-wrapper
sed -i 's/Exec=pinball/Exec=pinball-wrapper/g' pinball.desktop

# remove unused global higescorefiles:
rm -fr $RPM_BUILD_ROOT%{_localstatedir}
# remove unused test module
rm $RPM_BUILD_ROOT%{_libdir}/%{name}/libModuleTest.*
# remove bogus development files
rm $RPM_BUILD_ROOT%{_bindir}/%{name}-config
rm -r $RPM_BUILD_ROOT%{_includedir}/%{name}

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{name}.desktop
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 %{name}.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -p -m 0644 -t %{buildroot}%{_datadir}/pixmaps \
    data/%{name}.xpm

%post
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%postun
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi


%files
%doc README ChangeLog
%license COPYING
%{_bindir}/%{name}*
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.xpm


%changelog
* Wed Jul 22 2015 Sérgio Basto <sergio@serjux.com> - 0.3.2-1
- Update to github version (https://github.com/sergiomb2/pinball).

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 01 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.3.1-24
- Run autoreconf to fix FTBFS on aarch64 (#926341)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 11 2013 Jon Ciesla <limburgher@gmail.com> - 0.3.1-21
- Drop desktop vendor tag.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-19
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 15 2010 Jon Ciesla <limb@jcomserv.net> - 0.3.1-16
- Fix FTBFS, BZ 631379.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 02 2009 Jon Ciesla <limb@jcomserv.net> - 0.3.1-14
- Patch for strict prototypes.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Nov 24 2008 Jon Ciesla <limb@jcomserv.net> - 0.3.1-12
- Cleaned up summary.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.3.1-11
- Autorebuild for GCC 4.3

* Sun Oct 21 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3.1-10
- Drop the bogus -devel package (also fixing the multilib conficts caused by
  it, bz 342881)

* Mon Sep 24 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3.1-9
- Use opengl-games-utils wrapper to show error dialog when DRI is missing

* Wed Aug 15 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3.1-8
- Update License tag for new Licensing Guidelines compliance

* Sat Mar 10 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3.1-7
- Fixup .desktop file categories for games-menus usage

* Mon Aug 28 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3.1-6
- FE6 Rebuild

* Thu Aug 10 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3.1-5
- Add missing rm -rf $RPM_BUILD_ROOT to %%install

* Fri Aug  4 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3.1-4
- Make building use / honor $RPM_OPT_FLAGS
- Add missing BR: libtool-ltdl-devel
- Remove %%{?_smp_mflags} as that breaks building when actually set

* Thu Aug  3 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3.1-3
- Cleaned up specfile for Fedora Extras submission, based on Che's newrpms spec
- Use system ltdl

* Sat Apr 05 2003 che
- upgrade to version 0.2.0a

* Mon Mar 03 2003 Che
- upgrade to version 0.1.3

* Mon Nov 04 2002 Che
- upgrade to version 0.1.1

* Wed Oct 30 2002 Che
- initial rpm release
