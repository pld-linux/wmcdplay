Summary: 	CD player applet for WindowMaker
Summary(pl):	Dokowalny odtwarzacz CD dla WindowMakera
Name:		wmcdplay
Version:	1.0Beta1
Release:	2
Group:          X11/Window Managers/Tools
Group(pl):      X11/Zarz±dcy Okien/Narzêdzia
Copyright: 	GPL
URL: 		http://www.geocities.com/SiliconValley/Vista/2471/wmcdplay.htm
Source0: 	http://www.geocities.com/SiliconValley/Vista/2471/%{name}.tgz
Source1: 	wmcdplay.wmconfig
Icon:           wmcdplay.gif
Patch0:		wmcdplay-c++.patch.gz
Patch1:		wmcdplay-lib.patch
BuildPrereq:	XFree86-devel
BuildPrereq:	xpm-devel
Buildroot: 	/tmp/%{name}-%{version}-root

%define _prefix	/usr/X11R6

%description 
Wmcdplay is a CD player applet designed for the Windowmaker dock.

%description -l pl
Wmcdplay jest odtwarzaczem p³yt CD, zaprojektowanym dla Doku WindowMakera.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p0

%build
xmkmf
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}} \
        $RPM_BUILD_ROOT/etc/X11/wmconfig

install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/%{name}

cp -a XPM/*.art $RPM_BUILD_ROOT%{_datadir}/%{name}

strip $RPM_BUILD_ROOT%{_bindir}/*

gzip -9nf README ARTWORK

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,ARTWORK}.gz
/etc/X11/wmconfig/%{name}
%attr(755,root,root) %{_bindir}/%{name}

%{_datadir}/%{name}

%changelog
* Sat May 15 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [1.0Beta1-2]
- package is FHS 2.0 compliant,
- modified spec file for PLD use,
- based on spec written by Fryguy_ <fryguy@falsehope.com>.
