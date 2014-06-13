# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/pseudocode
# catalog-date 2009-03-02 13:24:03 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-pseudocode
Version:	20090302
Release:	7
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20090302-2
+ Revision: 755144
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20090302-1
+ Revision: 719317
- texlive-pseudocode
- texlive-pseudocode
- texlive-pseudocode
- texlive-pseudocode

