# TODO
# - use system jquery: %{_datadir}/sparkleshare/html/jquery.js
Summary:	Sparkleshare is a file sharing and colaborating tool
Summary(pl.UTF-8):	Sparkleshare to narzędzie do współdzielenia plików
Name:		sparkleshare
Version:	1.4
Release:	0.1
License:	GPL v3
Group:		Applications/File
Source0:	https://bitbucket.org/hbons/sparkleshare/downloads/%{name}-linux-%{version}.tar.gz
# Source0-md5:	66ae2b680d723f7a8b38e184d3b3dc55
Source1:	https://github.com/hbons/Dazzle/archive/8e0063e/dazzle.tar.gz
# Source1-md5:	d17e3f9ef046424768144e4b13761472
URL:		https://sparkleshare.org/
BuildRequires:	desktop-file-utils
BuildRequires:	dotnet-gtk-sharp3-devel
BuildRequires:	dotnet-ndesk-dbus-glib-sharp-devel
BuildRequires:	dotnet-notify-sharp3-devel >= 3.0
BuildRequires:	dotnet-webkitgtk-sharp
BuildRequires:	gettext-tools
BuildRequires:	intltool
BuildRequires:	mono-csharp
BuildRequires:	pkgconfig
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	dotnet-gtk-sharp2
Requires:	dotnet-ndesk-dbus-glib-sharp
Requires:	git-core >= 1.8
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

%prep
%setup -q -a1
mv Dazzle-*/README README.dazzle
mv Dazzle-*/dazzle.sh .

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -p dazzle.sh $RPM_BUILD_ROOT%{_bindir}/dazzle

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
%doc README.md News.txt README.dazzle
%attr(755,root,root) %{_bindir}/dazzle
%attr(755,root,root) %{_bindir}/sparkleshare
%{_datadir}/%{name}
%{_desktopdir}/sparkleshare.desktop
%{_desktopdir}/sparkleshare-invite-opener.desktop
%{_iconsdir}/hicolor/*/apps/sparkleshare.png
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.dll*
%{_libdir}/%{name}/*.exe*
