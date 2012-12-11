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

%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.3600-4mdv2010.0
+ Revision: 430598
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.3600-3mdv2009.0
+ Revision: 241981
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.3600-1mdv2008.0
+ Revision: 77705
- update to new version 0.3600


* Wed Nov 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.3500-1mdv2007.0
+ Revision: 88632
- Import perl-Test-LectroTest

* Wed Nov 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.3500-1mdv2007.1
- first mdv release

