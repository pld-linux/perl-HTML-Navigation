#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	Navigation
%define         modname   %{pdir}-%{pnam}

Summary:	HTML::Navigation perl module
Summary(pl):	Modu³ perla HTML::Navigation
Name:		perl-%{modname}
Version:	0.26
Release:	5
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{modname}-%{version}.tar.gz
# Source0-md5:	92e06c381bcf256674d120a5990dd94e
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::Navigation is Perl module for creating navigation bars/menus of
arbitrary design and structure within HTML documents.

%description -l pl
HTML::Navigation to modu³ Perla do tworzeni nawigacyjnych pasków i
menu o dowolnym wygl±dzie i strukturze w dokumentach HTML.

%prep
%setup -q -n %{modname}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
