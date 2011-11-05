# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/pseudocode
# catalog-date 2009-03-02 13:24:03 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-pseudocode
Version:	20090302
Release:	1
Summary:	LaTeX environment for specifying algorithms in a natural way
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pseudocode
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pseudocode.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pseudocode.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This package provides the environment "pseudocode" for
describing algorithms in a natural manner.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pseudocode/pseudocode.sty
%doc %{_texmfdistdir}/doc/latex/pseudocode/README
%doc %{_texmfdistdir}/doc/latex/pseudocode/pseudocode.pdf
%doc %{_texmfdistdir}/doc/latex/pseudocode/pseudocode.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
