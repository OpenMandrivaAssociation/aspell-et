%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.1.21-1
%define fname aspell6-%{languagecode}
%define aspell_ver 0.60
%define languageenglazy Estonian
%define languagecode et
%define lc_ctype et_EE

Summary:	%{languageenglazy} files for aspell
Name:		aspell-%{languagecode}
Version:	0.1.21.1
Release:	15
Group:		System/Internationalization
License:	LGPLv2
Url:		http://aspell.net/
Source0:	http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2

BuildRequires:	aspell >= %{aspell_ver}
BuildRequires:	make
Requires:	aspell >= %{aspell_ver}
# Mandriva Stuff
Requires:	locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 1
Provides:	aspell-dictionary
Provides:	aspell-%{lc_ctype}
Provides:	spell-%{languagecode}
Autoreqprov:	no

%description
An %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -qn %{fname}-%{src_ver}

%build
# don't use configure macro
./configure

%make

%install
%makeinstall_std

chmod 644 Copyright README* 

%files
%doc README* Copyright doc/*
%{_libdir}/aspell-%{aspell_ver}/*

