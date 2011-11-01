Name:		texlive-alnumsec
Version:	v0.03
Release:	1
Summary:	Alphanumeric section numbering
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/alnumsec
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/alnumsec.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/alnumsec.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/alnumsec.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package allows you to use alphanumeric section numbering,
for instance "A. Introduction ... III. International Law". Its
output is similar to alphanum, but you can use the standard
LaTeX sectioning commands, so that it is possible to switch
numbering schemes easily. Greek letters, double letters (bb)
and different delimiters around them are supported.

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
%{_texmfdistdir}/tex/latex/alnumsec/alnumsec.sty
%doc %{_texmfdistdir}/doc/latex/alnumsec/README
%doc %{_texmfdistdir}/doc/latex/alnumsec/alnumsec.pdf
#- source
%doc %{_texmfdistdir}/source/latex/alnumsec/alnumsec.dtx
%doc %{_texmfdistdir}/source/latex/alnumsec/alnumsec.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
