%include	/usr/lib/rpm/macros.perl
%define         pdir      HTML
%define         pnam      Navigation
%define         modname   %{pdir}-%{pnam}

Summary:	HTML-Navigation perl module
Summary(pl):	Modu� perla HTML-Navigation
Name:		perl-%{modname}
Version:	0.26
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	��ȯ/����/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{modname}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::Navigation is Perl module for creating navigation bars/menus of
arbitrary design and structure within HTML documents.

%description -l pl
HTML::Navigation to modu� Perla do tworzeni nawigacyjnych pask�w i
menu o dowolnym wygl�dzie i strukturze w dokumentach HTML.

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
