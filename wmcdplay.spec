Summary:	CD player applet for WindowMaker
Summary(pl):	Dokowalny odtwarzacz CD dla WindowMakera
Name:		wmcdplay
Version:	1.0Beta1
Release:	6
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://www.geocities.com/SiliconValley/Vista/2471/%{name}.tgz
Source1:	%{name}.desktop
Patch0:		%{name}-c++.patch.gz
Patch1:		%{name}-lib.patch
Patch2:		%{name}-ComplexProgramTargetNoMan.patch
Icon:		wmcdplay.gif
URL:		http://www.geocities.com/SiliconValley/Vista/2471/wmcdplay.html
BuildRequires:	XFree86-devel
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
%patch2 -p1

%build
xmkmf
%{__make} \
	CC=%{__cc} \
	CXX=%{__cc} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}} \
        $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

install %{name} $RPM_BUILD_ROOT%{_bindir}
#install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

cp -a XPM/*.art $RPM_BUILD_ROOT%{_datadir}/%{name}

gzip -9nf README ARTWORK

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%doc *.gz

#%{_applnkdir}/DockApplets/wmcdplay.desktop
