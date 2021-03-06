# $Id$
# Authority: dag
# Upstream: Koichi Taniguchi <taniguchi@livedoor.jp>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name URI-Escape-JavaScript

Summary: Perl implementation of JavaScript's escape() and unescape() functions
Name: perl-URI-Escape-JavaScript
Version: 0.04
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/URI-Escape-JavaScript/

Source: http://search.cpan.org/CPAN/authors/id/T/TA/TANIGUCHI/URI-Escape-JavaScript-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Encode) >= 2.12
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
BuildRequires: perl >= 5.8.1
Requires: perl(Encode) >= 2.12
Requires: perl >= 5.8.1

%filter_from_requires /^perl*/d
%filter_setup


%description
perl-URI-Escape-JavaScript is a Perl implementation of JavaScript's
escape() and unescape() functions.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/URI::Escape::JavaScript.3pm*
%dir %{perl_vendorlib}/URI/
%dir %{perl_vendorlib}/URI/Escape/
#%{perl_vendorlib}/URI/Escape/JavaScript/
%{perl_vendorlib}/URI/Escape/JavaScript.pm

%changelog
* Mon Mar  8 2010 Christoph Maser <cmr@financial.com> - 0.04-1
- Updated to version 0.04.

* Mon Jun  8 2009 Christoph Maser <cmr@financial.com> - 0.03-1
- Updated to version 0.03.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
