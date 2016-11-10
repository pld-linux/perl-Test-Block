#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Test
%define	pnam	Block
Summary:	Test::Block - Specify fine granularity test plans
Summary(pl.UTF-8):	Test::Block - określanie szczegółowych planów testów
Name:		perl-Test-Block
Version:	0.13
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f4e289f7f2a333983f1e4d578d82f5a3
# https://rt.cpan.org/Ticket/Attachment/1600903/856113/0001-Make-Test-Block-work-with-perl-5.23.8.patch
Patch0:		%{name}-perl5.24.patch
URL:		http://search.cpan.org/dist/Test-Block/
BuildRequires:	perl-Module-Build >= 0.38
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Test::Builder) >= 0.17
BuildRequires:	perl-Test-Builder-Tester >= 1.01
BuildRequires:	perl-Test-Exception >= 0.15
BuildRequires:	perl-Test-Simple >= 0.47
%endif
Requires:	perl-base
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	perl(Tie::StdScalar)

%description
This module allows you to specify the number of expected tests at a
finer level of granularity than an entire test script. It is built
with Test::Builder and plays happily with Test::More and friends.

%description -l pl.UTF-8
Ten moduł pozwala na określanie liczby oczekiwanych testów na poziomie
dokładniejszym niż cały skrypt testowy. Jest stworzony w oparciu o
Test::Builder i dobrze współpracuje z Test::More oraz podobnymi.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p2

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Test/Block.pm
%{_mandir}/man3/Test::Block.3pm*
