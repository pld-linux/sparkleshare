# TODO
# - use system jquery: %{_datadir}/sparkleshare/html/jquery.js
Summary:	Sparkleshare is a file sharing and colaborating tool
Summary(pl.UTF-8):	Sparkleshare to narzędzie do współdzielenia plików
Name:		sparkleshare
Version:	1.0.0
Release:	0.1
License:	GPL v3
Group:		Applications/File
Source0:	https://github.com/downloads/hbons/SparkleShare/%{name}-linux-%{version}.tar.gz
# Source0-md5:	1f43c873e220a8a8f28ee46b33e4ca19
URL:		https://sparkleshare.org/
BuildRequires:	desktop-file-utils
BuildRequires:	dotnet-gtk-sharp2-devel
BuildRequires:	dotnet-ndesk-dbus-glib-sharp-devel
BuildRequires:	dotnet-notify-sharp-devel >= 0.4.0-4
BuildRequires:	dotnet-webkit-sharp-devel
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	mono-csharp
#BuildRequires:	nautilus-python
BuildRequires:	pkgconfig
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	dotnet-gtk-sharp2
Requires:	dotnet-ndesk-dbus-glib-sharp
Requires:	git-core >= 1.7.12
Requires:	mono
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sparkleshare is a file sharing and colaborating tool inspired by
Dropbox.

SparkleShare is an Open Source collaboration and sharing tool that is
designed to keep things simple and to stay out of your way. It allows
you to instantly sync with Git repositories and is available for Linux
distributions, Mac and Windows.

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
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# unsupported themes
%{__rm} -r $RPM_BUILD_ROOT%{_iconsdir}/ubuntu-mono-dark
%{__rm} -r $RPM_BUILD_ROOT%{_iconsdir}/ubuntu-mono-light
# don't want gnome depencency
%{__rm} $RPM_BUILD_ROOT%{_iconsdir}/gnome/scalable/apps/sparkleshare-symbolic.svg

desktop-file-validate $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
desktop-file-validate $RPM_BUILD_ROOT%{_desktopdir}/%{name}-invite-opener.desktop

#%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database
%update_icon_cache hicolor

%postun
%update_desktop_database
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/sparkleshare.desktop
%{_desktopdir}/sparkleshare-invite-opener.desktop
%{_iconsdir}/hicolor/*/apps/sparkleshare.png
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.dll*
%{_libdir}/%{name}/*.exe*

%if 0
%files plugin-nautilus
%defattr(644,root,root,755)
%{_libdir}/nautilus/extensions-2.0/python/sparkleshare-nautilus-extension.py
%endif
