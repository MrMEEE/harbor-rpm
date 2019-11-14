%define  debug_package %{nil}
%global __os_install_post %{nil}

%define service_user harbor
%define service_group harbor
%define service_homedir /opt/harbor
%define service_logdir /var/log/harbor
%define service_configdir /etc/harbor
%define service_datadir /var/lib/harbor/registry

Summary: Harbor Registry Service
Name: harbor-registry
Version: ¤CLEANVERSION¤
Release: ¤BUILDRELEASE¤%{dist}
Source0: registry-¤VERSION¤
Source1: harbor-registry.service
Source2: config.yml 
License: GPLv3
Group: System Tools
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}.buildroot
AutoReqProv: false

%description
%{summary}

%prep

%install
mkdir -p $RPM_BUILD_ROOT%{service_homedir}/registry
mkdir -p $RPM_BUILD_ROOT%{service_configdir}/registry
mkdir -p $RPM_BUILD_ROOT%{service_datadir}
mkdir -p $RPM_BUILD_ROOT%{_unitdir}

install -m 755 %{SOURCE0} %{buildroot}/%{service_homedir}/registry/registry
install -m 755 %{SOURCE1} %{buildroot}/%{_unitdir}/harbor-registry.service
install -m 755 %{SOURCE2} %{buildroot}/%{service_configdir}/registry/config.yml

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
%config %{service_configdir}/registry
%{service_homedir}/registry
%attr(0755, harbor, harbor) %{service_homedir}/registry/registry
%attr(0644, root, root) %{_unitdir}/harbor-registry.service
%{service_datadir}

%changelog
* Thu Nov 14 2019 19:12:31 +0000 Martin Juhl <mj@casalogic.dk> 1.9.3_rc1
* Sun Nov 03 2019 15:08:58 +0000 Martin Juhl <mj@casalogic.dk> 1.9.2_rc1
* Fri Sep 27 2019 14:15:32 +0000 Martin Juhl <mj@casalogic.dk> 1.9.1_rc1
* Wed Sep 11 2019 18:15:49 +0000 Martin Juhl <mj@casalogic.dk> 1.9.0_rc2
* Wed Sep 04 2019 06:14:54 +0000 Martin Juhl <mj@casalogic.dk> 1.9.0_rc1
* Wed Aug 14 2019 12:08:23 +0000 Martin Juhl <mj@casalogic.dk> 1.8.2
* Wed Aug 14 2019 10:41:29 +0000 Martin Juhl <mj@casalogic.dk> 1.8.2
* Tue Aug 13 2019 13:18:23 +0000 Martin Juhl <mj@casalogic.dk> 1.8.2_rc2
* Tue Aug 13 2019 12:17:17 +0000 Martin Juhl <mj@casalogic.dk> 1.8.2_rc2
* Tue Aug 13 2019 11:41:14 +0000 Martin Juhl <mj@casalogic.dk> 1.8.2_rc2
* Tue Aug 13 2019 11:25:34 +0000 Martin Juhl <mj@casalogic.dk> 1.8.2_rc2
- New version build: 2.7.1
