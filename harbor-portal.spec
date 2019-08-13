%define  debug_package %{nil}
%global __os_install_post %{nil}

%define service_user harbor
%define service_group harbor
%define service_homedir /opt/harbor
%define service_logdir /var/log/harbor
%define service_configdir /etc/harbor
%define service_datadir /var/lib/harbor

Summary: Harbor Portal
Name: harbor-portal
Version: ¤CLEANVERSION¤
Release: ¤BUILDRELEASE¤%{dist}
Source0: portal-¤VERSION¤.tar.gz
License: GPLv3
Group: System Tools
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}.buildroot
AutoReqProv: false

%description
%{summary}

%prep

%install
mkdir -p $RPM_BUILD_ROOT%{service_homedir}/portal

cd $RPM_BUILD_ROOT%{service_homedir}/portal && tar zxf %{SOURCE0}

%pre

%post

%preun

%postun

%clean

%files
%defattr(0644, harbor, nginx, 0755)
%{service_homedir}/portal

%changelog
* Tue Aug 13 2019 11:25:34 +0000 Martin Juhl <mj@casalogic.dk> 1.8.2_rc2
- New version build: 1.8.2_rc2

