%define name wmcdplay
%define version 1.0Beta1
%define release 1

%define builddir $RPM_BUILD_DIR/%{name}

Summary: CD player applet

Name: %{name}
Version: %{version}
Release: %{release}
Group: X11/Utilities
Copyright: GPL
Vendor: Sam Hawker <shawkie@geocities.com>
Url: http://www.geocities.com/SiliconValley/Vista/2471/wmcdplay.htm
Packager: Fryguy_ <fryguy@falsehope.com>
Distribution: Freshmeat RPMs
Source0: %{name}.tgz
Source1: %{name}.wmconfig
Patch: %{name}-c++.patch.gz
Buildroot: /tmp/%{name}-%{version}-%{release}-root
Icon: %{name}.gif

%changelog
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

%description 
Wmcdplay is a CD player applet designed for the
Windowmaker dock.

%prep

%setup -n %{name}

%patch -p1

%build
xmkmf
make CFLAGS="$RPM_OPT_FLAGS"

%install
if [ -d $RPM_BUILD_ROOT ]; then rm -r $RPM_BUILD_ROOT ; fi
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/{bin,share/wmcdplay}
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
strip %{builddir}/wmcdplay
rm -f %{builddir}/XPM/standard.art
cp %{builddir}/wmcdplay $RPM_BUILD_ROOT/usr/X11R6/bin
cp %{builddir}/XPM/*.art $RPM_BUILD_ROOT/usr/X11R6/share/wmcdplay
cp $RPM_SOURCE_DIR/%{name}.wmconfig $RPM_BUILD_ROOT/etc/X11/wmconfig/%{name}

%files
%doc README ARTWORK COPYING
%attr(644,root,root) %config(missingok) /etc/X11/wmconfig/wmcdplay
%attr(4755,root,root) /usr/X11R6/bin/wmcdplay
%attr(755,root,root) %dir /usr/X11R6/share/wmcdplay
%attr(644,root,root) /usr/X11R6/share/wmcdplay/*.art

%clean
rm -r $RPM_BUILD_ROOT
rm -r %{builddir}
