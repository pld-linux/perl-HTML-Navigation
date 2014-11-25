#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	HTML
%define		pnam	Navigation
%include	/usr/lib/rpm/macros.perl
Summary:	HTML::Navigation perl module
Summary(pl.UTF-8):	Moduł perla HTML::Navigation
Name:		perl-HTML-Navigation
Version:	0.26
Release:	6
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	92e06c381bcf256674d120a5990dd94e
URL:		http://search.cpan.org/dist/HTML-Navigation/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::Navigation is Perl module for creating navigation bars/menus of
arbitrary design and structure within HTML documents.

%description -l pl.UTF-8
HTML::Navigation to moduł Perla do tworzeni nawigacyjnych pasków i
menu o dowolnym wyglądzie i strukturze w dokumentach HTML.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%{perl_vendorlib}/HTML/*.pm
%{_mandir}/man3/*
