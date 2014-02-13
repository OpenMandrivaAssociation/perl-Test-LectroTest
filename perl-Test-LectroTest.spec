%define debug_package %{nil}

%define module  Test-LectroTest

Name:		perl-%{module}
Version:	0.3600
Release:	5
Summary:	Easy, automatic, specification-based tests
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Test/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel

%description 
This module provides a simple (yet full featured) interface to LectroTest, an
automated, specification-based testing system for Perl. To use it, declare
properties that specify the expected behavior of your software. LectroTest then
checks your software to see whether those properties hold.

%prep
%setup -q -n %{module}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%check
%make test

%files
%doc Changes README
%{perl_vendorlib}/Test
%{_mandir}/*/*
