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

install -m 755 %{SOURCE0} %{buildroot}/%{service_homedir}/core/harbor_core
install -m 755 %{SOURCE1} %{buildroot}/%{_unitdir}/harbor-core.service
install -m 755 %{SOURCE2} %{buildroot}/%{service_configdir}/core/app.conf
install -m 755 %{SOURCE3} %{buildroot}/%{service_configdir}/core/env
install -m 755 %{SOURCE5} %{buildroot}/%{service_homedir}/core/views/reset-password-mail.tpl
install -m 755 %{SOURCE6} %{buildroot}/%{service_homedir}/core/views/404.tpl

%pre
/usr/bin/getent group %{service_group} >/dev/null || /usr/sbin/groupadd --system %{service_group}
/usr/bin/getent passwd %{service_user} >/dev/null || /usr/sbin/useradd --no-create-home --system -g %{service_group} --home-dir %{service_homedir} -s /bin/bash %{service_user}
/usr/sbin/usermod -s /bin/bash %{service_user}

%post
%systemd_post harbor-core

%preun
%systemd_preun harbor-core

%postun
%systemd_postun harbor-core

%clean

%files
%defattr(0644, harbor, harbor, 0755)
%config %{service_configdir}/core
%config %{service_configdir}/db
%{service_homedir}/core
%dir %{service_datadir}/data
%attr(0755, bitwarden, bitwarden) %{service_homedir}/core/harbor_core
%attr(0644, root, root) %{_unitdir}/harbor-core.service

%changelog
* Fri Aug 02 2019 16:58:07 +0000 Martin Juhl <mj@casalogic.dk> 1.8.2_rc1
* Fri Aug 02 2019 16:55:21 +0000 Martin Juhl <mj@casalogic.dk> 1.8.2_rc1
* Fri Aug 02 2019 16:53:58 +0000 Martin Juhl <mj@casalogic.dk> 1.8.2_rc1
- New version build: 1.8.2_rc1
