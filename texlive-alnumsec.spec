Name:		texlive-alnumsec
Version:	15878
Release:	3
Summary:	Alphanumeric section numbering
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/alnumsec
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/alnumsec.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/alnumsec.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/alnumsec.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package allows you to use alphanumeric section numbering,
for instance "A. Introduction ... III. International Law". Its
output is similar to alphanum, but you can use the standard
LaTeX sectioning commands, so that it is possible to switch
numbering schemes easily. Greek letters, double letters (bb)
and different delimiters around them are supported.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
