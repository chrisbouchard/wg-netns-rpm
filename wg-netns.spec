Name: wg-netns
Version: 2.0.1
Release: 3%{?dist}
BuildArch: noarch
Summary: WireGuard with Linux Network Namespaces
License: MIT

Source: https://github.com/dadevel/wg-netns/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: systemd-rpm-macros

Requires: /sbin/ip
Requires: /usr/bin/wg
Requires: python3 >= 3.7

Recommends: python3-pyyaml

%description
wg-quick with support for Linux network namespaces. A simple Python script that
implements the steps described at wireguard.com/netns.

%prep
%autosetup

%install
install --mode=755 --directory %{buildroot}%{_sbindir}
install --mode=755 wg-netns.py %{buildroot}%{_sbindir}/wg-netns

install --mode=755 --directory %{buildroot}%{_unitdir}
install --mode=644 wg-netns@.service %{buildroot}%{_unitdir}/wg-netns@.service

install --mode=700 --directory %{buildroot}%{_sysconfdir}/wireguard

%post
%systemd_post wg-netns@.service

%preun
%systemd_preun wg-netns@.service

%postun
%systemd_postun wg-netns@.service

%files
%license LICENSE
%doc README.md
%{_sbindir}/wg-netns
%{_unitdir}/wg-netns@.service
%dir %{_sysconfdir}/wireguard

%changelog
* Fri Sep 23 2022 Chris Bouchard <chris@upliftinglemma.net> - 2.0.1-3
- Added dist tag and changelog
