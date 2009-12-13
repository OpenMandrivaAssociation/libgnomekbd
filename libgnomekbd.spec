%define major 4
%define libname	%mklibname gnomekbd  %{major}
%define libnamedev %mklibname -d gnomekbd

Summary: GNOME keyboard libraries
Name: libgnomekbd
Version: 2.28.2
Release: %mkrel 1
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
License: LGPLv2+
Group: System/Libraries
Url: http://www.gnome.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: dbus-glib-devel
BuildRequires: desktop-file-utils
BuildRequires: gtk2-devel
BuildRequires: libglade2.0-devel
BuildRequires: libGConf2-devel
BuildRequires: libxklavier-devel >= 4.0
BuildRequires: intltool

%description
GNOME keyboard indicator plugin

%package common
Summary: Files used by GNOME keyboard libraries
Group: %{group}
Conflicts:	%{name} < 2.1.90-2mdv
Conflicts:	gnome-control-center < 2.18.0

%description common
Files used by GNOME keyboard library

%package -n %{libname}
Summary:	Dynamic libraries for GNOME applications
Group:		%{group}
Requires:	%{name}-common >= %{version}

%description -n %{libname}
GNOME keyboard library

%package -n %{libnamedev}
Summary:	Static libraries, include files for GNOME
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Obsoletes: %mklibname -d gnomekbd 1

%description -n %{libnamedev}
Static library and headers file needed in order to develop
applications using the GNOME keyboard library

%prep
%setup -q -n %{name}-%{version}

%build

%configure2_5x
%make LIBS=-lm

%install
rm -rf $RPM_BUILD_ROOT

GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std

%find_lang %name
desktop-file-install --vendor="" \
  --remove-category="AdvancedSettings" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-System-Configuration-GNOME" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*


%clean
rm -rf $RPM_BUILD_ROOT

%define schemas desktop_gnome_peripherals_keyboard_xkb

%post common
%post_install_gconf_schemas %{schemas}

%preun common
%preun_uninstall_gconf_schemas %{schemas}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
  
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files 
%defattr(-,root,root)
%doc NEWS ChangeLog
%_bindir/gkbd-indicator-plugins-capplet
%_datadir/applications/gkbd-indicator-plugins-capplet.desktop
%_datadir/libgnomekbd/

%files common -f %name.lang
%defattr(-,root,root)
%{_sysconfdir}/gconf/schemas/desktop_gnome_peripherals_keyboard_xkb.schemas

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libgnomekbd*.so.%{major}*

%files -n %{libnamedev}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%attr(644,root,root) %{_libdir}/*.la
%{_libdir}/*.a
