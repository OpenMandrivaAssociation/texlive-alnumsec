%global tl_name alnumsec
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.03
Release:	%{tl_revision}.1
Summary:	Alphanumeric section numbering
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/alnumsec
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/alnumsec.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/alnumsec.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/alnumsec.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package allows you to use alphanumeric section numbering, for
instance "A. Introduction ... III. International Law". Its output is
similar to alphanum, but you can use the standard LaTeX sectioning
commands, so that it is possible to switch numbering schemes easily.
Greek letters, double letters (bb) and different delimiters around them
are supported.

