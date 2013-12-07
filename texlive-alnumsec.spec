# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/alnumsec
# catalog-date 2008-05-11 02:21:17 +0200
# catalog-license lppl
# catalog-version v0.03
Name:		texlive-alnumsec
Version:	v0.03
Release:	5
Summary:	Alphanumeric section numbering
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/alnumsec
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/alnumsec.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/alnumsec.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/alnumsec.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> v0.03-2
+ Revision: 749163
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> v0.03-1
+ Revision: 717815
- texlive-alnumsec
- texlive-alnumsec
- texlive-alnumsec
- texlive-alnumsec
- texlive-alnumsec

