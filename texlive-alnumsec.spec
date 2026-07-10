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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package allows you to use alphanumeric section numbering, for
instance "A. Introduction ... III. International Law". Its output is
similar to alphanum, but you can use the standard LaTeX sectioning
commands, so that it is possible to switch numbering schemes easily.
Greek letters, double letters (bb) and different delimiters around them
are supported.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/alnumsec
%dir %{_datadir}/texmf-dist/source/latex/alnumsec
%dir %{_datadir}/texmf-dist/tex/latex/alnumsec
%doc %{_datadir}/texmf-dist/doc/latex/alnumsec/README
%doc %{_datadir}/texmf-dist/doc/latex/alnumsec/alnumsec.pdf
%doc %{_datadir}/texmf-dist/source/latex/alnumsec/alnumsec.dtx
%doc %{_datadir}/texmf-dist/source/latex/alnumsec/alnumsec.ins
%{_datadir}/texmf-dist/tex/latex/alnumsec/alnumsec.sty
