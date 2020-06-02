#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-GIS-Distance
Version  : 0.18
Release  : 5
URL      : https://cpan.metacpan.org/authors/id/B/BL/BLUEFEET/GIS-Distance-0.18.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BL/BLUEFEET/GIS-Distance-0.18.tar.gz
Summary  : 'Calculate geographic distances.'
Group    : Development/Tools
License  : GPL-3.0
Requires: perl-GIS-Distance-license = %{version}-%{release}
Requires: perl-GIS-Distance-perl = %{version}-%{release}
Requires: perl(Class::Measure::Length)
BuildRequires : buildreq-cpan
BuildRequires : perl(ExtUtils::Config)
BuildRequires : perl(ExtUtils::Helpers)
BuildRequires : perl(ExtUtils::InstallPaths)
BuildRequires : perl(Module::Build::Tiny)

%description
# NAME
GIS::Distance - Calculate geographic distances.
# SYNOPSIS
```perl
use GIS::Distance;

%package dev
Summary: dev components for the perl-GIS-Distance package.
Group: Development
Provides: perl-GIS-Distance-devel = %{version}-%{release}
Requires: perl-GIS-Distance = %{version}-%{release}

%description dev
dev components for the perl-GIS-Distance package.


%package license
Summary: license components for the perl-GIS-Distance package.
Group: Default

%description license
license components for the perl-GIS-Distance package.


%package perl
Summary: perl components for the perl-GIS-Distance package.
Group: Default
Requires: perl-GIS-Distance = %{version}-%{release}

%description perl
perl components for the perl-GIS-Distance package.


%prep
%setup -q -n GIS-Distance-0.18
cd %{_builddir}/GIS-Distance-0.18

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-GIS-Distance
cp %{_builddir}/GIS-Distance-0.18/LICENSE %{buildroot}/usr/share/package-licenses/perl-GIS-Distance/31a3d460bb3c7d98845187c716a30db81c44b615
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/GIS::Distance.3
/usr/share/man/man3/GIS::Distance::ALT.3
/usr/share/man/man3/GIS::Distance::Constants.3
/usr/share/man/man3/GIS::Distance::Cosine.3
/usr/share/man/man3/GIS::Distance::Formula.3
/usr/share/man/man3/GIS::Distance::GreatCircle.3
/usr/share/man/man3/GIS::Distance::Haversine.3
/usr/share/man/man3/GIS::Distance::MathTrig.3
/usr/share/man/man3/GIS::Distance::Null.3
/usr/share/man/man3/GIS::Distance::Polar.3
/usr/share/man/man3/GIS::Distance::Vincenty.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-GIS-Distance/31a3d460bb3c7d98845187c716a30db81c44b615

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.3/GIS/Distance.pm
/usr/lib/perl5/vendor_perl/5.30.3/GIS/Distance/ALT.pm
/usr/lib/perl5/vendor_perl/5.30.3/GIS/Distance/Constants.pm
/usr/lib/perl5/vendor_perl/5.30.3/GIS/Distance/Cosine.pm
/usr/lib/perl5/vendor_perl/5.30.3/GIS/Distance/Formula.pm
/usr/lib/perl5/vendor_perl/5.30.3/GIS/Distance/GreatCircle.pm
/usr/lib/perl5/vendor_perl/5.30.3/GIS/Distance/Haversine.pm
/usr/lib/perl5/vendor_perl/5.30.3/GIS/Distance/MathTrig.pm
/usr/lib/perl5/vendor_perl/5.30.3/GIS/Distance/Null.pm
/usr/lib/perl5/vendor_perl/5.30.3/GIS/Distance/Polar.pm
/usr/lib/perl5/vendor_perl/5.30.3/GIS/Distance/Vincenty.pm
