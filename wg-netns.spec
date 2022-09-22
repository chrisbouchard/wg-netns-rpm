Name: wg-netns
Version: 2.0.1
Release: 1
BuildArch: noarch
Summary: WireGuard with Linux Network Namespaces
License: MIT

%description
wg-quick with support for Linux network namespaces. A simple Python script that
implements the steps described at wireguard.com/netns.

Source0: https://github.com/dadevel/wg-netns/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: systemd-rpm-macros

Requires: /sbin/ip
Requires: /usr/bin/wg
Requires: python3 >= 3.7

Recommends: python3-pyyaml

%prep
%autosetup

%install
install --mode=755 wg-netns.py %{buildroot}%{_sbindir}/wg-netns
install --mode=644 wg-netns@.service %{buildroot}%{_unitdir}/wg-netns@.service

install --mode=700 --directory %{buildroot}%{_sysconfdir}/wireguard

%files
%license LICENSE
%doc README.md
%{_sbindir}/wg-netns
%{_unitdir}/wg-netns@.service
%dir %{_sysconfdir}/wireguard
