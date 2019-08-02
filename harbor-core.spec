%define  debug_package %{nil}
%global __os_install_post %{nil}

%define service_user harbor
%define service_group harbor
%define service_homedir /opt/harbor
%define service_logdir /var/log/harbor
%define service_configdir /etc/harbor

Summary: Harbor Core Service
Name: harbor-core
Version: ¤CLEANVERSION¤
Release: ¤BUILDRELEASE¤%{dist}
Source0: harbor-core-¤VERSION¤
Source1: harbor-core.service
Source2: harbor-core.conf-¤RVERSION¤
License: GPLv3
Group: System Tools
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}.buildroot
AutoReqProv: false

%description
%{summary}

%prep

%install
mkdir -p $RPM_BUILD_ROOT%{service_homedir}/core
mkdir -p $RPM_BUILD_ROOT%{service_configdir}/core
mkdir -p $RPM_BUILD_ROOT%{service_configdir}/core/token
mkdir -p $RPM_BUILD_ROOT%{service_configdir}/core/certificates
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
mkdir -p $RPM_BUILD_ROOT%{service_logdir}

install -m 755 %{SOURCE0} %{buildroot}/%{service_homedir}/core/harbor_core
install -m 755 %{SOURCE1} %{buildroot}/%{_unitdir}/harbor-core.service
install -m 755 %{SOURCE2} %{buildroot}/%{service_configdir}/bitwarden-rs.conf


%pre
/usr/bin/getent group %{service_group} >/dev/null || /usr/sbin/groupadd --system %{service_group}
/usr/bin/getent passwd %{service_user} >/dev/null || /usr/sbin/useradd --no-create-home --system -g %{service_group} --home-dir %{service_homedir} -s /bin/bash %{service_user}
/usr/sbin/usermod -s /bin/bash %{service_user}

%post
%systemd_post bitwarden_rs

%preun
%systemd_preun bitwarden_rs

%postun
%systemd_postun bitwarden_rs

%clean

%files
%defattr(0644, bitwarden, bitwarden, 0755)
%config %{service_configdir}/bitwarden-rs.conf
%{service_homedir}/server
%dir %{service_homedir}/server/data
%attr(0755, bitwarden, bitwarden) %{service_homedir}/server/bin/bitwarden_rs
%attr(0644, root, root) %{_unitdir}/bitwarden_rs.service

%changelog
