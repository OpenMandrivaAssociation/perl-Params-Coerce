%define module   Params-Coerce
%define version    0.14
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Allows your classes to do coercion of parameters
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Params/%{module}-%{version}.tar.gz
BuildRequires: perl(Carp)
BuildRequires: perl(Params::Util)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/Params

