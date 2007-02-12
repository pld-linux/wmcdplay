Summary:	CD player applet for WindowMaker
Summary(pl.UTF-8):	Dokowalny odtwarzacz CD dla WindowMakera
Name:		wmcdplay
Version:	1.0Beta1
Release:	8
License:	GPL
Group:		X11/Window Managers/Tools
#Source0:	http://www.geocities.com/SiliconValley/Vista/2471/%{name}.tgz
Source0:	%{name}.tgz
# Source0-md5:	3b84b902186ba65770c268841ca12ae2
Source1:	%{name}.desktop
Patch0:		%{name}-c++.patch.gz
Patch1:		%{name}-lib.patch
Patch2:		%{name}-ComplexProgramTargetNoMan.patch
#URL:		http://www.geocities.com/SiliconValley/Vista/2471/wmcdplay.html
BuildRequires:	XFree86-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wmcdplay is a CD player applet designed for the Windowmaker dock.

%description -l pl.UTF-8
Wmcdplay jest odtwarzaczem płyt CD, zaprojektowanym dla Doku
WindowMakera.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p0
%patch2 -p1

%build
xmkmf
%{__make} \
	CXX="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}} \
	$RPM_BUILD_ROOT%{_desktopdir}/docklets

install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

cp -a XPM/*.art $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ARTWORK
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/docklets/wmcdplay.desktop
