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
install -d $RPM_BUILD_ROOT/{usr/X11R6/{bin,share/wmcdplay},etc/X11/wmconfig}

install wmcdplay $RPM_BUILD_ROOT/usr/X11R6/bin
install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/wmcdplay

cp -a XPM/*.art $RPM_BUILD_ROOT/usr/X11R6/share/wmcdplay

strip $RPM_BUILD_ROOT/usr/X11R6/bin/wmcdplay

gzip -9nf README ARTWORK

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,ARTWORK}.gz
/etc/X11/wmconfig/wmcdplay
%attr(755,root,root) /usr/X11R6/bin/wmcdplay

/usr/X11R6/share/wmcdplay

%changelog
* Sat May 15 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [1.0Beta1-2]
- modified a bit spec file for PLD use,
- added wmcdpaly-lib.patch,
- fixed permissions,
- package is FHS 2.0 compliant.

* Mon Nov 16 1998 Fryguy_ <fryguy@falsehope.com>
  [wmcdplay-1.0Beta1-1]
- Added setuid bit on wmcdplay binary so non root users can access
  the /dev/cdrom.
- Release 1.0 Beta1 05/09/98
  - Added some error checking.
  - "-a artwork_file" is now "-f artwork_file", sorry ;-).
  - Added "-a" command line argument for AfterStep users.
  - Added "-position position" command line argument.
  - Command line arguments, "-a", "-w" and "-s" are now toggle,
     so if you enable one at compile-time, you can override
     it at run-time.
  - Track selection actually works now??
      (anyone notice a recurring theme here??)
  - Seperate update interval for when drive is empty.
      (thanks to .....)
  - Fixed problem with (some?) SCSI devices refusing to
      give LBA values. Thanks to the linux ide-scsi-emulator.
  - Now looks in some known directories for artwork files as
      a last resort.
  - Improved artwork loading (it was very brain-dead).
  - Formatting changes in artwork files (ARTWORK documentation
      is now up-to-date).
