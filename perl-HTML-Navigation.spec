%include	/usr/lib/rpm/macros.perl
%define         pdir      HTML
%define         pnam      Navigation
%define         modname   %{pdir}-%{pnam}

Summary:	HTML-Navigation perl module
Summary(pl):	Modu³ perla HTML-Navigation
Name:		perl-%{modname}
Version:	0.26
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{modname}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::Navigation is Perl module for creating navigation bars/menus of
arbitrary design and structure within HTML documents.

%prep
%setup -q -n %{modname}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT
gzip -9nf README ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
