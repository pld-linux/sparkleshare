
%define		_beta	beta1
Summary:	Sparkleshare is a file sharing and colaborating tool
Summary(pl.UTF-8):	Sparkleshare to narzędzie do współdzielenia plików
Name:		sparkleshare
Version:	0.2
Release:	0.%{_beta}.2
License:	GPL v3
Group:		Applications/File
Source0:	http://sparkleshare.org/%{name}-%{version}-%{_beta}.tar.gz
# Source0-md5:	5dec96cac3459f6b6df4b0418f8ed274
URL:		https://sparkleshare.org
BuildRequires:	dotnet-gtk-sharp2-devel
BuildRequires:	dotnet-ndesk-dbus-glib-sharp-devel
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	mono-csharp
BuildRequires:	nautilus-python
BuildRequires:	pkgconfig
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	dotnet-gtk-sharp2
Requires:	dotnet-ndesk-dbus-glib-sharp
Requires:	git-core
Requires:	mono
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sparkleshare is a file sharing and colaborating tool inspired by
Dropbox.

%description -l pl.UTF-8
Sparkleshare to narzędzie do współdzielenia plików i pracy grupowej
zainspirowane Dropboksem.

%package plugin-nautilus
Summary:	The sparkleshare plugin for nautilus
Summary(pl.UTF-8):	Wtyczka sparkleshare do nautilusa
Group:		X11/Applications
Requires:	nautilus-python

%description plugin-nautilus
This package contains the sparkleshare Nautilus plugin

%description plugin-nautilus -l pl.UTF-8
Ten pakiet zawiera wtyczke sparkleshare do Nautilusa

%prep
%setup -q -n %{name}-%{version}-%{_beta}

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root)  %{_bindir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/folder-sparkleshare.png
%{_libdir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_pixmapsdir}/side-splash.png

%files plugin-nautilus
%defattr(644,root,root,755)
%{_libdir}/nautilus/extensions-2.0/python/sparkleshare-nautilus-extension.py
