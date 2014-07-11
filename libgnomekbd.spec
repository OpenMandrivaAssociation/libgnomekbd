%define url_ver %(echo %{version}|cut -d. -f1,2)

%define major	8
%define gimajor	3.0
%define libname	%mklibname gnomekbd  %{major}
%define libui	%mklibname gnomekbdui  %{major}
%define girname	%mklibname gnomekbd-gir  %{gimajor}
%define devname %mklibname -d gnomekbd

Summary:	GNOME keyboard libraries
Name:		libgnomekbd
Version:	3.6.0
Release:	8
License:	LGPLv2+
Group:		System/Libraries
Url:		http://www.gnome.org/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/libgnomekbd/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	pkgconfig(gdk-3.0) >= 2.91.7
BuildRequires:	pkgconfig(gio-2.0) >= 2.18
BuildRequires:	pkgconfig(glib-2.0) >= 2.18
BuildRequires:	pkgconfig(gtk+-3.0) >= 2.90
BuildRequires:	pkgconfig(libxklavier) >= 5.1
BuildRequires:	pkgconfig(gobject-introspection-1.0) >= 0.6.7

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

%package -n %{libui}
Summary:	Dynamic libraries for GNOME applications
Group:		%{group}
Conflicts:	%{_lib}gnomekbd8 < 3.6.0-2

%description -n %{libui}
GNOME keyboard library

%package -n %{girname}
Summary:	GObject Introspection interface library for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface library for %{name}.

%package -n %{devname}
Summary:	Development libraries, include files for GNOME
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libui} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}

%description -n %{devname}
Development library and headers file needed in order to develop
applications using the GNOME keyboard library

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-static \
	--enable-introspection

%make

%install
%makeinstall_std

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
%{_libdir}/libgnomekbd.so.%{major}*

%files -n %{libui}
%{_libdir}/libgnomekbdui.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Gkbd-%{gimajor}.typelib

%files -n %{devname}
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_datadir}/gir-1.0/Gkbd-%{gimajor}.gir

