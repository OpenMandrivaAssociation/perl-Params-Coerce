%define upstream_name    Params-Coerce
%define upstream_version 0.14

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Allows your classes to do coercion of parameters
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Params/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(Params::Util)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
A big part of good API design is that we should be able to be flexible in
the ways that we take parameters.

Params::Coerce attempts to encourage this, by making it easier to take a
variety of different arguments, while adding negligable additional
complexity to your code.

What is Coercion
    "Coercion" in computing terms generally referse to "implicit type
    conversion". This is where data and object are converted from one type
    to another behind the scenes, and you just just magically get what you
    need.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/Params


%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.140.0-1mdv2010.0
+ Revision: 404282
- rebuild using %%perl_convert_version

* Sun Jul 13 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.14-1mdv2009.0
+ Revision: 234303
- import perl-Params-Coerce


* Sun Jul 13 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.14-1mdv2009.0
- initial mdv release, generated with cpan2dist


