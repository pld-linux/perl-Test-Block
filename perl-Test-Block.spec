#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Test
%define	pnam	Block
Summary:	Test::Block - Specify fine granularity test plans
#Summary(pl):	
Name:		perl-Test-Block
Version:	0.11
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/A/AD/ADIE/Test-Block-0.11.tar.gz
# Source0-md5:	386a722947f2c77f6157d1dea0338e35
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Test::Builder::Tester) >= 1.01
BuildRequires:	perl(Test::Exception) >= 0.15
BuildRequires:	perl >= 5.6.1
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows you to specify the number of expected tests at a finer level
of granularity than an entire test script. It is built with Test::Builder and
plays happily with Test::More and friends.

If you are not already familiar with Test::More now would be the time to go
take a look.

Test::Block supplies a special variable $Plan that you can localize to specify
the number of tests in a block.


# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%{perl_vendorlib}/Test/*.pm
#%%{perl_vendorlib}/Test/Block
%{_mandir}/man3/*
