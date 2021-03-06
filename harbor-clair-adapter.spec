%define  debug_package %{nil}
%global __os_install_post %{nil}

%define service_user harbor
%define service_group harbor
%define service_homedir /opt/harbor
%define service_logdir /var/log/harbor
%define service_configdir /etc/harbor
%define service_datadir /var/lib/harbor

Summary: Harbor Clair Scanning Service Adapter
Name: harbor-clair-adapter
Version: ¤CLEANVERSION¤
Release: ¤BUILDRELEASE¤%{dist}
Source0: harbor-scanner-clair-¤VERSION¤
Source1: harbor-clair-adapter.service
Source2: env
License: GPLv3
Group: System Tools
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}.buildroot
AutoReqProv: false
Requires: git

%description
%{summary}

%prep

%install
mkdir -p $RPM_BUILD_ROOT%{service_homedir}/clair-adapter
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
mkdir -p $RPM_BUILD_ROOT%{service_configdir}/clair-adapter


install -m 755 %{SOURCE0} %{buildroot}/%{service_homedir}/clair-adapter/clair-adapter
install -m 755 %{SOURCE1} %{buildroot}/%{_unitdir}/harbor-clair-adapter.service
install -m 755 %{SOURCE2} %{buildroot}/%{service_configdir}/clair-adapter/env

%pre
/usr/bin/getent group %{service_group} >/dev/null || /usr/sbin/groupadd --system %{service_group}
/usr/bin/getent passwd %{service_user} >/dev/null || /usr/sbin/useradd --no-create-home --system -g %{service_group} --home-dir %{service_homedir} -s /bin/bash %{service_user}
/usr/sbin/usermod -s /bin/bash %{service_user}

%post

%preun

%postun

%clean

%files
%defattr(0644, harbor, harbor, 0755)
%config %{service_configdir}/clair-adapter/env
%{service_homedir}/clair-adapter
%attr(0755, harbor, harbor) %{service_homedir}/clair-adapter/clair-adapter
%attr(0644, root, root) %{_unitdir}/harbor-clair-adapter.service

%changelog
* Sat Jan 09 2021 19:10:43 +0000 Martin Juhl <m@rtinjuhl.dk> 2.1.3_rc2
* Thu Jan 07 2021 03:09:54 +0000 Martin Juhl <m@rtinjuhl.dk> 2.1.3_rc1
* Wed Dec 30 2020 14:19:04 +0000 Martin Juhl <m@rtinjuhl.dk> 2.1.2_rc1
- New version build: 1.1.1
* Sun Apr 05 2020 14:09:37 +0000 Martin Juhl <m@rtinjuhl.dk> 1.10.2_rc1
* Sat Feb 15 2020 03:22:08 +0000 Martin Juhl <m@rtinjuhl.dk> 1.10.1_rc1
* Sat Feb 15 2020 03:03:36 +0000 Martin Juhl <m@rtinjuhl.dk> 1.10.1_rc1
- New version build: 1.0.1
