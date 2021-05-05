Name:		RPM test		
Version:	1
Release:	1%{?dist}
Summary:	test for rpm build

Group:		Massie
License:	GPL
URL:		https://github.com/massiecd/rpmspec.git
Source0:	test.tar

%description
This is a test for building an rpm

%prep
%setup -q


%build
%install


%install
install -m 0755 -d $RPM_BUILD_ROOT/opt/test.txt

%files
/opt/test.txt



%changelog
* Wed Jan 05 2021 Christopher Massie 1.0.0
  - Initial release
