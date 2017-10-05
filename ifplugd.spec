%define debug_package %{nil}

Summary:      Detect and perform actions when an ethernet cable is (un)plugged.
Name:         ifplugd
Version:      0.28
Release:      1
Copyright:    GPL
Group:        Networking/Daemons
URL:          http://0pointer.de/lennart/projects/ifplugd/
Source:       %{name}-%{version}.tar.gz
Packager:     Diego Santa Cruz <Diego.SantaCruz@epfl.ch>
BuildRoot:    %{_tmppath}/%{name}-%{version}-root
BuildPrereq:  libdaemon-devel

%description
ifplugd is a Linux daemon which will automatically configure your
ethernet device when a cable is plugged in and automatically
unconfigure it if the cable is pulled. This is useful on laptops with
network adapters onboard , since it will only configure the interface
when a cable is really connected.

ifplugd is a rather simplistic approach to this target since it relies
on your distribution's native interface configuration system.

%prep
%setup -q
%build
%configure
make

%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf "$RPM_BUILD_ROOT"
mkdir -p "$RPM_BUILD_ROOT"/usr/sbin
make DESTDIR=$RPM_BUILD_ROOT PREFIX=%{prefix} install

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf "$RPM_BUILD_ROOT"

%post
/sbin/chkconfig --add ifplugd

%preun
/sbin/chkconfig --del ifplugd

%files
%defattr(755,root,root)
%doc LICENSE README
%doc doc/README.html doc/style.css
%{_sbindir}/ifplugd
%{_sbindir}/ifplugstatus
%{_mandir}/man?/ifplugd*
%{_mandir}/man?/ifplugstatus*
%{_sysconfdir}/init.d/ifplugd
%config %{_sysconfdir}/ifplugd/ifplugd.conf
%config %{_sysconfdir}/ifplugd/ifplugd.action

%changelog

* Mon Jul 21 2003 Lennart Poettering 0.16
- Modified slightly to be auto generated by autoconf

* Wed Jul 16 2003 Diego Santa Cruz <Diego.SantaCruz@epfl.ch> 0.15
- Updated to version 0.15
- Make it depend on libdaemon

* Thu Jan  9 2003 Asgeir Nilsen <rpmspec@asgeirnilsen.com> 0.11-2
- Minor adjustments and init file patch