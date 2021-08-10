Name:               init-headphone
Version:            0.14
Release:            1%{?dist}
Summary:            Manage the headphone amplifier found in some Clevo laptops
License:            GPLv3+
URL:                https://github.com/Unrud/%{name}
Source0:            https://github.com/Unrud/%{name}/archive/v%{version}.tar.gz
%{?systemd_requires}
BuildRequires:      python3-devel, systemd, kmod
Requires:           python3, kmod
BuildArch:          noarch

%description
Manage the headphone amplifier found in some Clevo laptops. Can initialize the
device if headphones are not working after suspend.

%prep
%autosetup -n %{name}-%{version}
cat << EOF > 80-%{name}.preset
enable init-headphone.service
EOF

%build
./autogen.sh
%configure
%make_build

%install
%make_install
%py3_shebang_fix %{buildroot}%{_sbindir}/%{name}
install -D -t %{buildroot}/usr/lib/systemd/system-preset 80-%{name}.preset


%files
%license COPYING
%doc README.md NEWS.md
%{_sbindir}/%{name}
%{_unitdir}/%{name}.service
/usr/lib/systemd/system-preset/80-%{name}.preset

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service
