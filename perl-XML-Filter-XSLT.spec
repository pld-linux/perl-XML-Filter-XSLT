#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	Filter-XSLT
Summary:	XML::Filter::XSLT - XSLT as a SAX filter
Summary(pl):	XML::Filter::XSLT - XSLT jako filtr SAX
Name:		perl-XML-Filter-XSLT
Version:	0.03
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8128f541da6a5a2ee6a3f4764c0652b5
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-XML-LibXSLT >= 1.31
BuildRequires:	perl-XML-SAX >= 0.03
BuildRequires:	perl-XML-SAX-Writer >= 0.20
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It is a simple XSLT SAX2 filter.  It uses any available XSLT processor
on your system that we can use in some SAXy way.  Currently this is
just XML::LibXSLT (which we use to build a DOM tree), but we expect
more processors will be added over time.

%description -l pl
Jest to prosty filtr XSLT dla SAX2. Korzysta z dowolnego dostêpnêgo w
systemie procesora XSLT, z którego potrafi korzystaæ w jaki¶
SAX-opodobny sposób. Aktualnie jest to po prostu XML::LibXSLT (u¿ywany
do tworzenia drzewa DOM), lecz oczekuje siê dodania za jaki¶ czas
wiêkszej liczby procesorów.

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
%{perl_vendorlib}/%{pdir}/*/*
%{_mandir}/man3/*
