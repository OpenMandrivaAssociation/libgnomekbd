%define major 8
%define girmajor 3.0

%define libname	%mklibname gnomekbd  %{major}
%define girname	%mklibname gnomekbd-gir  %{girmajor}
%define develname %mklibname -d gnomekbd

Summary: GNOME keyboard libraries
Name: libgnomekbd
Version: 3.6.0
Release: 1
License: LGPLv2+
Group: System/Libraries
Url: http://www.gnome.org/
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/3.6/%{name}-%{version}.tar.xz

BuildRequires: intltool
BuildRequires: chrpath
BuildRequires: pkgconfig(gdk-3.0) >= 2.91.7
BuildRequires: pkgconfig(gio-2.0) >= 2.18
BuildRequires: pkgconfig(glib-2.0) >= 2.18
BuildRequires: pkgconfig(gtk+-3.0) >= 2.90
BuildRequires: pkgconfig(libxklavier) >= 5.1
BuildRequires: pkgconfig(gobject-introspection-1.0) >= 0.6.7

%description
GNOME keyboard indicator plugin

%package common
Summary:	Files used by GNOME keyboard libraries
Group:		%{group}
Obsoletes:	libgnomekbd < 3.4.0

%description common
Files used by GNOME keyboard library

%package -n %{libname}
Summary:	Dynamic libraries for GNOME applications
Group:		%{group}

%description -n %{libname}
GNOME keyboard library

%package -n %{girname}
Summary:	GObject Introspection interface library for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface library for %{name}.

%package -n %{develname}
Summary:	Development libraries, include files for GNOME
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}

%description -n %{develname}
Development library and headers file needed in order to develop
applications using the GNOME keyboard library

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-static \
	-enable-introspection

%make

%install
%makeinstall_std
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%find_lang %{name}

%define schemas desktop_gnome_peripherals_keyboard_xkb

%preun common
%preun_uninstall_gconf_schemas %{schemas}

%files common -f %{name}.lang
%doc NEWS ChangeLog
%{_bindir}/gkbd-keyboard-display
%{_datadir}/applications/gkbd-keyboard-display.desktop
%{_datadir}/GConf/gsettings/libgnomekbd.convert
%{_datadir}/glib-2.0/schemas/org.gnome.libgnomekbd*.gschema.xml
%{_datadir}/libgnomekbd/

%files -n %{libname}
%{_libdir}/libgnomekbd*.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Gkbd-%{girmajor}.typelib

%files -n %{develname}
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_datadir}/gir-1.0/Gkbd-%{girmajor}.gir



%changelog
* Tue Oct  2 2012 Arkady L. Shane <ashejn@rosalab.ru> 3.6.0-1
- update to 3.6.0

* Fri Apr 27 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.4.0.2-1
+ Revision: 793707
- new version 3.4.0.2

* Fri Nov 25 2011 Matthew Dawkins <mattydaw@mandriva.org> 3.2.0-1
+ Revision: 733465
- fixed files lists
- new version 3.2.0
- spec clean up
- disabled static build
- removed .la files
- removed defattr
- removed old ldconfig scriptlets & post_install_gconf_schemas
- removed clean section
- fixed devel summary & description
- removed old obsoletes
- split out gir pkg
- converted BRs to pkgconfig provides
- removed mkrel & BuildRoot

* Sun May 22 2011 Funda Wang <fwang@mandriva.org> 2.32.0-3
+ Revision: 677084
- rebuild to add gconf2 as req

* Fri Apr 29 2011 Funda Wang <fwang@mandriva.org> 2.32.0-2
+ Revision: 660619
- add br

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Tue Sep 28 2010 Götz Waschk <waschk@mandriva.org> 2.32.0-1mdv2011.0
+ Revision: 581606
- update to new version 2.32.0

* Sat Sep 18 2010 Götz Waschk <waschk@mandriva.org> 2.31.92-1mdv2011.0
+ Revision: 579344
- update to new version 2.31.92

* Fri Aug 20 2010 Götz Waschk <waschk@mandriva.org> 2.31.5-2mdv2011.0
+ Revision: 571507
- move ui files to common package (bug #60721)

* Fri Jul 30 2010 Götz Waschk <waschk@mandriva.org> 2.31.5-1mdv2011.0
+ Revision: 563579
- new version

* Wed Jun 23 2010 Frederic Crozat <fcrozat@mandriva.com> 2.30.2-1mdv2010.1
+ Revision: 548661
- Release 2.30.2
- Remove patch0 (merged upstream)

* Mon Jun 21 2010 Frederic Crozat <fcrozat@mandriva.com> 2.30.1-5mdv2010.1
+ Revision: 548386
- Update patch0 with fix for GNOME bug #618709

* Thu May 06 2010 Frederic Crozat <fcrozat@mandriva.com> 2.30.1-4mdv2010.1
+ Revision: 542876
- Patch0 (GIT): various bug fixes (including GNOME bug #617643)

* Wed Apr 28 2010 Frederic Crozat <fcrozat@mandriva.com> 2.30.1-3mdv2010.1
+ Revision: 540436
- Remove libglade2 BR

* Wed Apr 28 2010 Christophe Fergeau <cfergeau@mandriva.com> 2.30.1-2mdv2010.1
+ Revision: 540033
- rebuild so that shared libraries are properly stripped again

* Sat Apr 24 2010 Götz Waschk <waschk@mandriva.org> 2.30.1-1mdv2010.1
+ Revision: 538425
- new version
- drop patch

* Mon Apr 12 2010 Götz Waschk <waschk@mandriva.org> 2.30.0-2mdv2010.1
+ Revision: 533676
- fix default value in schema (bug #58466)

* Mon Mar 29 2010 Funda Wang <fwang@mandriva.org> 2.30.0-1mdv2010.1
+ Revision: 528710
- update to new version 2.30.0

* Tue Mar 09 2010 Götz Waschk <waschk@mandriva.org> 2.29.92-1mdv2010.1
+ Revision: 516896
- update to new version 2.29.92

* Mon Jan 11 2010 Götz Waschk <waschk@mandriva.org> 2.29.5-1mdv2010.1
+ Revision: 489618
- update to new version 2.29.5

* Sun Dec 13 2009 Götz Waschk <waschk@mandriva.org> 2.28.2-1mdv2010.1
+ Revision: 478178
- update to new version 2.28.2

* Wed Sep 23 2009 Götz Waschk <waschk@mandriva.org> 2.28.0-1mdv2010.0
+ Revision: 447634
- update to new version 2.28.0

* Wed Aug 26 2009 Götz Waschk <waschk@mandriva.org> 2.27.91-1mdv2010.0
+ Revision: 421335
- update to new version 2.27.91

* Wed Jul 15 2009 Götz Waschk <waschk@mandriva.org> 2.27.4-1mdv2010.0
+ Revision: 396228
- new version
- drop patch

* Mon Jun 29 2009 Götz Waschk <waschk@mandriva.org> 2.27.2-3mdv2010.0
+ Revision: 390540
- update for new libxklavier
- new major

* Mon May 25 2009 Götz Waschk <waschk@mandriva.org> 2.27.2-1mdv2010.0
+ Revision: 379508
- update to new version 2.27.2

* Sat Mar 14 2009 Götz Waschk <waschk@mandriva.org> 2.26.0-1mdv2009.1
+ Revision: 354971
- update to new version 2.26.0

* Fri Feb 20 2009 Götz Waschk <waschk@mandriva.org> 2.25.91-1mdv2009.1
+ Revision: 343196
- update to new version 2.25.91

* Tue Sep 23 2008 Götz Waschk <waschk@mandriva.org> 2.24.0-1mdv2009.0
+ Revision: 287256
- new version
- update build deps

* Thu Sep 04 2008 Götz Waschk <waschk@mandriva.org> 2.23.91-1mdv2009.0
+ Revision: 280233
- new version
- drop patch

* Thu Jul 03 2008 Götz Waschk <waschk@mandriva.org> 2.23.2-1mdv2009.0
+ Revision: 231002
- new version
- update license
- fix linking

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Mar 19 2008 Götz Waschk <waschk@mandriva.org> 2.22.0-1mdv2008.1
+ Revision: 188800
- new version
- update file list

* Thu Jan 31 2008 Götz Waschk <waschk@mandriva.org> 2.21.4.1-2mdv2008.1
+ Revision: 160686
- rebuild for new libxklavier

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Dec 18 2007 Götz Waschk <waschk@mandriva.org> 2.21.4.1-1mdv2008.1
+ Revision: 132037
- new version
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Oct 25 2007 Götz Waschk <waschk@mandriva.org> 2.21.1-1mdv2008.1
+ Revision: 102206
- new version
- new major

* Mon Oct 01 2007 Frederic Crozat <fcrozat@mandriva.com> 2.20.0-2mdv2008.0
+ Revision: 94124
- Add conflicts to ease upgrade from  2007.0

* Mon Sep 17 2007 Götz Waschk <waschk@mandriva.org> 2.20.0-1mdv2008.0
+ Revision: 89048
- new version

* Sun Aug 26 2007 Götz Waschk <waschk@mandriva.org> 2.19.91-1mdv2008.0
+ Revision: 71593
- new version
- drop patch 1

* Mon Aug 20 2007 Frederic Crozat <fcrozat@mandriva.com> 2.19.90-2mdv2008.0
+ Revision: 67921
- Move schema and translation into a subpackage
- Patch1: fix various crashes (GNOME bugs #466301, 429907)

* Tue Aug 14 2007 Götz Waschk <waschk@mandriva.org> 2.19.90-1mdv2008.0
+ Revision: 63477
- fix buildrequires
- new version
- fix build
- new devel name

* Sun May 20 2007 Götz Waschk <waschk@mandriva.org> 2.18.2-1mdv2008.0
+ Revision: 28935
- new version

* Tue Apr 17 2007 Götz Waschk <waschk@mandriva.org> 2.18.1-1mdv2008.0
+ Revision: 13831
- new version


* Mon Mar 12 2007 Götz Waschk <waschk@mandriva.org> 2.18.0-1mdv2007.1
+ Revision: 141620
- new version

* Thu Mar 01 2007 Götz Waschk <waschk@mandriva.org> 2.17.92-1mdv2007.1
+ Revision: 130284
- new version
- add icon

* Thu Nov 30 2006 Götz Waschk <waschk@mandriva.org> 2.17.2-3mdv2007.1
+ Revision: 89272
- bot rebuild
- rebuild

* Wed Nov 08 2006 Götz Waschk <waschk@mandriva.org> 2.17.2-1mdv2007.1
+ Revision: 78052
- fix desktop entry
- fix buildrequires
- Import libgnomekbd

* Wed Nov 08 2006 Götz Waschk <waschk@mandriva.org> 2.17.2-1mdv2007.1
- initial package

