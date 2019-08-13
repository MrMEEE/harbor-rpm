%define  debug_package %{nil}
%global __os_install_post %{nil}

%define service_user harbor
%define service_group harbor
%define service_homedir /opt/harbor
%define service_logdir /var/log/harbor
%define service_configdir /etc/harbor
%define service_datadir /var/lib/harbor

Summary: Harbor Job Service
Name: harbor-jobservice
Version: ¤CLEANVERSION¤
Release: ¤BUILDRELEASE¤%{dist}
Source0: harbor_jobservice-¤VERSION¤
Source1: harbor-jobservice.service
Source2: env
Source3: config.yml
License: GPLv3
Group: System Tools
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}.buildroot
AutoReqProv: false

%description
%{summary}

%prep

%install
mkdir -p $RPM_BUILD_ROOT%{service_homedir}/jobservice
mkdir -p $RPM_BUILD_ROOT%{service_configdir}/jobservice
mkdir -p $RPM_BUILD_ROOT%{service_logdir}/jobs
mkdir -p $RPM_BUILD_ROOT%{_unitdir}

install -m 755 %{SOURCE0} %{buildroot}/%{service_homedir}/jobservice/harbor_jobservice
install -m 755 %{SOURCE1} %{buildroot}/%{_unitdir}/harbor-jobservice.service
install -m 755 %{SOURCE2} %{buildroot}/%{service_configdir}/jobservice/env
install -m 755 %{SOURCE3} %{buildroot}/%{service_configdir}/jobservice/config.yml

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
%config %{service_configdir}/jobservice
%{service_homedir}/jobservice
%dir %{service_logdir}/jobs
%attr(0755, harbor, harbor) %{service_homedir}/jobservice/harbor_jobservice
%attr(0644, root, root) %{_unitdir}/harbor-jobservice.service

%changelog
* Tue Aug 13 2019 11:25:34 +0000 Martin Juhl <mj@casalogic.dk> 1.8.2_rc2
* Tue Aug 13 2019 10:15:29 +0000 Martin Juhl <mj@casalogic.dk> 1.8.2_rc2
- New version build: 1.8.2_rc2

