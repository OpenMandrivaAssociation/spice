%define name spice
%define version 3f5
%define release %mkrel 9

Summary: 	Berkeley SPICE 3 Circuit Simulator
Name: 		%name
Version: 	%version
Release: 	%release
License:	BSD
URL:		http://www.ibiblio.org/pub/Linux/apps/circuits/
Group: 		Sciences/Other
Source: 	%{name}%{version}sfix.tar.bz2
Patch0:		%name-linux.conf.patch
Patch1:		%name-3.5.5-gcc-4.1.patch
Buildrequires:	libtermcap-devel
BuildRequires:	libxt-devel 
BuildRequires:	libxaw-devel

%description
SPICE 3 is a general-purpose circuit simulation program for nonlinear
dc, nonlinear transient, and linear ac analyses.  Circuits may contain
resistors, capacitors, inductors, mutual inductors, independent
voltage and current sources, four types of dependent sources,
transmission lines, and the four most common semiconductor devices:
diodes, BJT's, JFET's, and MOSFET's.

This version includes support for the Bsim3 model (V3.1)

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -n %{name}%{version}sfix

%patch0 -p1
%patch1 -p1

sed -i -e "s/LIB = lib/LIB = %_lib/" conf/linux

%build
./util/build linux gcc

obj/bin/makeidx lib/helpdir/spice.txt

# install has to be done by hand, because we are not assured
# that the builder has root privileges - things would be easier
# if spice had autoconf!

%install
install -d  $RPM_BUILD_ROOT%_bindir
install -d  $RPM_BUILD_ROOT%_libdir/spice/scripts
install -d  $RPM_BUILD_ROOT%_libdir/spice/helpdir

#install -d  $RPM_BUILD_ROOT%_libdir/spice/examples

install -d  $RPM_BUILD_ROOT%_mandir/man1
#install -d  $RPM_BUILD_ROOT%_mandir/man3
#install -d  $RPM_BUILD_ROOT%_mandir/man5

install -s obj/bin/spice3 $RPM_BUILD_ROOT%_bindir
ln -s /usr/bin/spice3 $RPM_BUILD_ROOT%_bindir/spice
install -s obj/bin/help $RPM_BUILD_ROOT%_bindir
install -s obj/bin/nutmeg $RPM_BUILD_ROOT%_bindir
install -s obj/bin/sconvert $RPM_BUILD_ROOT%_bindir
install -s obj/bin/multidec $RPM_BUILD_ROOT%_bindir
install -s obj/bin/proc2mod $RPM_BUILD_ROOT%_bindir

rm lib/make*
cp -r lib/* $RPM_BUILD_ROOT%_libdir/spice
#cp -r examples/ $RPM_BUILD_ROOT%_libdir/spice

install -m 644 man/man1/* $RPM_BUILD_ROOT%_mandir/man1
#install -m 644 man/man3/mfb.3 $RPM_BUILD_ROOT%_mandir/man3
#install -m 644 man/man5/mfbcap.5 $RPM_BUILD_ROOT%_mandir/man5

chmod 644 3f5patches/README*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%doc readme readme.Linux notes/spice2
%doc 3f5patches/README*
%_libdir/spice
%_bindir/*
%_mandir/man1/*
#%_mandir/man3/*
#%_mandir/man5/*


