Name:       c-b18-565-3
Version:    1.0
Release:    1%{?dist}
Summary:    Rustamov Bekhruz ... B18-565 ...
Group:      Testing
License:    GPL
URL:        https://github.com/RustamovBN/my-rpm-package
Source:     %{name}-%{version}.tar.gz
BuildRequires: gcc

%description
A test package

%prep
%setup -q

%build
gcc -O2 -o c-b18-565-3 c-b18-565-3.c

%install
mkdir -p %{buildroot}%{_bindir}
cp c-b18-565-21.c %{buildroot}%{_bindir}

%files
%{_bindir}/c-b18-565-3.c

%changelog
* Fri May 28 2021 Rustamov
- Added %{_bindir}/c-b18-565-3.c
