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
* Wed Dec 30 2020 14:19:04 +0000 Martin Juhl <m@rtinjuhl.dk> 2.1.2_rc1
- New version build: 2.1.2_rc1
* Sun Apr 05 2020 14:09:37 +0000 Martin Juhl <m@rtinjuhl.dk> 1.10.2_rc1
- New version build: 1.10.2_rc1
* Sat Feb 15 2020 03:22:08 +0000 Martin Juhl <m@rtinjuhl.dk> 1.10.1_rc1
* Tue Feb 11 2020 07:09:14 +0000 Martin Juhl <m@rtinjuhl.dk> 1.10.1_rc1
- New version build: 1.10.1_rc1
* Fri Dec 06 2019 11:09:41 +0000 Martin Juhl <m@rtinjuhl.dk> 1.10.0_rc2
- New version build: 1.10.0_rc2
* Fri Nov 22 2019 11:08:55 +0000 Martin Juhl <mj@casalogic.dk> 1.10.0_rc1
- New version build: 1.10.0_rc1
* Wed Nov 20 2019 19:01:50 +0000 Martin Juhl <mj@casalogic.dk> 1.9.3_rc1
* Wed Nov 20 2019 16:47:17 +0000 Martin Juhl <mj@casalogic.dk> 1.9.3_rc1
* Thu Nov 14 2019 19:12:31 +0000 Martin Juhl <mj@casalogic.dk> 1.9.3_rc1
- New version build: 1.9.3_rc1
* Sun Nov 03 2019 15:08:58 +0000 Martin Juhl <mj@casalogic.dk> 1.9.2_rc1
- New version build: 1.9.2_rc1
* Fri Sep 27 2019 14:15:32 +0000 Martin Juhl <mj@casalogic.dk> 1.9.1_rc1
- New version build: 1.9.1_rc1
* Wed Sep 11 2019 18:15:49 +0000 Martin Juhl <mj@casalogic.dk> 1.9.0_rc2
- New version build: 1.9.0_rc2
* Wed Sep 04 2019 06:14:54 +0000 Martin Juhl <mj@casalogic.dk> 1.9.0_rc1
- New version build: 1.9.0_rc1
* Wed Aug 14 2019 12:08:23 +0000 Martin Juhl <mj@casalogic.dk> 1.8.2
* Wed Aug 14 2019 10:41:29 +0000 Martin Juhl <mj@casalogic.dk> 1.8.2
- New version build: 1.8.2
* Tue Aug 13 2019 13:18:23 +0000 Martin Juhl <mj@casalogic.dk> 1.8.2_rc2
* Tue Aug 13 2019 12:17:17 +0000 Martin Juhl <mj@casalogic.dk> 1.8.2_rc2
* Tue Aug 13 2019 11:41:14 +0000 Martin Juhl <mj@casalogic.dk> 1.8.2_rc2
* Tue Aug 13 2019 11:25:34 +0000 Martin Juhl <mj@casalogic.dk> 1.8.2_rc2
- New version build: 1.8.2_rc2

