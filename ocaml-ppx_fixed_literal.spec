#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Simpler notation for fixed point literals
Summary(pl.UTF-8):	Prostsza notacja dla stałych stałoprzecinkowych
Name:		ocaml-ppx_fixed_literal
Version:	0.14.0
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/ppx_fixed_literal/tags
Source0:	https://github.com/janestreet/ppx_fixed_literal/archive/v%{version}/ppx_fixed_literal-%{version}.tar.gz
# Source0-md5:	52c54456db2017363e0bcaaaca90fcea
URL:		https://github.com/janestreet/ppx_fixed_literal
BuildRequires:	ocaml >= 1:4.04.2
BuildRequires:	ocaml-base-devel >= 0.14
BuildRequires:	ocaml-base-devel < 0.15
BuildRequires:	ocaml-dune >= 2.0.0
BuildRequires:	ocaml-ppxlib-devel >= 0.11.0
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
A ppx rewriter that rewrites fixed point literal of the form 1.0v to
conversion functions currently in scope.

This package contains files needed to run bytecode executables using
ppx_fixed_literal library.

%description -l pl.UTF-8
Moduł przepisujący ppx przepisujący literały stałoprzecinkowe postaci
1.0v na obecne w kontekście funkcje konwersji.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki ppx_fixed_literal.

%package devel
Summary:	Simpler notation for fixed point literals - development part
Summary(pl.UTF-8):	Prostsza notacja dla stałych stałoprzecinkowych - część programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-base-devel >= 0.14
Requires:	ocaml-ppxlib-devel >= 0.11.0

%description devel
This package contains files needed to develop OCaml programs using
ppx_fixed_literal library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki ppx_fixed_literal.

%prep
%setup -q -n ppx_fixed_literal-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ppx_fixed_literal/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/ppx_fixed_literal

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.md
%dir %{_libdir}/ocaml/ppx_fixed_literal
%attr(755,root,root) %{_libdir}/ocaml/ppx_fixed_literal/ppx.exe
%{_libdir}/ocaml/ppx_fixed_literal/META
%{_libdir}/ocaml/ppx_fixed_literal/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/ppx_fixed_literal/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/ppx_fixed_literal/*.cmi
%{_libdir}/ocaml/ppx_fixed_literal/*.cmt
%{_libdir}/ocaml/ppx_fixed_literal/*.cmti
%{_libdir}/ocaml/ppx_fixed_literal/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/ppx_fixed_literal/ppx_fixed_literal.a
%{_libdir}/ocaml/ppx_fixed_literal/*.cmx
%{_libdir}/ocaml/ppx_fixed_literal/*.cmxa
%endif
%{_libdir}/ocaml/ppx_fixed_literal/dune-package
%{_libdir}/ocaml/ppx_fixed_literal/opam
