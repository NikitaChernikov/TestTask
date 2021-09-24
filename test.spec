Name:           test
Version:        0.0.1
Release:        1%{?dist}
Summary:        Test task in RAIDIX!
BuildArch:      noarch

License:        GPLv3+
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

%description
Test task written for RAIDIX company.

%prep
%setup -q 


%build
make %{?_smp_mflags}


%install
%make_install


%files
%{_bindir}/%{name}



%changelog
* Fri Sep 24 2021 root
- First version baing packaged. 
