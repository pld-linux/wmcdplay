Summary:	CD player applet for WindowMaker
Summary(pl):	Dokowalny odtwarzacz CD dla WindowMakera
Name:		wmcdplay
Version:	1.0Beta1
Release:	4
Group:		X11/Window Managers/Tools
Group(de):	X11/Fenstermanager/Werkzeuge
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
License:	GPL
Source0:	http://www.geocities.com/SiliconValley/Vista/2471/%{name}.tgz
Source1:	%{name}.desktop
Icon:		wmcdplay.gif
URL:		http://www.geocities.com/SiliconValley/Vista/2471/wmcdplay.html
Patch0:		%{name}-c++.patch.gz
Patch1:		%{name}-lib.patch
BuildRequires:	XFree86-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6

%description 
Wmcdplay is a CD player applet designed for the Windowmaker dock.

%description -l pl
Wmcdplay jest odtwarzaczem p³yt CD, zaprojektowanym dla Doku
WindowMakera.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p0

%build
xmkmf
%{__make} CFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions -fno-implicit-templates "

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}} \
        $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

cp -a XPM/*.art $RPM_BUILD_ROOT%{_datadir}/%{name}

gzip -9nf README ARTWORK

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{_applnkdir}/DockApplets/wmcdplay.desktop

%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
