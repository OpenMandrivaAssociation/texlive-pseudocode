%global tl_name pseudocode
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	LaTeX environment for specifying algorithms in a natural way
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pseudocode
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pseudocode.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pseudocode.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides the environment "pseudocode" for describing
algorithms in a natural manner.

