%define  debug_package %{nil}
%global __os_install_post %{nil}

%define service_user harbor
%define service_group harbor
%define service_homedir /opt/harbor
%define service_logdir /var/log/harbor
%define service_configdir /etc/harbor
%define service_datadir /var/lib/harbor

Summary: Harbor Core Service
Name: harbor-core
Version: ¤CLEANVERSION¤
Release: ¤BUILDRELEASE¤%{dist}
Source0: harbor-core-¤VERSION¤
Source1: harbor-core.service
Source2: prepare-¤VERSION¤/common/config/core/app.conf
Source3: prepare-¤VERSION¤/common/config/core/env
Source4: db-¤VERSION¤.tar.gz
License: GPLv3
Group: System Tools
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}.buildroot
AutoReqProv: false

%description
%{summary}

%prep
tar zxf %{SOURCE4}

%install
mkdir -p $RPM_BUILD_ROOT%{service_homedir}/core
mkdir -p $RPM_BUILD_ROOT%{service_configdir}/db
mkdir -p $RPM_BUILD_ROOT%{service_datadir}/data
mkdir -p $RPM_BUILD_ROOT%{service_configdir}/core
mkdir -p $RPM_BUILD_ROOT%{service_configdir}/core/token
mkdir -p $RPM_BUILD_ROOT%{service_configdir}/core/certificates
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
mkdir -p $RPM_BUILD_ROOT%{service_logdir}

mv db-¤VERSION¤/db/ $RPM_BUILD_ROOT%{service_configdir}/db/initial
mv db-¤VERSION¤/migrations/postgresql $RPM_BUILD_ROOT%{service_configdir}/db/migrations

install -m 755 %{SOURCE0} %{buildroot}/%{service_homedir}/core/harbor_core
install -m 755 %{SOURCE1} %{buildroot}/%{_unitdir}/harbor-core.service
install -m 755 %{SOURCE2} %{buildroot}/%{service_configdir}/core/app.conf
install -m 755 %{SOURCE3} %{buildroot}/%{service_configdir}/core/env

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
%config %{service_configdir}/harbor/core
%config %{service_configdir}/harbor/db
%{service_homedir}/core
%dir %{service_datadir}/data
%attr(0755, bitwarden, bitwarden) %{service_homedir}/core/harbor-core
%attr(0644, root, root) %{_unitdir}/harbor-core.service

%changelog
* Fri Aug 02 2019 16:58:07 +0000 Martin Juhl <mj@casalogic.dk> 1.8.2_rc1
* Fri Aug 02 2019 16:55:21 +0000 Martin Juhl <mj@casalogic.dk> 1.8.2_rc1
* Fri Aug 02 2019 16:53:58 +0000 Martin Juhl <mj@casalogic.dk> 1.8.2_rc1
- New version build: 1.8.2_rc1