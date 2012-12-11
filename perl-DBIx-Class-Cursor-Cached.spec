%define upstream_name   DBIx-Class-Cursor-Cached
%define upstream_version    1.001001

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Cursor class with built-in caching support
Url:		http://search.cpan.org/dist/%{upstream_name}
Source:		http://www.cpan.org/modules/by-module/DBIx/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Cache::FileCache)
BuildRequires:	perl(DBIx::Class)
BuildRequires:	perl(DBD::SQLite)
BuildRequires:	perl(Digest::SHA1)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
This package provides cursor class with built-in caching support.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.1.1-2mdv2011.0
+ Revision: 657402
- rebuild for updated spec-helper

* Mon Apr 04 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.1-1
+ Revision: 650298
- update to new version 1.001001

* Fri Mar 25 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.0-1
+ Revision: 648531
- update to new version 1.001000

* Sat Jun 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.1-1mdv2011.0
+ Revision: 389934
- import perl-DBIx-Class-Cursor-Cached


* Sat Jun 27 2009 cpan2dist 1.0.1-1mdv
- initial mdv release, generated with cpan2dist

