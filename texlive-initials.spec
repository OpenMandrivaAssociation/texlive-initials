%global tl_name initials
%global tl_revision 54080

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Adobe Type 1 decorative initial fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/initials
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/initials.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/initials.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
For each font, at least a .pfb and a .tfm file is provided, with an .fd
file for use with LaTeX.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from initials:
Map Acorn.map
Map AnnSton.map
Map ArtNouv.map
Map ArtNouvc.map
Map Carrickc.map
Map Eichenla.map
Map Eileen.map
Map EileenBl.map
Map Elzevier.map
Map GotIn.map
Map GoudyIn.map
Map Kinigcap.map
Map Konanur.map
Map Kramer.map
Map MorrisIn.map
Map Nouveaud.map
Map Romantik.map
Map Rothdn.map
Map RoyalIn.map
Map Sanremo.map
Map Starburst.map
Map Typocaps.map
Map Zallman.map
TL_DROPIN_EOF
