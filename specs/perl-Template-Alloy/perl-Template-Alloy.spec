# $Id$
# Authority: dag
# Upstream: Paul Seamons <perl$seamons,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Template-Alloy

Summary: TT2/3, HT, HTE, Tmpl, and Velocity Engine
Name: perl-Template-Alloy
Version: 1.016
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Template-Alloy/

Source: http://search.cpan.org/CPAN/authors/id/R/RH/RHANDOM/Template-Alloy-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(Digest::MD5) >= 1
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl(Digest::MD5) >= 1

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
perl-Template-Alloy is a Perl module that implements a TT2/3, HT, HTE,
Tmpl, and Velocity Engine.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find samples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST MANIFEST.SKIP META.yml README samples/
%doc %{_mandir}/man3/Template::Alloy.3pm*
%doc %{_mandir}/man3/Template::Alloy::*.3pm*
%dir %{perl_vendorlib}/Template/
%{perl_vendorlib}/Template/Alloy/
%{perl_vendorlib}/Template/Alloy.pm
%{perl_vendorlib}/Template/Alloy.pod

%changelog
* Thu Feb 10 2011 Christoph Maser <cmaser@gmx.de> - 1.016-1
- Updated to version 1.016.

* Fri Jun 12 2009 Christoph Maser <cmr@financial.com> - 1.013-1
- Updated to version 1.013.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 1.012-1
- Updated to release 1.012.

* Fri Dec 14 2007 Dag Wieers <dag@wieers.com> - 1.011-1
- Updated to release 1.011.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.009-1
- Updated to release 1.009.

* Tue Aug 07 2007 Dag Wieers <dag@wieers.com> - 1.006-1
- Initial package. (using DAR)
