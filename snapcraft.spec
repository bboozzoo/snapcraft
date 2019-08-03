%bcond_without check

%global provider_prefix github.com/snapcore/snapcraft

Name:           snapcraft
Version:        3.7
Release:        1%{?dist}
Summary:        A convenience tool for building snaps

License:        GPLv3
URL:            https://github.com/snapcore/snapcraft
Source0:        https://%{provider_prefix}/archive/%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-click
BuildRequires:  python3-devel
BuildRequires:  python3-jsonschema
BuildRequires:  python3-progressbar2
BuildRequires:  python3-pyelftools
BuildRequires:  python3-pymacaroons-pynacl
BuildRequires:  python3-pyxdg
BuildRequires:  python3-requests
BuildRequires:  python3-requests-toolbelt
BuildRequires:  python3-requests-unixsocket
BuildRequires:  python3-tabulate
%if %{with check}
BuildRequires:  python3-fixtures
BuildRequires:  python3-lxml
BuildRequires:  python3-pyramid
BuildRequires:  python3-testscenarios
BuildRequires:  xdelta
%endif

%description
Snapcraft is a convenience tool for packaging and publishing software as snaps.

%prep
%autosetup -n %{name}-%{version}


%build
%py3_build


%install
%py3_install


%if %{with check}
%check
# run unit tests only
#%{__python3} setup.py test
# TODO tests fail, need patching
%endif

%files
%license COPYING
%doc README.md
%{python3_sitelib}/*
%{_bindir}/snapcraft
%{_bindir}/snapcraftctl
%{_datadir}/snapcraft


%changelog
* Sat Aug  3 2019 Maciek Borzecki <maciek.borzecki@gmail.com>
- Initial packaging
