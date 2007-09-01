%define module  Test-LectroTest
%define name    perl-%{module}
%define version 0.3600
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Easy, automatic, specification-based tests
License:        GPL or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Test/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description 
This module provides a simple (yet full featured) interface to LectroTest, an
automated, specification-based testing system for Perl. To use it, declare
properties that specify the expected behavior of your software. LectroTest then
checks your software to see whether those properties hold.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%check
%make test

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Test
%{_mandir}/*/*


