%define major 1
%define libname	%mklibname gnomekbd  %{major}

Summary: GNOME keyboard libraries
Name: libgnomekbd
Version: 2.18.0
Release: %mkrel 1
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2

License: LGPL
Group: System/Libraries
Url: http://www.gnome.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: dbus-glib-devel
BuildRequires: desktop-file-utils
BuildRequires: libgnomeui2-devel
BuildRequires: libglade2.0-devel
BuildRequires: libxklavier-devel
BuildRequires: perl-XML-Parser

%description
GNOME keyboard indicator plugin


%package -n %{libname}
Summary:	Dynamic libraries for GNOME applications
Group:		%{group}

%description -n %{libname}
GNOME keyboard library

%package -n %{libname}-devel
Summary:	Static libraries, include files for GNOME
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}

%description -n %{libname}-devel
Static library and headers file needed in order to develop
applications using the GNOME keyboard library

%prep
%setup -q -n %{name}-%{version}

%build

%configure2_5x
%make

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

%post
%post_install_gconf_schemas desktop_gnome_peripherals_keyboard_xkb
%update_icon_cache hicolor

%preun
%preun_uninstall_gconf_schemas desktop_gnome_peripherals_keyboard_xkb

%postun
%clean_icon_cache hicolor

%post -n %{libname} -p /sbin/ldconfig
  
%postun -n %{libname} -p /sbin/ldconfig

%files -f %name.lang
%defattr(-,root,root)
%doc NEWS ChangeLog
%{_sysconfdir}/gconf/schemas/desktop_gnome_peripherals_keyboard_xkb.schemas
%_bindir/gkbd-indicator-plugins-capplet
%_datadir/applications/gkbd-indicator-plugins-capplet.desktop
%_datadir/libgnomekbd/
%_datadir/icons/hicolor/48x48/apps/gkbd-indicator-plugins-capplet.png

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libgnomekbd*.so.%{major}*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%attr(644,root,root) %{_libdir}/*.la
%{_libdir}/*.a


