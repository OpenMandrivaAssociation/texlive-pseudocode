Name:		texlive-pseudocode
Version:	54080
Release:	2
Summary:	LaTeX environment for specifying algorithms in a natural way
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pseudocode
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pseudocode.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pseudocode.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides the environment "pseudocode" for
describing algorithms in a natural manner.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pseudocode/pseudocode.sty
%doc %{_texmfdistdir}/doc/latex/pseudocode/README
%doc %{_texmfdistdir}/doc/latex/pseudocode/pseudocode.pdf
%doc %{_texmfdistdir}/doc/latex/pseudocode/pseudocode.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
