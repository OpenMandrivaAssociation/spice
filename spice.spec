%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	Berkeley SPICE 3 Circuit Simulator
Name:		spice
Version:	3f5
Release:	17
License:	BSD
URL:		https://www.ibiblio.org/pub/Linux/apps/circuits/
Group:		Sciences/Other
Source:		%{name}%{version}sfix.tar.bz2
Patch0:		%{name}-linux.conf.patch
Patch1:		%{name}-3.5.5-gcc-4.1.patch
BuildRequires:	termcap-devel
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(xaw7)

%description
SPICE 3 is a general-purpose circuit simulation program for nonlinear
dc, nonlinear transient, and linear ac analyses.  Circuits may contain
resistors, capacitors, inductors, mutual inductors, independent
voltage and current sources, four types of dependent sources,
transmission lines, and the four most common semiconductor devices:
diodes, BJT's, JFET's, and MOSFET's.

This version includes support for the Bsim3 model (V3.1)

%prep
%setup -q -n %{name}%{version}sfix

%patch0 -p1 -b .linux-conf
%patch1 -p1 -b .gcc41

%build
./util/build linux gcc

# install has to be done by hand, because we are not assured
# that the builder has root privileges - things would be easier
# if spice had autoconf!

%install
install -d  %{buildroot}%{_bindir}
install -d  %{buildroot}%{_datadir}/%{name}/scripts
install -d  %{buildroot}%{_datadir}/%{name}/helpdir

install -d  %{buildroot}%{_mandir}/man1

install obj/bin/spice3 %{buildroot}%{_bindir}
ln -s /usr/bin/spice3 %{buildroot}%{_bindir}/spice
install obj/bin/help %{buildroot}%{_bindir}
install obj/bin/nutmeg %{buildroot}%{_bindir}
install obj/bin/sconvert %{buildroot}%{_bindir}
install obj/bin/multidec %{buildroot}%{_bindir}
install obj/bin/proc2mod %{buildroot}%{_bindir}

rm lib/make*
cp -r lib/* %{buildroot}%{_datadir}/%{name}

obj/bin/makeidx %{buildroot}%{_datadir}/%{name}/helpdir/spice.txt
install -m 644 man/man1/* %{buildroot}%{_mandir}/man1

chmod 644 3f5patches/README*

%files
%defattr(-,root,root,0755)
%doc readme readme.Linux notes/spice2
%doc 3f5patches/README*
%{_datadir}/%{name}
%{_bindir}/*
%{_mandir}/man1/*

