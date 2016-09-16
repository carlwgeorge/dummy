Name: dummy
Version: 1
Release: 1%{?dist}
Summary: Dummy package
License: MIT
URL: https://github.com/carlwgeorge/dummy
Source0: dummy.sh
BuildArch: noarch


%description
Dummy package.


%install
install -D -p -m 0755 %{S:0} %{buildroot}%{_bindir}/dummy


%files
%{_bindir}/dummy


%changelog
* Fri Sep 16 2016 Carl George <carl.george@rackspace.com> - 1-1
- Initial package
