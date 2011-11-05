# revision 22653
# category Package
# catalog-ctan /macros/latex/contrib/pdftex-def/pdftex.def
# catalog-date 2011-05-28 11:53:45 +0200
# catalog-license lppl1.3
# catalog-version 0.06d
Name:		texlive-pdftex-def
Version:	0.06d
Release:	1
Summary:	Colour and Graphics support for PDFTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pdftex-def/pdftex.def
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdftex-def.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3

%description
The file pdftex.def provides device-specific definitions for
colour and graphics support when running pdf(La)TeX.

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
%{_texmfdistdir}/tex/latex/pdftex-def/pdftex.def
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
