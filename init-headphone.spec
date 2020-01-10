Name:               init-headphone
Version:            0.13
Release:            1%{?dist}
Summary:            Manage the headphone amplifier found in some Clevo laptops
License:            GPLv3+
URL:                https://github.com/Unrud/%{name}
Source0:            https://github.com/Unrud/%{name}/archive/v%{version}.tar.gz
%{?systemd_requires}
BuildRequires:      python3, systemd
Requires:           python3
BuildArch:          noarch

%description
Manage the headphone amplifier found in some Clevo laptops. Can initialize the
device if headphones are not working after suspend.

%prep
%autosetup -n %{name}-%{version}

%build
./autogen.sh
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc README.md NEWS.md
%{_sbindir}/%{name}
%{_unitdir}/%{name}.service

%post
%systemd_post %{name}.service
if [ "$1" = 1 ] ; then
  /bin/systemctl --no-reload enable %{name}.service >/dev/null 2>&1 || :
fi
if /bin/systemctl is-enabled %{name}.service >/dev/null 2>&1 ; then
  /bin/systemctl start %{name}.service >/dev/null 2>&1 || :
fi

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun %{name}.service
