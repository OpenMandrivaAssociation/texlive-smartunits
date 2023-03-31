Name:		texlive-smartunits
Version:	39592
Release:	2
Summary:	Converting between common metric and Imperial units
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/smartunits
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/smartunits.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/smartunits.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX package implements a \SmartUnit macro for converting
between (some) metric and Imperial units. The package requires
pgfkeys and siunitx.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/smartunits
%doc %{_texmfdistdir}/doc/latex/smartunits

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
