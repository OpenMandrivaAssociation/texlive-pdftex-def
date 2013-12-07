# revision 22653
# category Package
# catalog-ctan /macros/latex/contrib/pdftex-def/pdftex.def
# catalog-date 2011-05-28 11:53:45 +0200
# catalog-license lppl1.3
# catalog-version 0.06d
Name:		texlive-pdftex-def
Version:	0.06d
Release:	5
Summary:	Colour and Graphics support for PDFTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pdftex-def/pdftex.def
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdftex-def.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The file pdftex.def provides device-specific definitions for
colour and graphics support when running pdf(La)TeX.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pdftex-def/pdftex.def

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.06d-2
+ Revision: 754768
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.06d-1
+ Revision: 719226
- texlive-pdftex-def
- texlive-pdftex-def
- texlive-pdftex-def
- texlive-pdftex-def

